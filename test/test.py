from ultralytics import YOLO
from PIL import Image

if __name__ == '__main__':
    # 从头开始创建一个新的YOLO模型
    model = YOLO('yolov8n.yaml')
    # 加载预训练的YOLO模型（推荐用于训练）
    model = YOLO('models/yolov8n.pt')
    # 使用'coco128.yaml'数据集对模型进行训练，训练3个epoch
    results = model.train(data='coco128.yaml', epochs=3)
    # 在验证集上评估模型的性能
    results = model.val()
    # 使用模型对图像进行目标检测
    im1 = Image.open("../data/person.jpg")
    results = model.predict(source=im1, save=True)  # save plotted images
