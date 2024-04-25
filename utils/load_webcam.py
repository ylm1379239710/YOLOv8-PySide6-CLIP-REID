import cv2
import numpy as np
from ultralytics.yolo.data.augment import LetterBox


class LoadWebcam:  # for inference
    # YOLOv5 local webcam dataloader, i.e. `python detect.py --source 0`
    def __init__(self, pipe='0', imgsz=640, stride=32,auto=True, transforms=None):
        self.transforms = transforms
        self.imgsz = imgsz
        self.stride = stride
        self.pipe = eval(pipe) if pipe.isnumeric() else pipe
        self.cap = cv2.VideoCapture(self.pipe)  # video capture object
        self.cap.set(cv2.CAP_PROP_BUFFERSIZE, 3)  # set buffer size
        self.bs = self.__len__()
        self.mode= 'stream'
        self.auto = auto
    def __iter__(self):
        self.count = -1
        return self

    def __next__(self):
        self.count += 1
        if cv2.waitKey(1) == ord('q'):  # q to quit
            self.cap.release()
            cv2.destroyAllWindows()
            raise StopIteration

        # Read frame
        ret_val, img0 = self.cap.read()
        # Print
        assert ret_val, f'Camera Error {self.pipe}'
        img_path = 'webcam.mp4'
        s = f'webcam {self.count}: '

        if self.transforms:
            im = self.transforms(img0)  # transforms
        else:
            im = LetterBox(self.imgsz, self.auto, stride=self.stride)(image=img0)
            im = im.transpose((2, 0, 1))[::-1]  # HWC to CHW, BGR to RGB
            im = np.ascontiguousarray(im)  # contiguous

        return img_path, im, img0, self.cap , s

    def __len__(self):
        return 0  # 1E12 frames = 32 streams at 30 FPS for 30 years