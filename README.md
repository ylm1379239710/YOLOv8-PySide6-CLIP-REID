# YPCRer — Pedestrian Re-Identification System Based on YOLOv8 and CLIP-ReID

---
## 📚 项目简介

YPCRer 是在 YoloSide v2 项目基础上进行的再开发，在原有的目标检测功能上进行改动。引入CLIP-ReID，新增了数据管理（增删改查）、行人重识别和任务记录功能。此次项目是为了学习目标检测和重识别技术，同时学习使用了QT的Pyside6进行桌面应用开发。我也有相关的资料可以找我QQ：1379239710。

---
## ✏️ 参考项目链接

### CLIP-ReID 项目
**源码链接**：
- Github：[https://github.com/Syliz517/CLIP-ReID](https://github.com/Syliz517/CLIP-ReID)

### 界面功能等参考
**链接**：
- Github：[https://github.com/Jai-wei/YOLOv8-PySide6-GUI](https://github.com/Jai-wei/YOLOv8-PySide6-GUI)
- B站：[YoloSide V2.0 ~ yolov8 pyside6 可视化界面 gui 目标检测 毕业设计](https://www.bilibili.com/video/BV1Cb411f7cw/?spm_id_from=333.337.search-card.all.click&vd_source=eb243edd059640e52705bf18f8a0d6a8)

### YOLOv8
- Github：[ultralytics](https://github.com/ultralytics/ultralytics?tab=readme-ov-file)
---
## 🎦 视频展示
- B站：[YPCRer——基于Yolov8和CLIP-ReID的行人重识别系统](https://www.bilibili.com/video/BV1oTzGYPEsn/?spm_id_from=333.337.search-card.all.click&vd_source=eb243edd059640e52705bf18f8a0d6a8)

---
## 💻 核心技术栈

### 后端：
- 数据库：MySQL 8.0

### 前端
- Pyside6

### 目标检测技术
- YOLOv8

### 重识别技术
- CLIP-ReId

---

## 🔨 开发环境

- 操作系统：Windows 11
- 集成开发工具：Pycharm
- 版本控制工具：Git
- 环境管理：Anaconda （Python 版本：3.11）

---

## 📊 代码架构

![代码架构](https://github.com/ylm1379239710/YOLOv8-PySide6-CLIP-REID/raw/main/img/Architecture.png)
- [显示不了点这里](https://gitee.com/yang-luming321/yolov8-py-side6-clip-reid/blob/main/README.md#-%E4%BB%A3%E7%A0%81%E6%9E%B6%E6%9E%84)

---

## ☝️ 使用
- 模型准备：下载CLIP-ReId和YOLOv8的模型（模型太大没有上传），要根据模型进行略微修改。
  因为clip-reid的模型太大了上传不了，所以项目的代码架构中reid-models这个文件夹没有需要自己创建，然后放入模型。
  模型的话需要你自己去上面参考项目CLIP-ReID 项目的主页下载,项目里面使用的是Market1501的模型（因为其它模型参数也不一样，需要自己修改参数才能跑其它模型）。
  ![image](https://github.com/user-attachments/assets/dea81516-c805-48a9-8cb1-3c292c57da4a)
- 安装环境

```
conda create -n test(虚拟环境名称，可更换)
conda activate test

下面是安装pytorch，要先安装cuda（根据自己的电脑来，不会可以查教程）
(pytorch推荐2.1.0，尽量别上高版本，容易出错)
conda install pytorch==2.1.0 torchvision==0.16.0 torchaudio==2.1.0 pytorch-cuda=11.8 -c pytorch -c nvidia


pip install yacs
pip install timm
pip install scikit-image
pip install tqdm
pip install ftfy
pip install regex

下面的版本要对应（python为3.11.7版本，下面为适配的版本，版本不一样大概率报错）
pip install ultralytics==8.0.48
pip install pyside6==6.4.2

然后numpy下降到1.24版本
conda install numpy==1.24
然后是安装mysql(如果不需要数据管理功能，可以注释掉相关代码)
分为安装mysql服务和安装pymysql包，不会的搜百度
然后创建数据库，导入sql文件夹中的sql文件
往里面的表都随便添加一些数据

```
---
## 🎀 界面展示

- [显示不了点这里](https://gitee.com/yang-luming321/yolov8-py-side6-clip-reid/blob/main/README.md#-%E7%95%8C%E9%9D%A2%E5%B1%95%E7%A4%BA)

登录：

![登录](https://github.com/ylm1379239710/YOLOv8-PySide6-CLIP-REID/raw/main/img/loginUI.png)

主页：

![主页](https://github.com/ylm1379239710/YOLOv8-PySide6-CLIP-REID/raw/main/img/homeUI.png)

数据管理：

![数据管理](https://github.com/ylm1379239710/YOLOv8-PySide6-CLIP-REID/raw/main/img/dataUI.png)

目标检测：

![目标检测](https://github.com/ylm1379239710/YOLOv8-PySide6-CLIP-REID/raw/main/img/detectUI.png)

重识别：

![重识别](https://github.com/ylm1379239710/YOLOv8-PySide6-CLIP-REID/raw/main/img/reidUI.png)
