# -*- coding: utf-8 -*-
import sys

from PySide6 import QtCore
################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
                               QPushButton, QSizePolicy, QWidget, QMessageBox)

from main import *
from dao import user_dao
from entity.user_model import User


class Ui_Form(QWidget):

    def __init__(self):
        super(Ui_Form, self).__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(517, 369)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(100, 140, 311, 91))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setContentsMargins(30, 10, 10, 0)
        self.lineEdit = QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.setWindowIcon(QPixmap(u"img/user.png"))
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.lineEdit_2 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_2)

        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(120, 270, 101, 31))
        icon = QIcon()
        icon.addFile(u"img/login.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.clicked.connect(self.login)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(290, 270, 101, 31))
        icon1 = QIcon()
        icon1.addFile(u"img/reset.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.clicked.connect(self.resetForm)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(180, 60, 251, 51))
        font1 = QFont()
        font1.setPointSize(26)
        self.label_3.setFont(font1)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(110, 50, 61, 61))
        self.label_4.setPixmap(QPixmap(u"img/logo.jpg").scaled(self.label_4.size(), aspectMode=Qt.KeepAspectRatio))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "管理员登录"))
        self.label.setText(_translate("Form", "用户名："))
        self.label_2.setText(_translate("Form", "密  码："))
        self.pushButton.setText(_translate("Form", "登录"))
        self.pushButton_2.setText(_translate("Form", "重置"))
        self.label_3.setText(_translate("Form", "行人重识别系统"))

    def resetForm(self):
        """
        重置
        :return:
        """
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")

    def login(self):
        """
        用户登录判断 数据库判断成功，则打开主窗体，否则提示报错信息
        :return:
        """
        userName = self.lineEdit.text()
        password = self.lineEdit_2.text()
        if userName.strip() == "" or password.strip() == "":
            QMessageBox.warning(None, '系统提示', '用户名和密码不能为空！')
        else:
            user = User(userName, password)
            resultUser = userDao.login(user)
            if resultUser:
                userDao.currentUser = user
                self.m = MainWindow()  # 实例化主窗体
                self.m.show()  # 打开主窗体
                self.hide()  # 隐藏登录窗体
            else:
                QMessageBox.warning(None, '系统提示', '用户名或者密码输入错误！')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = Ui_Form()
    ui.show()

    sys.exit(app.exec())