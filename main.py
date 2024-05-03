from custom_grips import CustomGrip
from ui.message_box import MessageBox
from ui.home import Ui_MainWindow
from utils.capnums import Camera
from utils.predictor import YoloPredictor
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from ui.rtsp_dialog import RtspDialog
from utils.reidentifier import YolovClipReidentifier
import json
import sys
import cv2
import os

GLOBAL_STATE = False  # max min flag
GLOBAL_TITLE_BAR = True
# 按照数据库中的字段顺序包含了属性名
FILE_FIELD_ORDER = ['ID', 'Title', 'UploadTime', 'Type', 'Description']
RECORD_FIELD_ORDER = ['ID', 'Title', 'Time', 'Type']


class MainWindow(QMainWindow, Ui_MainWindow):
    main_yolo_begin_sgl = Signal()  # The main window sends an execution signal to the yolo instance
    main_yolo_clip_begin_sgl = Signal()  # The main window sends an execution signal to the yolo instance

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # basic interface
        self.setupUi(self)
        self.setAttribute(Qt.WA_TranslucentBackground)  # rounded transparent
        self.setWindowFlags(Qt.FramelessWindowHint)  # Set window flag: hide window borders
        UIFunctions.uiDefinitions(self)
        # Show module shadows
        UIFunctions.shadow_style(self, self.Class_QF, QColor(162, 129, 247))
        UIFunctions.shadow_style(self, self.Target_QF, QColor(251, 157, 139))
        UIFunctions.shadow_style(self, self.Fps_QF, QColor(170, 128, 213))
        UIFunctions.shadow_style(self, self.Class_QF_2, QColor(162, 129, 247))
        UIFunctions.shadow_style(self, self.Target_QF_2, QColor(251, 157, 139))
        UIFunctions.shadow_style(self, self.Fps_QF_2, QColor(170, 128, 213))
        # UIFunctions.shadow_style(self, self.Model_QF, QColor(64, 186, 193))
        # contents init
        self.ReidContentBox.hide()
        self.DataManageContentBox.hide()
        self.DetectContentBox.hide()
        self.TaskRecordContentBox.hide()

        # Detect

        # read model folder
        self.pt_list = os.listdir('./yolov-models')
        self.pt_list = [file for file in self.pt_list if file.endswith('.pt')]
        self.pt_list.sort(key=lambda x: os.path.getsize('./yolov-models/' + x))  # sort by file size
        self.model_box.clear()
        self.model_box.addItems(self.pt_list)
        self.Qtimer_ModelBox = QTimer(self)  # Timer: Monitor model file changes every 2 seconds
        self.Qtimer_ModelBox.timeout.connect(self.ModelBoxRefre)
        self.Qtimer_ModelBox.start(2000)

        # Yolo-v8 thread
        self.yolo_predict = YoloPredictor()  # Create a Yolo instance
        self.select_model = self.model_box.currentText()  # default model
        self.yolo_predict.new_model_name = "./yolov-models/%s" % self.select_model
        self.yolo_thread = QThread()  # Create yolo thread
        self.yolo_predict.pre_img.connect(lambda x: self.show_image(x, self.pre_video))
        self.yolo_predict.res_img.connect(lambda x: self.show_image(x, self.res_video))
        self.yolo_predict.status_msg.connect(lambda x: self.show_status(x))
        self.yolo_predict.fps.connect(lambda x: self.fps_num.setText(x))
        # self.yolo_predict.labels.connect(self.show_labels)
        self.yolo_predict.class_num.connect(lambda x: self.class_num.setText(str(x)))
        self.yolo_predict.target_num.connect(lambda x: self.target_num.setText(str(x)))
        self.yolo_predict.progress.connect(lambda x: self.progress_bar.setValue(x))
        self.main_yolo_begin_sgl.connect(self.yolo_predict.run)
        self.yolo_predict.moveToThread(self.yolo_thread)

        # Model parameters
        self.model_box.currentTextChanged.connect(self.change_model)
        self.iou_spinbox.valueChanged.connect(lambda x: self.change_val(x, 'iou_spinbox'))  # iou box
        self.iou_slider.valueChanged.connect(lambda x: self.change_val(x, 'iou_slider'))  # iou scroll bar
        self.conf_spinbox.valueChanged.connect(lambda x: self.change_val(x, 'conf_spinbox'))  # conf box
        self.conf_slider.valueChanged.connect(lambda x: self.change_val(x, 'conf_slider'))  # conf scroll bar
        self.speed_spinbox.valueChanged.connect(lambda x: self.change_val(x, 'speed_spinbox'))  # speed box
        self.speed_slider.valueChanged.connect(lambda x: self.change_val(x, 'speed_slider'))  # speed scroll bar

        # Prompt window initialization
        self.class_num.setText('--')
        self.target_num.setText('--')
        self.fps_num.setText('--')

        # self.Model_name.setText(self.select_model)

        # Select detection source
        self.src_file_button.clicked.connect(self.open_src_file)  # select local file
        self.src_cam_button.clicked.connect(self.chose_cam)  # chose cam
        self.src_rtsp_button.clicked.connect(self.chose_rtsp)  # chose_rtsp

        # start testing button
        self.run_button.clicked.connect(self.run_or_continue)  # pause/start
        self.stop_button.clicked.connect(self.stop)  # termination

        # Other function buttons
        self.save_res_button.toggled.connect(self.is_save_res)  # save image option
        self.save_txt_button.toggled.connect(self.is_save_txt)  # Save label option

        # Reid
        # read model folder
        self.pth_list = os.listdir('./reid-models')
        self.pth_list = [file for file in self.pth_list if file.endswith('.pth')]
        self.pth_list.sort(key=lambda x: os.path.getsize('./reid-models/' + x))  # sort by file size
        self.reid_model_box.clear()
        self.reid_model_box.addItems(self.pth_list)
        self.model_box_2.clear()
        self.model_box_2.addItems(self.pt_list)
        self.Qtimer_ModelBox = QTimer(self)  # Timer: Monitor model file changes every 2 seconds
        self.Qtimer_ModelBox.timeout.connect(self.ModelBoxRefre_Reid)
        self.Qtimer_ModelBox.start(2000)

        # Yolo-v8 Clip Reid thread
        self.yolo_clip_reidentifier = YolovClipReidentifier()  # Create a Yolo instance
        self.select_model_2 = self.model_box_2.currentText()  # default model
        self.select_reid_model = self.reid_model_box.currentText()  # default model
        self.yolo_clip_reidentifier.new_model_name = "./yolov-models/%s" % self.select_model_2
        self.yolo_clip_reidentifier.new_reid_model_name = "./reid-models/%s" % self.select_reid_model
        self.yolo_clip_thread = QThread()  # Create yolo thread
        # self.yolo_clip_reidentifier.pre_img.connect(lambda x: self.show_image(x, self.pre_video_2))
        self.yolo_clip_reidentifier.res_img.connect(lambda x: self.show_image(x, self.res_video_2))
        self.yolo_clip_reidentifier.res_crop_img.connect(lambda x: self.crop_add(x, self.listWidget))
        self.yolo_clip_reidentifier.status_msg.connect(lambda x: self.show_reid_status(x))
        self.yolo_clip_reidentifier.fps.connect(lambda x: self.fps_num_2.setText(x))
        # self.yolo_predict.labels.connect(self.show_labels)
        self.yolo_clip_reidentifier.class_num.connect(lambda x: self.class_num_2.setText(str(x)))
        self.yolo_clip_reidentifier.target_num.connect(lambda x: self.target_num_2.setText(str(x)))
        self.yolo_clip_reidentifier.progress.connect(lambda x: self.progress_bar_2.setValue(x))
        self.main_yolo_clip_begin_sgl.connect(self.yolo_clip_reidentifier.run)
        self.yolo_clip_reidentifier.moveToThread(self.yolo_clip_thread)

        # Model parameters
        self.model_box_2.currentTextChanged.connect(self.change_yolo_model)
        self.reid_model_box.currentTextChanged.connect(self.change_reid_model)
        self.iou_spinbox_2.valueChanged.connect(lambda x: self.change_reid_val(x, 'iou_spinbox'))  # iou box
        self.iou_slider_2.valueChanged.connect(lambda x: self.change_reid_val(x, 'iou_slider'))  # iou scroll bar
        self.conf_spinbox_2.valueChanged.connect(lambda x: self.change_reid_val(x, 'conf_spinbox'))  # conf box
        self.conf_slider_2.valueChanged.connect(lambda x: self.change_reid_val(x, 'conf_slider'))  # conf scroll bar
        self.speed_spinbox_2.valueChanged.connect(lambda x: self.change_reid_val(x, 'speed_spinbox'))  # speed box
        self.speed_slider_2.valueChanged.connect(lambda x: self.change_reid_val(x, 'speed_slider'))  # speed scroll bar

        # Prompt window initialization
        self.class_num_2.setText('--')
        self.target_num_2.setText('--')
        self.fps_num_2.setText('--')

        self.target_select_button.clicked.connect(self.select_reid_target_image)  # select local file

        # Select reid source
        self.src_file_button_2.clicked.connect(self.open_src_reid_file)  # select local file
        self.src_cam_button_2.clicked.connect(self.chose_reid_cam)  # chose cam
        self.src_rtsp_button_2.clicked.connect(self.chose_reid_rtsp)  # chose_rtsp

        # start testing button
        self.run_button_2.clicked.connect(self.run_or_continue_reid)  # pause/start
        self.stop_button_2.clicked.connect(self.reid_stop)  # termination

        # Other function buttons
        self.save_res_button_2.toggled.connect(self.is_save_res_reid)  # save image option
        self.save_txt_button_2.toggled.connect(self.is_save_txt_reid)  # Save label option

        # initialization
        self.load_config()
        self.table_widget.load_data(1, self.page_box, self.total_page_num, FILE_FIELD_ORDER, self.add_button,
                                    self.search_button, self.type_box, self.line_edit)
        self.table_widget_2.load_data(2, self.page_box_2, self.total_page_num_2, RECORD_FIELD_ORDER, QPushButton(),
                                      self.search_button_2, self.type_box_2, self.line_edit_2)
        # h_layout_1 = QHBoxLayout()
        # h_layout_1.addWidget(self.table_widget.page_spinbox)
        # h_layout_1.addWidget(self.table_widget.total_label)
        # self.verticalLayout_44.addLayout(h_layout_1)

        # self.table_widget_2.load_data(initial_data)
        # h_layout_2 = QHBoxLayout()
        # h_layout_2.addWidget(self.table_widget_2.page_spinbox)
        # h_layout_2.addWidget(self.table_widget_2.total_label)
        # self.verticalLayout_45.addLayout(h_layout_2)

        self.ToggleBotton.clicked.connect(lambda: UIFunctions.toggle_menu(self, True))  # left navigation button
        self.HomeBotton.clicked.connect(lambda: UIFunctions.open_page(self, self.HomePage, True))
        self.DetectButton.clicked.connect(lambda: UIFunctions.open_page(self, self.DetectContentBox, True))
        self.DataManageButton.clicked.connect(lambda: UIFunctions.open_page(self, self.DataManageContentBox, True))
        self.ReidButton.clicked.connect(lambda: UIFunctions.open_page(self, self.ReidContentBox, True))
        self.TaskRecordButton.clicked.connect(lambda: UIFunctions.open_page(self, self.TaskRecordContentBox, True))
        self.detect_set_button.clicked.connect(lambda: UIFunctions.setting_box(self, self.prm_page, True))
        self.reid_set_button.clicked.connect(lambda: UIFunctions.setting_box(self, self.prm_page_2, True))

    # The main window displays the original image and detection results
    def show_image(self, img_src, label):
        try:
            ih, iw = img_src.shape[:2]
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

    # Control start/pause
    def run_or_continue(self):
        if self.yolo_predict.source == '':
            self.show_status('Please select a video source before starting detection...')
            self.run_button.setChecked(False)
        else:
            self.yolo_predict.stop_dtc = False
            if self.run_button.isChecked():
                self.run_button.setChecked(True)  # start button
                self.save_txt_button.setEnabled(False)  # It is forbidden to check and save after starting the detection
                self.save_res_button.setEnabled(False)
                self.show_status('Detecting...')
                self.yolo_predict.continue_dtc = True  # Control whether Yolo is paused
                if not self.yolo_thread.isRunning():
                    self.yolo_thread.start()
                    self.main_yolo_begin_sgl.emit()

            else:
                self.yolo_predict.continue_dtc = False
                self.show_status("Pause...")
                self.run_button.setChecked(False)  # start button

    # Control start/pause
    def run_or_continue_reid(self):
        if self.yolo_clip_reidentifier.source == '':
            self.show_reid_status('Please select a video source before starting reidentification...')
            self.run_button_2.setChecked(False)
        if self.yolo_clip_reidentifier.image_path == '':
            self.show_reid_status('Please select a target img before starting reidentification...')
            self.run_button_2.setChecked(False)
        if self.yolo_clip_reidentifier.image_path != '' and self.yolo_clip_reidentifier.source != '':
            self.yolo_clip_reidentifier.stop_dtc = False
            if self.run_button_2.isChecked():
                self.run_button_2.setChecked(True)  # start button
                self.save_txt_button_2.setEnabled(
                    False)  # It is forbidden to check and save after starting the detection
                self.save_res_button_2.setEnabled(False)
                self.show_reid_status('Detecting...')
                self.yolo_clip_reidentifier.continue_dtc = True  # Control whether Yolo is paused
                if not self.yolo_clip_thread.isRunning():
                    self.yolo_clip_thread.start()
                    self.main_yolo_clip_begin_sgl.emit()

            else:
                self.yolo_clip_reidentifier.continue_dtc = False
                self.show_reid_status("Pause...")
                self.run_button_2.setChecked(False)  # start button

    # bottom status bar information
    def show_status(self, msg):
        self.status_bar.setText(msg)
        if 'Detection completed' in msg:
            self.save_res_button.setEnabled(True)
            self.save_txt_button.setEnabled(True)
            self.run_button.setChecked(False)
            self.progress_bar.setValue(0)
            if self.yolo_thread.isRunning():
                self.yolo_thread.quit()  # end process
        elif 'Detection terminated' in msg:
            self.save_res_button.setEnabled(True)
            self.save_txt_button.setEnabled(True)
            self.run_button.setChecked(False)
            self.progress_bar.setValue(0)
            if self.yolo_thread.isRunning():
                self.yolo_thread.quit()  # end process
            self.pre_video.clear()  # clear image display
            self.res_video.clear()
            self.class_num.setText('--')
            self.target_num.setText('--')
            self.fps_num.setText('--')

    def show_reid_status(self, msg):
        self.status_bar_2.setText(msg)
        if 'Re-identification completed' in msg:
            self.save_res_button_2.setEnabled(True)
            self.save_txt_button_2.setEnabled(True)
            self.run_button_2.setChecked(False)
            self.progress_bar_2.setValue(0)
            if self.yolo_clip_thread.isRunning():
                self.yolo_clip_thread.quit()  # end process
        elif 'Re-identification terminated' in msg:
            self.save_res_button_2.setEnabled(True)
            self.save_txt_button_2.setEnabled(True)
            self.run_button_2.setChecked(False)
            self.progress_bar_2.setValue(0)
            if self.yolo_clip_thread.isRunning():
                self.yolo_clip_thread.quit()  # end process
            self.pre_video_2.clear()  # clear image display
            self.res_video_2.clear()
            self.class_num_2.setText('--')
            self.target_num_2.setText('--')
            self.fps_num_2.setText('--')

    # select local file
    def open_src_file(self):
        config_file = 'config/fold.json'
        config = json.load(open(config_file, 'r', encoding='utf-8'))
        open_fold = config['open_fold']
        if not os.path.exists(open_fold):
            open_fold = os.getcwd()
        name, _ = QFileDialog.getOpenFileName(self, 'Video/image', open_fold,
                                              "Pic File(*.mp4 *.mkv *.avi *.flv *.jpg *.png)")
        if name:
            self.yolo_predict.source = name
            self.show_status('Load File：{}'.format(os.path.basename(name)))
            config['open_fold'] = os.path.dirname(name)
            config_json = json.dumps(config, ensure_ascii=False, indent=2)
            with open(config_file, 'w', encoding='utf-8') as f:
                f.write(config_json)
            self.stop()

    # select local file
    def open_src_reid_file(self):
        config_file = 'config/fold.json'
        config = json.load(open(config_file, 'r', encoding='utf-8'))
        open_fold = config['open_fold']
        if not os.path.exists(open_fold):
            open_fold = os.getcwd()
        name, _ = QFileDialog.getOpenFileName(self, 'Video/image', open_fold,
                                              "Pic File(*.mp4 *.mkv *.avi *.flv *.jpg *.png)")
        if name:
            self.yolo_clip_reidentifier.source = name
            self.show_reid_status('Load File：{}'.format(os.path.basename(name)))
            config['open_fold'] = os.path.dirname(name)
            config_json = json.dumps(config, ensure_ascii=False, indent=2)
            with open(config_file, 'w', encoding='utf-8') as f:
                f.write(config_json)
            self.reid_stop()

    # Select camera source
    def chose_cam(self):
        try:
            self.stop()
            MessageBox(
                self.close_button, title='tips', text='loading camera...', time=2000, auto=True).exec()
            # get the number of local cameras
            _, cams = Camera().get_cam_num()
            popMenu = QMenu()
            popMenu.setFixedWidth(self.src_cam_button.width())
            popMenu.setStyleSheet('''
                                            QMenu {
                                            font-size: 16px;
                                            font-family: "Microsoft YaHei UI";
                                            font-weight: light;
                                            color:white;
                                            padding-left: 5px;
                                            padding-right: 5px;
                                            padding-top: 4px;
                                            padding-bottom: 4px;
                                            border-style: solid;
                                            border-width: 0px;
                                            border-color: rgba(255, 255, 255, 255);
                                            border-radius: 3px;
                                            background-color: rgba(200, 200, 200,50);}
                                            ''')

            for cam in cams:
                exec("action_%s = QAction('%s')" % (cam, cam))
                exec("popMenu.addAction(action_%s)" % cam)

            x = self.src_cam_button.mapToGlobal(self.src_cam_button.pos()).x()
            y = self.src_cam_button.mapToGlobal(self.src_cam_button.pos()).y()
            y = y + self.src_cam_button.frameGeometry().height()
            pos = QPoint(x, y)
            action = popMenu.exec(pos)
            if action:
                self.yolo_predict.source = action.text()
                self.show_status('Loading camera：{}'.format(action.text()))

        except Exception as e:
            self.show_status('%s' % e)

    def chose_reid_cam(self):
        try:
            self.reid_stop()
            MessageBox(
                self.close_button, title='tips', text='loading camera...', time=2000, auto=True).exec()
            # get the number of local cameras
            _, cams = Camera().get_cam_num()
            popMenu = QMenu()
            popMenu.setFixedWidth(self.src_cam_button_2.width())
            popMenu.setStyleSheet('''
                                            QMenu {
                                            font-size: 16px;
                                            font-family: "Microsoft YaHei UI";
                                            font-weight: light;
                                            color:white;
                                            padding-left: 5px;
                                            padding-right: 5px;
                                            padding-top: 4px;
                                            padding-bottom: 4px;
                                            border-style: solid;
                                            border-width: 0px;
                                            border-color: rgba(255, 255, 255, 255);
                                            border-radius: 3px;
                                            background-color: rgba(200, 200, 200,50);}
                                            ''')

            for cam in cams:
                exec("action_%s = QAction('%s')" % (cam, cam))
                exec("popMenu.addAction(action_%s)" % cam)

            x = self.src_cam_button_2.mapToGlobal(self.src_cam_button_2.pos()).x()
            y = self.src_cam_button_2.mapToGlobal(self.src_cam_button_2.pos()).y()
            y = y + self.src_cam_button_2.frameGeometry().height()
            pos = QPoint(x, y)
            action = popMenu.exec(pos)
            if action:
                self.yolo_clip_reidentifier.source = action.text()
                self.show_reid_status('Loading camera：{}'.format(action.text()))

        except Exception as e:
            self.show_reid_status('%s' % e)

    # select network source
    def chose_rtsp(self):
        self.rtsp_window = RtspDialog()
        config_file = 'config/ip.json'
        if not os.path.exists(config_file):
            ip = "rtmp://mobliestream.c3tv.com:554/live/goodtv.sdp"
            new_config = {"ip": ip}
            new_json = json.dumps(new_config, ensure_ascii=False, indent=2)
            with open(config_file, 'w', encoding='utf-8') as f:
                f.write(new_json)
        else:
            config = json.load(open(config_file, 'r', encoding='utf-8'))
            ip = config['ip']
        self.rtsp_window.rtspEdit.setText(ip)
        self.rtsp_window.show()
        self.rtsp_window.rtspButton.clicked.connect(lambda: self.load_rtsp(self.rtsp_window.rtspEdit.text()))

    # select network source
    def chose_reid_rtsp(self):
        self.rtsp_window = RtspDialog()
        config_file = 'config/reid_ip.json'
        if not os.path.exists(config_file):
            ip = "rtmp://mobliestream.c3tv.com:554/live/goodtv.sdp"
            new_config = {"ip": ip}
            new_json = json.dumps(new_config, ensure_ascii=False, indent=2)
            with open(config_file, 'w', encoding='utf-8') as f:
                f.write(new_json)
        else:
            config = json.load(open(config_file, 'r', encoding='utf-8'))
            ip = config['ip']
        self.rtsp_window.rtspEdit.setText(ip)
        self.rtsp_window.show()
        self.rtsp_window.rtspButton.clicked.connect(lambda: self.load_reid_rtsp(self.rtsp_window.rtspEdit.text()))

    # select network source
    def select_reid_target_image(self):
        config_file = 'config/fold.json'
        config = json.load(open(config_file, 'r', encoding='utf-8'))
        open_fold = config['open_fold']
        if not os.path.exists(open_fold):
            open_fold = os.getcwd()
        name, _ = QFileDialog.getOpenFileName(self, 'Select target image', open_fold,
                                              "Pic File(*.jpg *.png)")
        if name:
            self.yolo_clip_reidentifier.image_path = name
            self.show_reid_status('Select target image：{}'.format(os.path.basename(name)))
            config['open_fold'] = os.path.dirname(name)
            config_json = json.dumps(config, ensure_ascii=False, indent=2)
            with open(config_file, 'w', encoding='utf-8') as f:
                f.write(config_json)
            self.reid_stop()
            # self.pre_video_2.setPixmap(QPixmap(name))
            # 使用QPixmap加载图片
            pixmap = QPixmap(name)
            # 获取QLabel的大小
            label_size = self.pre_video_2.size()
            # 如果QLabel有有效的大小（即不是初始大小），则缩放图片
            if label_size.isValid():
                # 保持图片的宽高比，同时调整宽度使图片高度与QLabel高度相同
                scaled_pixmap = pixmap.scaled(
                    label_size.width(), label_size.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation
                )
                self.pre_video_2.setPixmap(scaled_pixmap)
            else:
                self.pre_video_2.setPixmap(pixmap)

    # load network sources
    def load_rtsp(self, ip):
        try:
            self.stop()
            MessageBox(
                self.close_button, title='提示', text='加载 rtsp...', time=1000, auto=True).exec()
            self.yolo_predict.source = ip
            new_config = {"ip": ip}
            new_json = json.dumps(new_config, ensure_ascii=False, indent=2)
            with open('config/ip.json', 'w', encoding='utf-8') as f:
                f.write(new_json)
            self.show_status('Loading rtsp：{}'.format(ip))
            self.rtsp_window.close()
        except Exception as e:
            self.show_status('%s' % e)

    # load network sources
    def load_reid_rtsp(self, ip):
        try:
            self.reid_stop()
            MessageBox(
                self.close_button, title='提示', text='加载 rtsp...', time=1000, auto=True).exec()
            self.yolo_clip_reidentifier.source = ip
            new_config = {"ip": ip}
            new_json = json.dumps(new_config, ensure_ascii=False, indent=2)
            with open('config/ip.json', 'w', encoding='utf-8') as f:
                f.write(new_json)
            self.show_reid_status('Loading rtsp：{}'.format(ip))
            self.rtsp_window.close()
        except Exception as e:
            self.show_reid_status('%s' % e)

    # Save test result button--picture/video
    def is_save_res(self):
        if self.save_res_button.checkState() == Qt.CheckState.Unchecked:
            self.show_status('NOTE: Run image results are not saved.')
            self.yolo_predict.save_res = False
        elif self.save_res_button.checkState() == Qt.CheckState.Checked:
            self.show_status('NOTE: Run image results will be saved.')
            self.yolo_predict.save_res = True

    # Save test result button--picture/video
    def is_save_res_reid(self):
        if self.save_res_button_2.checkState() == Qt.CheckState.Unchecked:
            self.show_reid_status('NOTE: Run image results are not saved.')
            self.yolo_clip_reidentifier.save_res = False
        elif self.save_res_button_2.checkState() == Qt.CheckState.Checked:
            self.show_reid_status('NOTE: Run image results will be saved.')
            self.yolo_clip_reidentifier.save_res = True

    # Save test result button -- label (txt)
    def is_save_txt(self):
        if self.save_txt_button.checkState() == Qt.CheckState.Unchecked:
            self.show_status('NOTE: Labels results are not saved.')
            self.yolo_predict.save_txt = False
        elif self.save_txt_button.checkState() == Qt.CheckState.Checked:
            self.show_status('NOTE: Labels results will be saved.')
            self.yolo_predict.save_txt = True

    # Save test result button -- label (txt)
    def is_save_txt_reid(self):
        if self.save_txt_button_2.checkState() == Qt.CheckState.Unchecked:
            self.show_reid_status('NOTE: Labels results are not saved.')
            self.yolo_clip_reidentifier.save_txt = False
        elif self.save_txt_button_2.checkState() == Qt.CheckState.Checked:
            self.show_reid_status('NOTE: Labels results will be saved.')
            self.yolo_clip_reidentifier.save_txt = True

    # Configuration initialization  ~~~wait to change~~~
    def load_config(self):
        config_file = 'config/setting.json'
        if not os.path.exists(config_file):
            iou = 0.26
            conf = 0.33
            rate = 10
            save_res = 0
            save_txt = 0
            new_config = {"iou": iou,
                          "conf": conf,
                          "rate": rate,
                          "save_res": save_res,
                          "save_txt": save_txt
                          }
            new_json = json.dumps(new_config, ensure_ascii=False, indent=2)
            with open(config_file, 'w', encoding='utf-8') as f:
                f.write(new_json)
        else:
            config = json.load(open(config_file, 'r', encoding='utf-8'))
            if len(config) != 5:
                iou = 0.26
                conf = 0.33
                rate = 10
                save_res = 0
                save_txt = 0
            else:
                iou = config['iou']
                conf = config['conf']
                rate = config['rate']
                save_res = config['save_res']
                save_txt = config['save_txt']
        self.yolo_predict.iou_thres = iou
        self.iou_spinbox.setValue(iou)
        self.yolo_predict.conf_thres = conf
        self.conf_spinbox.setValue(conf)
        self.yolo_predict.speed_thres = rate
        self.speed_spinbox.setValue(rate)
        self.save_res_button.setCheckState(Qt.CheckState(save_res))
        self.yolo_predict.save_res = (False if save_res == 0 else True)
        self.save_txt_button.setCheckState(Qt.CheckState(save_txt))
        self.yolo_predict.save_txt = (False if save_txt == 0 else True)
        self.run_button.setChecked(False)
        self.show_status("Welcome~")

    # Configuration initialization  ~~~wait to change~~~
    def load_reid_config(self):
        config_file = 'config/reid_setting.json'
        if not os.path.exists(config_file):
            iou = 0.26
            conf = 0.33
            rate = 10
            save_res = 0
            save_txt = 0
            new_config = {"iou": iou,
                          "conf": conf,
                          "rate": rate,
                          "save_res": save_res,
                          "save_txt": save_txt
                          }
            new_json = json.dumps(new_config, ensure_ascii=False, indent=2)
            with open(config_file, 'w', encoding='utf-8') as f:
                f.write(new_json)
        else:
            config = json.load(open(config_file, 'r', encoding='utf-8'))
            if len(config) != 5:
                iou = 0.26
                conf = 0.33
                rate = 10
                save_res = 0
                save_txt = 0
            else:
                iou = config['iou']
                conf = config['conf']
                rate = config['rate']
                save_res = config['save_res']
                save_txt = config['save_txt']
        self.yolo_clip_reidentifier.iou_thres = iou
        self.iou_spinbox_2.setValue(iou)
        self.yolo_clip_reidentifier.conf_thres = conf
        self.conf_spinbox_2.setValue(conf)
        self.yolo_clip_reidentifier.speed_thres = rate
        self.speed_spinbox_2.setValue(rate)
        self.save_res_button_2.setCheckState(Qt.CheckState(save_res))
        self.yolo_clip_reidentifier.save_res = (False if save_res == 0 else True)
        self.save_txt_button_2.setCheckState(Qt.CheckState(save_txt))
        self.yolo_clip_reidentifier.save_txt = (False if save_txt == 0 else True)
        self.run_button_2.setChecked(False)
        self.show_reid_status("Welcome~")

    # Terminate button and associated state
    def stop(self):
        if self.yolo_thread.isRunning():
            self.yolo_thread.quit()  # end thread
        self.yolo_predict.stop_dtc = True
        self.run_button.setChecked(False)  # start key recovery
        self.save_res_button.setEnabled(True)  # Ability to use the save button
        self.save_txt_button.setEnabled(True)  # Ability to use the save button
        # self.pre_video.clear()  # clear image display
        # self.res_video.clear()  # clear image display
        self.progress_bar.setValue(0)
        self.class_num.setText('--')
        self.target_num.setText('--')
        self.fps_num.setText('--')

    def reid_stop(self):
        if self.yolo_clip_thread.isRunning():
            self.yolo_clip_thread.quit()  # end thread
        self.yolo_clip_reidentifier.stop_dtc = True
        self.run_button_2.setChecked(False)  # start key recovery
        self.save_res_button_2.setEnabled(True)  # Ability to use the save button
        self.save_txt_button_2.setEnabled(True)  # Ability to use the save button
        # self.pre_video.clear()  # clear image display
        # self.res_video.clear()  # clear image display
        self.progress_bar_2.setValue(0)
        self.class_num_2.setText('--')
        self.target_num_2.setText('--')
        self.fps_num_2.setText('--')

    # Change detection parameters
    def change_val(self, x, flag):
        if flag == 'iou_spinbox':
            self.iou_slider.setValue(int(x * 100))  # The box value changes, changing the slider
        elif flag == 'iou_slider':
            self.iou_spinbox.setValue(x / 100)  # The slider value changes, changing the box
            self.show_status('IOU Threshold: %s' % str(x / 100))
            self.yolo_predict.iou_thres = x / 100
        elif flag == 'conf_spinbox':
            self.conf_slider.setValue(int(x * 100))
        elif flag == 'conf_slider':
            self.conf_spinbox.setValue(x / 100)
            self.show_status('Conf Threshold: %s' % str(x / 100))
            self.yolo_predict.conf_thres = x / 100
        elif flag == 'speed_spinbox':
            self.speed_slider.setValue(x)
        elif flag == 'speed_slider':
            self.speed_spinbox.setValue(x)
            self.show_status('Delay: %s ms' % str(x))
            self.yolo_predict.speed_thres = x  # ms

    def change_reid_val(self, x, flag):
        if flag == 'iou_spinbox':
            self.iou_slider_2.setValue(int(x * 100))  # The box value changes, changing the slider
        elif flag == 'iou_slider':
            self.iou_spinbox_2.setValue(x / 100)  # The slider value changes, changing the box
            self.show_reid_status('IOU Threshold: %s' % str(x / 100))
            self.yolo_clip_reidentifier.iou_thres = x / 100
        elif flag == 'conf_spinbox':
            self.conf_slider_2.setValue(int(x * 100))
        elif flag == 'conf_slider':
            self.conf_spinbox_2.setValue(x / 100)
            self.show_reid_status('Conf Threshold: %s' % str(x / 100))
            self.yolo_clip_reidentifier.conf_thres = x / 100
        elif flag == 'speed_spinbox':
            self.speed_slider_2.setValue(x)
        elif flag == 'speed_slider':
            self.speed_spinbox_2.setValue(x)
            self.show_reid_status('Delay: %s ms' % str(x))
            self.yolo_clip_reidentifier.speed_thres = x  # ms

    # change model
    def change_model(self, x):
        self.select_model = self.model_box.currentText()
        self.yolo_predict.new_model_name = "./yolov-models/%s" % self.select_model
        self.show_status('Change Model：%s' % self.select_model)
        # self.Model_name.setText(self.select_model)

    def change_yolo_model(self, x):
        self.select_model_2 = self.model_box_2.currentText()
        self.yolo_clip_reidentifier.new_model_name = "./yolov-models/%s" % self.select_model_2
        self.show_reid_status('Change YOLOv Model：%s' % self.select_model_2)

    def change_reid_model(self, x):
        self.select_reid_model = self.reid_model_box.currentText()
        self.yolo_clip_reidentifier.new_reid_model_name = "./reid-models/%s" % self.select_reid_model
        self.show_reid_status('Change Reid Model：%s' % self.select_reid_model)
        # self.Model_name.setText(self.select_model)

    # label result
    # def show_labels(self, labels_dic):
    #     try:
    #         self.result_label.clear()
    #         labels_dic = sorted(labels_dic.items(), key=lambda x: x[1], reverse=True)
    #         labels_dic = [i for i in labels_dic if i[1]>0]
    #         result = [' '+str(i[0]) + '：' + str(i[1]) for i in labels_dic]
    #         self.result_label.addItems(result)
    #     except Exception as e:
    #         self.show_status(e)

    # Cycle monitoring model file changes
    def ModelBoxRefre(self):
        pt_list = os.listdir('./yolov-models')
        pt_list = [file for file in pt_list if file.endswith('.pt')]
        pt_list.sort(key=lambda x: os.path.getsize('./yolov-models/' + x))
        # It must be sorted before comparing, otherwise the list will be refreshed all the time
        if pt_list != self.pt_list:
            self.pt_list = pt_list
            self.model_box.clear()
            self.model_box.addItems(self.pt_list)

    def ModelBoxRefre_Reid(self):
        pt_list = os.listdir('./yolov-models')
        pt_list = [file for file in pt_list if file.endswith('.pt')]
        pt_list.sort(key=lambda x: os.path.getsize('./yolov-models/' + x))
        # It must be sorted before comparing, otherwise the list will be refreshed all the time
        if pt_list != self.pt_list:
            self.pt_list = pt_list
            self.model_box_2.clear()
            self.model_box_2.addItems(self.pt_list)

        pth_list = os.listdir('./reid-models')
        pth_list = [file for file in pth_list if file.endswith('.pth')]
        pth_list.sort(key=lambda x: os.path.getsize('./reid-models/' + x))
        # It must be sorted before comparing, otherwise the list will be refreshed all the time
        if pth_list != self.pth_list:
            self.pt_list = pth_list
            self.reid_model_box.clear()
            self.reid_model_box.addItems(self.pth_list)

    # Get the mouse position (used to hold down the title bar and drag the window)
    def mousePressEvent(self, event):
        p = event.globalPosition()
        globalPos = p.toPoint()
        self.dragPos = globalPos

    # Optimize the adjustment when dragging the bottom and right edges of the window size
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # Exit Exit thread, save settings
    def closeEvent(self, event):
        config_file = 'config/setting.json'
        config = dict()
        config['iou'] = self.iou_spinbox.value()
        config['conf'] = self.conf_spinbox.value()
        config['rate'] = self.speed_spinbox.value()
        config['save_res'] = (0 if self.save_res_button.checkState() == Qt.Unchecked else 2)
        config['save_txt'] = (0 if self.save_txt_button.checkState() == Qt.Unchecked else 2)
        config_json = json.dumps(config, ensure_ascii=False, indent=2)
        with open(config_file, 'w', encoding='utf-8') as f:
            f.write(config_json)

        reid_config_file = 'config/reid_setting.json'
        config = dict()
        config['iou'] = self.iou_spinbox_2.value()
        config['conf'] = self.conf_spinbox_2.value()
        config['rate'] = self.speed_spinbox_2.value()
        config['save_res'] = (0 if self.save_res_button_2.checkState() == Qt.Unchecked else 2)
        config['save_txt'] = (0 if self.save_txt_button_2.checkState() == Qt.Unchecked else 2)
        config_json = json.dumps(config, ensure_ascii=False, indent=2)
        with open(config_file, 'w', encoding='utf-8') as f:
            f.write(config_json)

        # Exit the process before closing
        if self.yolo_thread.isRunning() or self.yolo_clip_thread.isRunning():
            MessageBox(
                self.close_button, title='Note', text='Exiting, please wait...', time=3000, auto=True).exec()
        if self.yolo_thread.isRunning():
            self.yolo_predict.stop_dtc = True
            self.yolo_thread.quit()
        if self.yolo_clip_thread.isRunning():
            self.yolo_clip_reidentifier.stop_dtc = True
            self.yolo_clip_thread.quit()
        sys.exit(0)

    def crop_add(self, crop_img, View):
        frame = cv2.cvtColor(crop_img, cv2.COLOR_BGR2RGB)
        img = QImage(frame.data, crop_img.shape[1], frame.shape[0], frame.shape[2] * frame.shape[1],
                     QImage.Format_RGB888)
        # 创建 QListWidgetItem
        item = QListWidgetItem()
        # 设置图片
        img = item.setIcon(QPixmap.fromImage(img))
        # 设置文本
        item.setText(self.status_bar_2.text())
        # 将项添加到 QListWidget
        View.addItem(item)


class UIFunctions(MainWindow):
    # Expand left menu
    def toggle_menu(self, enable):
        if enable:
            standard = 68
            maxExtend = 180
            width = self.LeftMenuBg.width()

            if width == 68:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # animation
            self.animation = QPropertyAnimation(self.LeftMenuBg, b"minimumWidth")
            self.animation.setDuration(500)  # ms
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuint)
            self.animation.start()

    # Open Detection Page
    def open_page(self, show_page, enable):
        if enable:
            if show_page.height() == 0:
                if self.HomePage.height() != 0:
                    self.HomePage.hide()
                    self.HomePage.setMaximumSize(0, 0)
                if self.DetectContentBox.height() != 0:
                    self.DetectContentBox.hide()
                    self.DetectContentBox.setMaximumSize(0, 0)
                if self.ReidContentBox.height() != 0:
                    self.ReidContentBox.hide()
                    self.ReidContentBox.setMaximumSize(0, 0)
                if self.DataManageContentBox.height() != 0:
                    self.DataManageContentBox.hide()
                    self.DataManageContentBox.setMaximumSize(0, 0)
                if self.TaskRecordContentBox.height() != 0:
                    self.TaskRecordContentBox.hide()
                    self.TaskRecordContentBox.setMaximumSize(0, 0)

            show_page.show()
            show_page.setMaximumSize(16777215, 16777215)

    # Expand the settings menu on the right
    def setting_box(self, set_box, enable):
        if enable:
            # GET WIDTH
            widthRightBox = set_box.width()  # right set column width
            # widthLeftBox = self.LeftMenuBg.width()  # left column length
            maxExtend = 220
            standard = 0

            # SET MAX WIDTH
            if widthRightBox == 0:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION LEFT BOX
            # self.left_box = QPropertyAnimation(self.LeftMenuBg, b"minimumWidth")
            # self.left_box.setDuration(500)
            # self.left_box.setStartValue(widthLeftBox)
            # self.left_box.setEndValue(68)
            # self.left_box.setEasingCurve(QEasingCurve.InOutQuart)

            # ANIMATION RIGHT BOX
            self.right_box = QPropertyAnimation(set_box, b"minimumWidth")
            self.right_box.setDuration(500)
            self.right_box.setStartValue(widthRightBox)
            self.right_box.setEndValue(widthExtended)
            self.right_box.setEasingCurve(QEasingCurve.InOutQuart)

            # GROUP ANIMATION
            self.group = QParallelAnimationGroup()
            # self.group.addAnimation(self.left_box)
            self.group.addAnimation(self.right_box)
            self.group.start()

    # maximize window
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == False:
            GLOBAL_STATE = True
            self.showMaximized()  # maximize
            # self.Main_QW.setContentsMargins(0, 0, 0, 0)   # appMargins = Main_QW
            self.max_sf.setToolTip("Restore")
            self.frame_size_grip.hide()  # Hide the interface size adjustment button
            self.left_grip.hide()  # Up, down, left, and right adjustments are prohibited
            self.right_grip.hide()
            self.top_grip.hide()
            self.bottom_grip.hide()
        else:
            GLOBAL_STATE = False
            self.showNormal()  # minimize
            self.resize(self.width() + 1, self.height() + 1)
            # self.Main_QW.setContentsMargins(10, 10, 10, 10)
            self.max_sf.setToolTip("Maximize")
            self.frame_size_grip.show()
            self.left_grip.show()
            self.right_grip.show()
            self.top_grip.show()
            self.bottom_grip.show()

    # window control
    def uiDefinitions(self):
        # Double-click the title bar to maximize
        def dobleClickMaximizeRestore(event):
            if event.type() == QEvent.MouseButtonDblClick:
                QTimer.singleShot(250, lambda: UIFunctions.maximize_restore(self))

        self.top.mouseDoubleClickEvent = dobleClickMaximizeRestore

        # MOVE WINDOW / MAXIMIZE / RESTORE
        def moveWindow(event):
            if GLOBAL_STATE:  # IF MAXIMIZED CHANGE TO NORMAL
                UIFunctions.maximize_restore(self)
            if event.buttons() == Qt.LeftButton:  # MOVE
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()

        self.top.mouseMoveEvent = moveWindow
        # CUSTOM GRIPS
        self.left_grip = CustomGrip(self, Qt.LeftEdge, True)
        self.right_grip = CustomGrip(self, Qt.RightEdge, True)
        self.top_grip = CustomGrip(self, Qt.TopEdge, True)
        self.bottom_grip = CustomGrip(self, Qt.BottomEdge, True)

        # MINIMIZE
        self.min_sf.clicked.connect(lambda: self.showMinimized())
        # MAXIMIZE/RESTORE
        self.max_sf.clicked.connect(lambda: UIFunctions.maximize_restore(self))
        # CLOSE APPLICATION
        self.close_button.clicked.connect(self.close)

    # Control the stretching of the four sides of the window
    def resize_grips(self):
        self.left_grip.setGeometry(0, 10, 10, self.height())
        self.right_grip.setGeometry(self.width() - 10, 10, 10, self.height())
        self.top_grip.setGeometry(0, 0, self.width(), 10)
        self.bottom_grip.setGeometry(0, self.height() - 10, self.width(), 10)

    # Show module to add shadow
    def shadow_style(self, widget, Color):
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setOffset(8, 8)  # offset
        shadow.setBlurRadius(38)  # shadow radius
        shadow.setColor(Color)  # shadow color
        widget.setGraphicsEffect(shadow)


# class DBFunctions:
#     def add(self):
#         pass
#
#     def get_all_file_data():
#         file_data_list = file_dao.get_all_file_data()
#         return file_data_list


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Home = MainWindow()
    Home.show()
    sys.exit(app.exec())
