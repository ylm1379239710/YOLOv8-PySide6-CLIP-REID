from ultralytics import YOLO
from PIL import Image

if __name__ == '__main__':
    model = YOLO('../yolov-models/yolov8n.pt')
    # 使用模型对图像进行目标检测
    im1 = Image.open("../data/person.jpg")
    results = model.predict(source=im1, show=True, save_crop=True,
                            name='output')  # save plotted images
    for r in results :
        print(r.names)
