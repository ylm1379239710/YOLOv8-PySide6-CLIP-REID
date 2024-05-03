import os
from datetime import datetime

from PIL import Image
from ultralytics.yolo.engine.predictor import BasePredictor

from dao import record_dao
from entity.record_model import Record
from utils.build import load_inference_source
from ultralytics.yolo.data.augment import classify_transforms
from ultralytics.yolo.engine.predictor import BasePredictor
from ultralytics.yolo.engine.results import Results
from ultralytics.yolo.utils import DEFAULT_CFG, LOGGER, SETTINGS, callbacks, ops
from ultralytics.yolo.utils.plotting import Annotator, colors, save_one_box
from ultralytics.yolo.utils.torch_utils import smart_inference_mode
from ultralytics.yolo.utils.files import increment_path
from ultralytics.yolo.utils.checks import check_imshow, check_imgsz
from ultralytics.yolo.cfg import get_cfg
from PySide6.QtCore import Signal, QObject
from collections import defaultdict
from pathlib import Path
import numpy as np
import time
import torch
import cv2

from utils.reid_model import CLIPReIDModel


class YolovClipReidentifier(BasePredictor, QObject):
    pre_img = Signal(np.ndarray)  # raw image signal
    res_img = Signal(np.ndarray)  # test result signal
    status_msg = Signal(str)  # Detecting/pausing/stopping/testing complete/error reporting signal
    fps = Signal(str)  # fps
    labels = Signal(dict)  # Detected target results (number of each category)
    progress = Signal(int)  # Completeness
    class_num = Signal(int)  # Number of categories detected
    target_num = Signal(int)  # Targets detected
    res_crop_img = Signal(np.ndarray)

    def __init__(self, cfg=DEFAULT_CFG, overrides=None):
        super(YolovClipReidentifier, self).__init__()
        QObject.__init__(self)
        self.args = get_cfg(cfg, overrides)
        self.args.classes = [0]
        project = self.args.project or Path(SETTINGS['runs_dir']) / 're-identify'
        name = f'ReidentificationOutput'
        self.save_dir = increment_path(Path(project) / name, exist_ok=self.args.exist_ok)
        self.done_warmup = False
        if self.args.show:
            self.args.show = check_imshow(warn=True)

        # GUI args
        self.used_model_name = None  # The detection model name to use
        self.new_model_name = None  # Models that change in real time
        self.used_reid_model_name = None  # The reid model name to use
        self.new_reid_model_name = None  # Models that change in real time
        self.source = ''  # input source
        self.stop_dtc = False  # Termination detection
        self.continue_dtc = True  # pause
        self.save_res = False  # Save test results
        self.save_txt = False  # save label(txt) file
        self.iou_thres = 0.45  # iou
        self.conf_thres = 0.25  # conf
        self.speed_thres = 10  # delay, ms
        self.labels_dict = {}  # return a dictionary of results
        self.progress_value = 0  # progress bar
        self.percent_length = 1000

        # Usable if setup is done
        self.model = None
        self.reid_model = None
        self.data = self.args.data  # data_dict
        self.reid_results = None
        self.imgsz = None
        self.device = None
        self.dataset = None
        self.vid_path, self.vid_writer = None, None
        self.annotator = None
        self.data_path = None
        self.image_path = None
        self.source_type = None
        self.batch = None
        self.callbacks = defaultdict(list, callbacks.default_callbacks)  # add callbacks
        callbacks.add_integration_callbacks(self)
        self.highest_similarity = -1

    # main for detect
    @smart_inference_mode()
    @torch.no_grad()
    def run(self):
        # try:
        if self.args.verbose:
            LOGGER.info('')

        # set model
        self.status_msg.emit('Loding Model...')
        if not self.model:
            self.setup_model(self.new_model_name)
            self.used_model_name = self.new_model_name
        if not self.reid_model:
            self.reid_model = CLIPReIDModel('./clipreid/configs/person/cnn_clipreid.yml',
                                            self.new_reid_model_name)
        # set source
        self.imgsz = check_imgsz(self.args.imgsz, stride=self.model.stride, min_dim=2)  # check image size
        if self.args.task == 'classify':
            transforms = getattr(self.model.model, 'transforms', classify_transforms(self.imgsz[0]))
        else:  # predict, segment
            transforms = None
        self.dataset = load_inference_source(source=self.source,
                                             transforms=transforms,
                                             imgsz=self.imgsz,
                                             vid_stride=self.args.vid_stride,
                                             stride=self.model.stride,
                                             auto=self.model.pt)
        self.source_type = self.dataset.source_type
        self.vid_path, self.vid_writer = [None] * self.dataset.bs, [None] * self.dataset.bs

        # Check save path/label
        if self.save_res or self.save_txt:
            (self.save_dir / 'labels' if self.save_txt else self.save_dir).mkdir(parents=True, exist_ok=True)

        # warmup model
        if not self.done_warmup:
            self.model.warmup(imgsz=(1 if self.model.pt or self.model.triton else self.dataset.bs, 3, *self.imgsz))
            self.done_warmup = True

        self.seen, self.windows, self.dt, self.batch = 0, [], (ops.Profile(), ops.Profile(), ops.Profile()), None

        target_feat_list = []
        img = torch.stack([self.reid_model.transform(Image.open(self.image_path).convert('RGB'))], dim=0)
        # for _, (img, _, _, _, _, _) in enumerate(self.reid_model.target_img):
        target_feat = self.reid_model.extract_feature(img)
        target_feat_list.append(target_feat)
        # start detection
        # for batch in self.dataset:
        count = 0  # run location frame
        start_time = time.time()  # used to calculate the frame rate
        batch = iter(self.dataset)
        while True:
            # Termination detection
            if self.stop_dtc:
                if self.vid_writer:
                    if isinstance(self.vid_writer[-1], cv2.VideoWriter):
                        self.vid_writer[-1].release()  # release final video writer
                self.vid_cap.release()
                self.status_msg.emit('Re-identification terminated')
                if self.save_res or self.save_txt:
                    self.status_msg.emit('Re-identification terminated! Save dir:' + str(self.save_dir))
                    # 获取当前目录
                    current_dir = os.getcwd()
                    path = os.path.join(current_dir, str(self.save_dir / p.name))
                    record = Record(p.name, datetime.now(), 're-identify', path, self.reid_results, None, None, None)
                    record_dao.add_record(record)
                break

            # Change the model midway
            if self.used_model_name != self.new_model_name:
                # self.status_msg.emit('Change Model...')
                self.setup_model(self.new_model_name)
                self.used_model_name = self.new_model_name

            # pause switch
            if self.continue_dtc:
                # time.sleep(0.001)
                self.status_msg.emit('Re-identifying...')
                batch = next(self.dataset)  # next data

                self.batch = batch
                path, im, im0s, self.vid_cap, _ = batch
                visualize = increment_path(self.save_dir / Path(path).stem,
                                           mkdir=True) if self.args.visualize else False

                # Calculation completion and frame rate (to be optimized)
                count += 1  # frame count +1
                if self.vid_cap:
                    all_count = self.vid_cap.get(cv2.CAP_PROP_FRAME_COUNT)  # total frames
                    self.progress_value = int(count / all_count * 1000)  # progress bar(0~1000)
                    self.progress.emit(self.progress_value)
                else:
                    self.progress_value = self.percent_length

                if count % 5 == 0 and count >= 5:  # Calculate the frame rate every 5 frames
                    self.fps.emit(str(int(5 / (time.time() - start_time))))
                    start_time = time.time()
                # preprocess
                with self.dt[0]:
                    im = self.preprocess(im)
                    if len(im.shape) == 3:
                        im = im[None]  # expand for batch dim
                # inference
                with self.dt[1]:
                    preds = self.model(im, augment=self.args.augment, visualize=visualize)
                # postprocess
                with self.dt[2]:
                    self.results = self.postprocess(preds, im, im0s)

                if count % 5 == 0 and count >= 5:
                    # reid main process
                    milliseconds = self.vid_cap.get(cv2.CAP_PROP_POS_MSEC)
                    seconds = milliseconds // 1000

                    for r in self.results:
                        res_im = r.orig_img
                        indexs = r.boxes.xyxy
                        for target_feat in target_feat_list:
                            for xyxy in indexs:
                                xmin = int(xyxy[0].item())
                                ymin = int(xyxy[1].item())
                                xmax = int(xyxy[2].item())
                                ymax = int(xyxy[3].item())
                                crop = torch.stack([self.reid_model.transform(
                                    Image.fromarray(res_im[ymin:ymax, xmin:xmax], 'RGB')
                                )], dim=0)
                                # crop = frame[ymin:ymax, xmin:xmax]
                                crop_feat = self.reid_model.extract_feature(crop)
                                current_similarity = self.reid_model.match(target_feat.cpu(), crop_feat.cpu())
                                if current_similarity > 0.85:
                                    self.status_msg.emit(str(seconds))
                                    if self.reid_results is not None:
                                        self.reid_results = self.reid_results + '/' + str(seconds)
                                    else:
                                        self.reid_results = str(seconds)
                                    self.res_crop_img.emit(r.orig_img[ymin:ymax, xmin:xmax])
                                    cv2.rectangle(res_im, (xmin, ymin), (xmax, ymax), (255, 0, 255), 3)
                                if current_similarity > self.highest_similarity:
                                    self.highest_similarity = current_similarity
                    # visualize, save, write results
                    n = len(im)  # To be improved: support multiple img
                    for i in range(n):
                        self.results[i].speed = {
                            'preprocess': self.dt[0].dt * 1E3 / n,
                            'inference': self.dt[1].dt * 1E3 / n,
                            'postprocess': self.dt[2].dt * 1E3 / n}
                        # p, im0 = (path[i], im0s[i].copy()) if self.source_type.webcam or self.source_type.from_img \
                        p, im0 = (path[i], im0s[i].copy()) if self.source_type.from_img else (path, im0s.copy())
                        p = Path(p)  # the source dir
                        # s:::   video 1/1 (6/6557) 'path':
                        # must, to get boxs\labels
                        label_str = self.write_results(i, self.results, (p, im, im0))  # labels   /// original :s +=

                        # labels and nums dict
                        class_nums = 0
                        target_nums = 0
                        self.labels_dict = {}
                        if 'no detections' in label_str:
                            pass
                        else:
                            for ii in label_str.split(',')[:-1]:
                                nums, label_name = ii.split('~')
                                self.labels_dict[label_name] = int(nums)
                                target_nums += int(nums)
                                class_nums += 1
                        # save img or video result
                        if self.save_res:
                            self.save_preds(self.vid_cap, i, str(self.save_dir / p.name))
                        # Send test results
                        self.res_img.emit(res_im)  # after reid
                        # self.pre_img.emit(im0s if isinstance(im0s, np.ndarray) else im0s[0])  # Before testing
                        # self.labels.emit(self.labels_dict)        # webcam need to change the def write_results
                        self.class_num.emit(class_nums)
                        self.target_num.emit(target_nums)

                        if self.speed_thres != 0:
                            time.sleep(self.speed_thres / 1000)  # delay , ms
                    self.progress.emit(self.progress_value)  # progress bar

            # Re-identification completed
            if self.progress_value == self.percent_length:
                if self.vid_writer:
                    if isinstance(self.vid_writer[-1], cv2.VideoWriter):
                        self.vid_writer[-1].release()  # release final video writer
                self.vid_cap.release()
                self.status_msg.emit('Re-identification completed')
                if self.save_res or self.save_txt:
                    self.status_msg.emit('Re-identification completed! Save dir:' + str(self.save_dir))
                    # 获取当前目录
                    current_dir = os.getcwd()
                    path = os.path.join(current_dir, str(self.save_dir / p.name))
                    record = Record(p.name, datetime.now(), 're-identify', path, self.reid_results, None, None, None)
                    record_dao.add_record(record)
                self.progress.emit(0)  # progress bar
                break

    # except Exception as e:
    #     pass
    #     print(e)
    #     self.status_msg.emit('%s' % e)

    def get_annotator(self, img):
        return Annotator(img, line_width=self.args.line_thickness, example=str(self.model.names))

    def preprocess(self, img):
        img = torch.from_numpy(img).to(self.model.device)
        img = img.half() if self.model.fp16 else img.float()  # uint8 to fp16/32
        img /= 255  # 0 - 255 to 0.0 - 1.0
        return img

    def postprocess(self, preds, img, orig_img):
        ### important
        preds = ops.non_max_suppression(preds,
                                        self.conf_thres,
                                        self.iou_thres,
                                        agnostic=self.args.agnostic_nms,
                                        max_det=self.args.max_det,
                                        classes=self.args.classes)
        results = []
        for i, pred in enumerate(preds):
            orig_img = orig_img[i] if isinstance(orig_img, list) else orig_img
            shape = orig_img.shape
            pred[:, :4] = ops.scale_boxes(img.shape[2:], pred[:, :4], shape).round()
            path, _, _, _, _ = self.batch
            img_path = path[i] if isinstance(path, list) else path
            results.append(Results(orig_img=orig_img, path=img_path, names=self.model.names, boxes=pred))
        # print(results)
        return results

    def write_results(self, idx, results, batch):
        p, im, im0 = batch
        log_string = ''
        if len(im.shape) == 3:
            im = im[None]  # expand for batch dim
        self.seen += 1
        imc = im0.copy() if self.args.save_crop else im0
        if self.source_type.webcam or self.source_type.from_img:  # batch_size >= 1         # attention
            # log_string += f'{idx}: '
            frame = self.dataset.count
        else:
            frame = getattr(self.dataset, 'frame', 0)
        self.data_path = p
        self.txt_path = str(self.save_dir / 'labels' / p.stem) + ('' if self.dataset.mode == 'image' else f'_{frame}')
        # log_string += '%gx%g ' % im.shape[2:]         # !!! don't add img size~
        self.annotator = self.get_annotator(im0)

        det = results[idx].boxes  # TODO: make boxes inherit from tensors

        if len(det) == 0:
            return f'{log_string}(no detections), '  # if no, send this~~

        for c in det.cls.unique():
            n = (det.cls == c).sum()  # detections per class
            log_string += f"{n}~{self.model.names[int(c)]},"  # {'s' * (n > 1)}, "   # don't add 's'
        # now log_string is the classes 👆

        # write
        for d in reversed(det):
            cls, conf = d.cls.squeeze(), d.conf.squeeze()
            if self.save_txt:  # Write to file
                line = (cls, *(d.xywhn.view(-1).tolist()), conf) \
                    if self.args.save_conf else (cls, *(d.xywhn.view(-1).tolist()))  # label format
                with open(f'{self.txt_path}.txt', 'a') as f:
                    f.write(('%g ' * len(line)).rstrip() % line + '\n')
            if self.save_res or self.args.save_crop or self.args.show or True:  # Add bbox to image(must)
                c = int(cls)  # integer class
                name = f'id:{int(d.id.item())} {self.model.names[c]}' if d.id is not None else self.model.names[c]
                label = None if self.args.hide_labels else (name if self.args.hide_conf else f'{name} {conf:.2f}')
                self.annotator.box_label(d.xyxy.squeeze(), label, color=colors(c, True))
            if self.args.save_crop:
                save_one_box(d.xyxy,
                             imc,
                             file=self.save_dir / 'crops' / self.model.model.names[c] / f'{self.data_path.stem}.jpg',
                             BGR=True)

        return log_string

    def save_preds(self, vid_cap, idx, save_path):
        im0 = self.annotator.result()
        # save imgs
        if self.dataset.mode == 'image':
            cv2.imwrite(save_path, im0)
        else:  # 'video' or 'stream'
            if self.vid_path:  # 'video'
                if self.vid_path[idx] != save_path:  # new video
                    self.vid_path[idx] = save_path
                    if isinstance(self.vid_writer[idx], cv2.VideoWriter):
                        self.vid_writer[idx].release()  # release previous video writer
                    if vid_cap:  # video
                        fps = int(vid_cap.get(cv2.CAP_PROP_FPS))  # integer required, floats produce error in MP4 codec
                        w = int(vid_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                        h = int(vid_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                    # else:  # stream
                    #     fps, w, h = 30, im0.shape[1], im0.shape[0]
                    save_path = str(Path(save_path).with_suffix('.mp4'))  # force *.mp4 suffix on results videos
                    self.vid_writer[idx] = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))
                self.vid_writer[idx].write(im0)
            else:  # 'stream'
                if vid_cap:
                    fps = int(vid_cap.get(cv2.CAP_PROP_FPS))  # integer required, floats produce error in MP4 codec
                    w = int(vid_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                    h = int(vid_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                # save_path = str(Path(save_path).with_suffix('.mp4'))  # force *.mp4 suffix on results videos
                if not self.vid_writer:
                    self.vid_writer.append(cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h)))
            self.vid_writer[0].write(im0)
