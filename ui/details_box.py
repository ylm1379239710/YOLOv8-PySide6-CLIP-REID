# -*- coding: utf-8 -*-
import os

################################################################################
## Form generated from reading UI file 'details_box.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
                               QSizePolicy, QWidget, QVBoxLayout, QPushButton)

class DetailsBox(QWidget,object):
    def __init__(self, file_path):
        super(DetailsBox, self).__init__()
        self.setupUi(self, file_path)

    def setupUi(self, Form, file_path):
        _, file_extension = os.path.splitext(file_path)

        if file_extension.lower() in ['.png', '.jpg', '.jpeg', '.bmp']:  # 假设这些是图片格式
            self.showImage(file_path, Form)
        elif file_extension.lower() in ['.mp4', '.avi', '.mkv', '.mov']:  # 假设这些是视频格式
            self.playVideo(file_path, Form)
        else:
            print(f"Unsupported file type: {file_extension}")

    def showImage(self, file_path, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 342)
        Form.setMinimumSize(QSize(500, 0))
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.picture = QLabel(Form)
        self.picture.setObjectName(u"picture")
        self.picture.setMinimumSize(QSize(200, 0))
        # 使用QPixmap加载图片
        pixmap = QPixmap(file_path)
        # 如果图片加载失败，则尝试使用QImage加载并转换为QPixmap
        if pixmap.isNull():
            image = QImage(file_path)
            if not image.isNull():
                pixmap = QPixmap.fromImage(image)
        if not pixmap.isNull():
            scaled_pixmap = pixmap.scaled(QSize(256,512), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            # 将图片设置到QLabel上
            self.picture.setPixmap(scaled_pixmap)

        self.horizontalLayout.addWidget(self.picture)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.formLayout = QFormLayout(self.widget)
        self.formLayout.setObjectName(u"formLayout")
        self.id_label = QLabel(self.widget)
        self.id_label.setObjectName(u"id_label")
        font = QFont()
        font.setPointSize(16)
        self.id_label.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.id_label)

        self.title_label = QLabel(self.widget)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.title_label)

        self.description_label = QLabel(self.widget)
        self.description_label.setObjectName(u"description_label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.description_label.sizePolicy().hasHeightForWidth())
        self.description_label.setSizePolicy(sizePolicy)
        self.description_label.setFont(font)
        self.description_label.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.description_label)

        self.upload_date_label = QLabel(self.widget)
        self.upload_date_label.setObjectName(u"upload_date_label")
        sizePolicy.setHeightForWidth(self.upload_date_label.sizePolicy().hasHeightForWidth())
        self.upload_date_label.setSizePolicy(sizePolicy)
        self.upload_date_label.setFont(font)
        self.upload_date_label.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.upload_date_label)

        self.file_path_label = QLabel(self.widget)
        self.file_path_label.setObjectName(u"file_path_label")
        sizePolicy.setHeightForWidth(self.file_path_label.sizePolicy().hasHeightForWidth())
        self.file_path_label.setSizePolicy(sizePolicy)
        self.file_path_label.setFont(font)
        self.file_path_label.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.file_path_label)

        self.file_name_label = QLabel(self.widget)
        self.file_name_label.setObjectName(u"file_name_label")
        sizePolicy.setHeightForWidth(self.file_name_label.sizePolicy().hasHeightForWidth())
        self.file_name_label.setSizePolicy(sizePolicy)
        self.file_name_label.setFont(font)
        self.file_name_label.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.file_name_label)

        self.file_size_label = QLabel(self.widget)
        self.file_size_label.setObjectName(u"file_size_label")
        sizePolicy.setHeightForWidth(self.file_size_label.sizePolicy().hasHeightForWidth())
        self.file_size_label.setSizePolicy(sizePolicy)
        self.file_size_label.setFont(font)
        self.file_size_label.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.file_size_label)

        self.file_type_label = QLabel(self.widget)
        self.file_type_label.setObjectName(u"file_type_label")
        sizePolicy.setHeightForWidth(self.file_type_label.sizePolicy().hasHeightForWidth())
        self.file_type_label.setSizePolicy(sizePolicy)
        self.file_type_label.setFont(font)
        self.file_type_label.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.formLayout.setWidget(14, QFormLayout.LabelRole, self.file_type_label)

        self.id_text = QLabel(self.widget)
        self.id_text.setObjectName(u"id_text")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.id_text)

        self.title_text = QLabel(self.widget)
        self.title_text.setObjectName(u"title_text")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.title_text)

        self.description_text = QLabel(self.widget)
        self.description_text.setObjectName(u"description_text")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.description_text)

        self.upload_date_text = QLabel(self.widget)
        self.upload_date_text.setObjectName(u"upload_date_text")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.upload_date_text)

        self.file_path_text = QLabel(self.widget)
        self.file_path_text.setObjectName(u"file_path_text")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.file_path_text)

        self.file_name_text = QLabel(self.widget)
        self.file_name_text.setObjectName(u"file_name_text")

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.file_name_text)

        self.file_size_text = QLabel(self.widget)
        self.file_size_text.setObjectName(u"file_size_text")

        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.file_size_text)

        self.file_type_text = QLabel(self.widget)
        self.file_type_text.setObjectName(u"file_type_text")

        self.formLayout.setWidget(14, QFormLayout.FieldRole, self.file_type_text)


        self.horizontalLayout.addWidget(self.widget)
        self.id_text.setWordWrap(True)
        self.title_text.setWordWrap(True)
        self.description_text.setWordWrap(True)
        self.upload_date_text.setWordWrap(True)
        self.file_type_text.setWordWrap(True)
        self.file_size_text.setWordWrap(True)
        self.file_name_text.setWordWrap(True)
        self.file_path_text.setWordWrap(True)
        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def playVideo(self, video_path, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 342)
        Form.setMinimumSize(QSize(500, 0))
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        # 创建一个 QMediaPlayer 实例
        self.player = QMediaPlayer(self)
        # 创建一个 QVideoWidget 实例，用于显示视频
        self.videoWidget = QVideoWidget()
        # 设置视频源
        self.player.setSource(QUrl.fromLocalFile(video_path))
        # 将视频输出设置为 QVideoWidget
        self.player.setVideoOutput(self.videoWidget)
        layout = QVBoxLayout()
        self.play_pause_button = QPushButton("Play", self)
        self.play_pause_button.clicked.connect(self.toggle_playback)
        layout.addWidget(self.play_pause_button)
        layout.addWidget(self.videoWidget)

        self.horizontalLayout.addLayout(layout)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.formLayout = QFormLayout(self.widget)
        self.formLayout.setObjectName(u"formLayout")
        self.id_label = QLabel(self.widget)
        self.id_label.setObjectName(u"id_label")
        font = QFont()
        font.setPointSize(16)
        self.id_label.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.id_label)

        self.title_label = QLabel(self.widget)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.title_label)

        self.description_label = QLabel(self.widget)
        self.description_label.setObjectName(u"description_label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.description_label.sizePolicy().hasHeightForWidth())
        self.description_label.setSizePolicy(sizePolicy)
        self.description_label.setFont(font)
        self.description_label.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.description_label)

        self.upload_date_label = QLabel(self.widget)
        self.upload_date_label.setObjectName(u"upload_date_label")
        sizePolicy.setHeightForWidth(self.upload_date_label.sizePolicy().hasHeightForWidth())
        self.upload_date_label.setSizePolicy(sizePolicy)
        self.upload_date_label.setFont(font)
        self.upload_date_label.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.upload_date_label)

        self.file_path_label = QLabel(self.widget)
        self.file_path_label.setObjectName(u"file_path_label")
        sizePolicy.setHeightForWidth(self.file_path_label.sizePolicy().hasHeightForWidth())
        self.file_path_label.setSizePolicy(sizePolicy)
        self.file_path_label.setFont(font)
        self.file_path_label.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.file_path_label)

        self.file_name_label = QLabel(self.widget)
        self.file_name_label.setObjectName(u"file_name_label")
        sizePolicy.setHeightForWidth(self.file_name_label.sizePolicy().hasHeightForWidth())
        self.file_name_label.setSizePolicy(sizePolicy)
        self.file_name_label.setFont(font)
        self.file_name_label.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.file_name_label)

        self.file_size_label = QLabel(self.widget)
        self.file_size_label.setObjectName(u"file_size_label")
        sizePolicy.setHeightForWidth(self.file_size_label.sizePolicy().hasHeightForWidth())
        self.file_size_label.setSizePolicy(sizePolicy)
        self.file_size_label.setFont(font)
        self.file_size_label.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.file_size_label)

        self.file_type_label = QLabel(self.widget)
        self.file_type_label.setObjectName(u"file_type_label")
        sizePolicy.setHeightForWidth(self.file_type_label.sizePolicy().hasHeightForWidth())
        self.file_type_label.setSizePolicy(sizePolicy)
        self.file_type_label.setFont(font)
        self.file_type_label.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.formLayout.setWidget(14, QFormLayout.LabelRole, self.file_type_label)

        self.id_text = QLabel(self.widget)
        self.id_text.setObjectName(u"id_text")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.id_text)

        self.title_text = QLabel(self.widget)
        self.title_text.setObjectName(u"title_text")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.title_text)

        self.description_text = QLabel(self.widget)
        self.description_text.setObjectName(u"description_text")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.description_text)

        self.upload_date_text = QLabel(self.widget)
        self.upload_date_text.setObjectName(u"upload_date_text")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.upload_date_text)

        self.file_path_text = QLabel(self.widget)
        self.file_path_text.setObjectName(u"file_path_text")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.file_path_text)

        self.file_name_text = QLabel(self.widget)
        self.file_name_text.setObjectName(u"file_name_text")

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.file_name_text)

        self.file_size_text = QLabel(self.widget)
        self.file_size_text.setObjectName(u"file_size_text")

        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.file_size_text)

        self.file_type_text = QLabel(self.widget)
        self.file_type_text.setObjectName(u"file_type_text")

        self.formLayout.setWidget(14, QFormLayout.FieldRole, self.file_type_text)


        self.horizontalLayout.addWidget(self.widget)
        self.id_text.setWordWrap(True)
        self.title_text.setWordWrap(True)
        self.description_text.setWordWrap(True)
        self.upload_date_text.setWordWrap(True)
        self.file_type_text.setWordWrap(True)
        self.file_size_text.setWordWrap(True)
        self.file_name_text.setWordWrap(True)
        self.file_path_text.setWordWrap(True)
        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi
    def toggle_playback(self):
        if self.player.playbackState() == QMediaPlayer.PlayingState:
            self.player.pause()
            self.play_pause_button.setText('Play')
        else:
            self.player.play()
            self.play_pause_button.setText('Pause')
    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.id_label.setText(QCoreApplication.translate("Form", u"ID\uff1a", None))
        self.title_label.setText(QCoreApplication.translate("Form", u"Title\uff1a", None))
        self.description_label.setText(QCoreApplication.translate("Form", u"Description\uff1a", None))
        self.upload_date_label.setText(QCoreApplication.translate("Form", u"UploadDate\uff1a", None))
        self.file_path_label.setText(QCoreApplication.translate("Form", u"FilePath\uff1a", None))
        self.file_name_label.setText(QCoreApplication.translate("Form", u"FileName\uff1a", None))
        self.file_size_label.setText(QCoreApplication.translate("Form", u"FileSize\uff1a", None))
        self.file_type_label.setText(QCoreApplication.translate("Form", u"FileType\uff1a", None))
        self.id_text.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.title_text.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.description_text.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.upload_date_text.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.file_path_text.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.file_name_text.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.file_size_text.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.file_type_text.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

