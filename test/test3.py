from ultralytics import YOLO
import os

os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
if __name__ == '__main__':
    model = YOLO('D:/daima/python/pyqt/yolov-models/yolov8n.pt')
    # 使用模型对图像进行目标追踪
    results = model.predict(source="行人走路.mp4", show=True, save_crop=True, save=True,
                            name="output")
