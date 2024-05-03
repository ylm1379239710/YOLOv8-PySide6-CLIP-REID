# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'custom_confirm_message_box.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, Signal)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
                               QSizePolicy, QVBoxLayout, QDialog, QWidget)

class ConfirmMessageBox(QDialog,object):
    confirmed = Signal()  # 定义一个自定义信号

    def __init__(self):
        super(ConfirmMessageBox, self).__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(302, 146)
        Form.setMinimumSize(QSize(0, 100))
        icon = QIcon()
        icon.addFile(u":/all/img/logo.jpg", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.text = QLabel(Form)
        self.text.setObjectName(u"text")
        font = QFont()
        font.setPointSize(16)
        self.text.setFont(font)
        self.text.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.text)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 0))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(60)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.yes_button = QPushButton(self.widget)
        self.yes_button.setObjectName(u"yes_button")
        self.yes_button.setFont(font)
        self.yes_button.clicked.connect(self.confirm)

        self.horizontalLayout.addWidget(self.yes_button)

        self.no_button = QPushButton(self.widget)
        self.no_button.setObjectName(u"no_button")
        self.no_button.setFont(font)
        self.no_button.clicked.connect(self.reject)

        self.horizontalLayout.addWidget(self.no_button)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)


    def confirm(self):
        # 发出自定义信号
        self.confirmed.emit()
        # 关闭对话框
        self.accept()

    # setupUi
    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.text.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4\u8fdb\u884c\u8be5\u64cd\u4f5c\u5417\uff1f", None))
        self.yes_button.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4", None))
        self.no_button.setText(QCoreApplication.translate("Form", u"\u53d6\u6d88", None))
    # retranslateUi

