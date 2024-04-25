import sys
import cv2
import os
import numpy as np
import torch
import torch.nn as nn
import torchvision.transforms as T
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QFileDialog, \
    QSlider, QProgressBar, QStatusBar, QListWidget
from PySide6.QtCore import QThread, Slot, Signal, Qt, QObject, QSize, QWaitCondition, QMutex
from PySide6.QtGui import QImage, QPixmap
from PIL import Image
from torchvision import transforms
from ultralytics import YOLO
from clipreid.model.make_model_clipreid import make_model
from clipreid.datasets.make_dataloader_clipreid import make_dataloader
from clipreid.config import cfg
from clipreid.datasets.bases import read_image
import os.path as osp
import time
from pathlib import Path
import argparse


# 行人重识别模型类
class CLIPReIDModel:
    # ---------- 行人重识别模型初始化 --------------------------
    def __init__(self, config_dir, wight_dir):
        parser = argparse.ArgumentParser(description="ReID Baseline Training")
        if not osp.exists(wight_dir):
            raise IOError("{} does not exist".format(wight_dir))
        if not osp.exists(config_dir):
            raise IOError("{} does not exist".format(config_dir))
        else:
            parser.add_argument(
                "--config_file", default=config_dir, help="path to config file",
                type=str)
        args = parser.parse_args()
        if args.config_file != "":
            cfg.merge_from_file(args.config_file)
        cfg.freeze()

        self.cfg = cfg
        os.environ['CUDA_VISIBLE_DEVICES'] = cfg.MODEL.DEVICE_ID
        # train_loader, train_loader_normal, val_loader, num_query, num_classes, camera_num, view_num = make_dataloader(
        #     self.cfg)
        # self.target_img = val_loader
        self.model = make_model(cfg, 751, 1, 1)
        self.model.load_param(wight_dir)
        self.transform = T.Compose([
            T.Resize(self.cfg.INPUT.SIZE_TEST),
            T.ToTensor(),
            T.Normalize(mean=self.cfg.INPUT.PIXEL_MEAN, std=self.cfg.INPUT.PIXEL_STD)
        ])
        self.device = "cuda"
        if self.device:
            if torch.cuda.device_count() > 1:
                print('Using {} GPUs for inference'.format(torch.cuda.device_count()))
                self.model.model = nn.DataParallel(self.model)
        self.model.to(self.device)
        self.model.eval()
        # 待完善

    def extract_feature(self, img):
        with torch.no_grad():
            img = img.to(self.device)
            feat = self.model(img)
        return feat

    def match(self, query_feature, frame_feature):
        cosine_similarity = torch.nn.functional.cosine_similarity(query_feature, frame_feature)
        return cosine_similarity.item()


# 视频处理线程
class YolovClipReid(QThread):
    res_img = Signal(np.ndarray)  # test result signal
    status_msg = Signal(str)  # Detecting/pausing/stopping/testing complete/error reporting signal
    fps = Signal(str)  # fps
    labels = Signal(dict)  # Detected target results (number of each category)
    progress = Signal(int)  # Completeness
    class_num = Signal(int)  # Number of categories detected
    target_num = Signal(int)  # Targets detected

    def __init__(self):
        super().__init__()
        self.video_path = None
        self.yolov_model = None
        self.image_path = None
        self.reid_model = None
        self.highest_similarity = -1
        self.isPause = False
        self.cond = QWaitCondition()
        self.mutex = QMutex()

    def run(self):
        # try:
        self.status_msg.emit('加载数据中...')
        target_feat_list = []
        img = torch.stack([self.reid_model.transform(Image.open(self.image_path).convert('RGB'))], dim=0)
        # for _, (img, _, _, _, _, _) in enumerate(self.reid_model.target_img):
        target_feat = self.reid_model.extract_feature(img)
        target_feat_list.append(target_feat)

        self.cap = cv2.VideoCapture(self.video_path)
        self.status_msg.emit('匹配中...')
        # start detection
        # Detection completed
        while self.cap.isOpened() and self.isPause == False:
            ret, frame = self.cap.read()
            if not ret:
                break
            # 获取当前视频帧位置
            now_fps = self.cap.get(1)
            # 设置每 15 帧输出一次
            if (now_fps % 15 != 0):
                # 跳帧
                ret = self.cap.grab()
                continue
            milliseconds = self.cap.get(cv2.CAP_PROP_POS_MSEC)
            seconds = milliseconds // 1000
            # # 转换为RGB格式，因为OpenCV使用BGR
            # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # frame_image = QImage(frame, QImage.Format_RGB888)
            results = self.yolov_model.predict(frame, classes=[0])
            for r in results:
                indexs = r.boxes.xyxy
                print(indexs)
                for target_feat in target_feat_list:
                    for xyxy in indexs:
                        xmin = int(xyxy[0].item())
                        ymin = int(xyxy[1].item())
                        xmax = int(xyxy[2].item())
                        ymax = int(xyxy[3].item())
                        crop = torch.stack([self.reid_model.transform(
                            Image.fromarray(frame[ymin:ymax, xmin:xmax], 'RGB')
                        )], dim=0)
                        # crop = frame[ymin:ymax, xmin:xmax]
                        crop_feat = self.reid_model.extract_feature(crop)
                        current_similarity = self.reid_model.match(target_feat.cpu(), crop_feat.cpu())
                        if current_similarity > 0.85:
                            self.status_msg.emit('第' + str(seconds) + 's匹配到该行人')
                            cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (255, 0, 255), 3)
                        if current_similarity > self.highest_similarity:
                            self.highest_similarity = current_similarity
            self.res_img.emit(frame)

    # except Exception as e:
    #     pass
    #     print(e)
    #     self.status_msg.emit('%s' % e)

    # 暂停（挂起）
    def pause(self):
        # 状态改为暂停
        self.isPause = True

    # 恢复
    def resume(self):
        # 状态改为恢复
        self.isPause = False
        # 调用QWaitCondition.wake()唤醒暂停的线程
        self.cond.wakeAll()


# 主窗口类
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.yolov_model = YOLO("../yolov-models/yolov8n.pt")
        self.reid_model = CLIPReIDModel("../clipreid/configs/person/cnn_clipreid.yml",
                                        "../reid-models/Market1501_clipreid_RN50_120.pth", )
        self.video_thread = YolovClipReid()
        self.video_thread.reid_model = self.reid_model
        self.video_thread.yolov_model = self.yolov_model

        self.initUI()

    def initUI(self):
        self.setWindowTitle('行人重识别匹配')

        # 创建中心部件和布局
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # 添加图片显示标签
        self.img_label = QLabel(self)
        self.img_label.setScaledContents(True)
        layout.addWidget(self.img_label)

        # 添加视频显示标签
        self.video_label = QLabel(self)
        self.video_label.setScaledContents(True)
        layout.addWidget(self.video_label)

        # 添加状态显示标签
        self.status_bar = QLabel(self)
        self.video_label.setScaledContents(True)
        self.status_bar.setStyleSheet(u"font: 700 11pt \"Segoe UI\";\n"
                                      "color: rgba(0, 0, 0, 140);")
        layout.addWidget(self.status_bar)
        self.video_thread.status_msg.connect(lambda x: self.show_status(x))

        # 添加状态显示标签
        self.res_video = QLabel(self)
        self.res_video.setScaledContents(True)
        self.video_thread.res_img.connect(lambda x: self.updateVideoFrame(x, self.res_video))

        layout.addWidget(self.res_video)

        self.yolov_clipreid = YolovClipReid()

        # 添加控制按钮
        controls_widget = QWidget()
        controls_layout = QVBoxLayout(controls_widget)

        self.video_button = QPushButton('选择视频', self)
        self.video_button.clicked.connect(self.selectVideo)
        controls_layout.addWidget(self.video_button)

        self.image_button = QPushButton('选择图片', self)
        self.image_button.clicked.connect(self.selectImage)
        controls_layout.addWidget(self.image_button)

        self.start_button = QPushButton('开始匹配', self)
        self.start_button.clicked.connect(self.startMatching)
        self.start_button.setEnabled(False)
        controls_layout.addWidget(self.start_button)

        self.pause_button = QPushButton('暂停匹配', self)
        self.pause_button.clicked.connect(self.pauseMatching)
        self.pause_button.setEnabled(False)
        controls_layout.addWidget(self.pause_button)

        layout.addWidget(controls_widget)

        # 添加进度条
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(100)
        self.progress_bar.setValue(0)
        layout.addWidget(self.progress_bar)

    def startMatching(self):
        if self.video_thread.video_path and self.video_thread.image_path:
            self.status_bar.setText("开始匹配")
            self.video_thread.start()
            self.start_button.setEnabled(False)
            self.pause_button.setEnabled(True)

    def pauseMatching(self):
        if self.video_thread and self.video_thread.isRunning():
            self.video_thread.pause()
            self.pause_button.setText('恢复匹配')
        else:
            self.video_thread.resume()
            self.pause_button.setText('暂停匹配')

    def selectVideo(self):
        video_path, _ = QFileDialog.getOpenFileName(self, "选择视频文件", "", "Video Files (*.mp4 *.avi)")
        if video_path:
            self.video_thread.video_path = video_path
            self.start_button.setEnabled(True)
            self.video_label.setText(video_path)  # 占位图片

    def selectImage(self):
        image_path, _ = QFileDialog.getOpenFileName(self, "选择图片文件", "", "Image Files (*.jpg *.png)")
        if image_path:
            self.video_thread.image_path = image_path
            self.start_button.setEnabled(True)
            self.img_label.setPixmap(QPixmap(image_path))  # 占位图片

    def show_status(self, msg):
        self.status_bar.setText(msg)
        # if msg == 'Detection completed' or msg == '检测完成':
        #     self.save_res_button.setEnabled(True)
        #     self.save_txt_button.setEnabled(True)
        #     self.run_button.setChecked(False)
        #     self.progress_bar.setValue(0)
        #     if self.yolo_thread.isRunning():
        #         self.yolo_thread.quit()  # end process
        # elif msg == 'Detection terminated!' or msg == '检测终止':
        #     self.save_res_button.setEnabled(True)
        #     self.save_txt_button.setEnabled(True)
        #     self.run_button.setChecked(False)
        #     self.progress_bar.setValue(0)
        #     if self.yolo_thread.isRunning():
        #         self.yolo_thread.quit()  # end process
        #     self.pre_video.clear()  # clear image display
        #     self.res_video.clear()
        #     self.Class_num.setText('--')
        #     self.Target_num.setText('--')
        #     self.fps_label.setText('--')

    @staticmethod
    def updateVideoFrame(img_src, label):
        try:
            ih, iw, _ = img_src.shape
            w = label.geometry().width()
            h = label.geometry().height()
            # keep the original data ratio
            if iw / w > ih / h:
                scal = w / iw
                nw = w
                nh = int(scal * ih)
                img_src_ = cv2.resize(img_src, (nw, nh))

            else:
                scal = h / ih
                nw = int(scal * iw)
                nh = h
                img_src_ = cv2.resize(img_src, (nw, nh))

            frame = cv2.cvtColor(img_src_, cv2.COLOR_BGR2RGB)
            img = QImage(frame.data, frame.shape[1], frame.shape[0], frame.shape[2] * frame.shape[1],
                         QImage.Format_RGB888)
            label.setPixmap(QPixmap.fromImage(img))

        except Exception as e:
            print(repr(e))

    def closeEvent(self, event):
        if self.video_thread and self.video_thread.isRunning():
            self.video_thread.requestInterruption()
            self.video_thread.quit()
        event.accept()

        # 主函数


def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
