# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
                               QSizePolicy, QTextEdit, QVBoxLayout, QWidget, QDialog)

class EditDialogBox(QDialog,object):
    confirmed = Signal()  # 定义一个自定义信号

    def __init__(self):
        super(EditDialogBox, self).__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(425, 300)
        font = QFont()
        font.setPointSize(16)
        Form.setFont(font)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title_label = QLabel(Form)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setFont(font)

        self.verticalLayout.addWidget(self.title_label)

        self.title_edit = QLineEdit(Form)
        self.title_edit.setObjectName(u"title_edit")

        self.verticalLayout.addWidget(self.title_edit)

        self.description_label = QLabel(Form)
        self.description_label.setObjectName(u"description_label")
        self.description_label.setFont(font)

        self.verticalLayout.addWidget(self.description_label)

        self.description_edit = QTextEdit(Form)
        self.description_edit.setObjectName(u"description_edit")
        self.description_edit.setMinimumSize(QSize(0, 96))

        self.verticalLayout.addWidget(self.description_edit)

        self.confirm_button = QPushButton(Form)
        self.confirm_button.setObjectName(u"confirm_button")
        self.confirm_button.clicked.connect(self.confirm)

        self.verticalLayout.addWidget(self.confirm_button)

        self.cancel_button = QPushButton(Form)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.clicked.connect(self.reject)

        self.verticalLayout.addWidget(self.cancel_button)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi
    def confirm(self):
        # 发出自定义信号
        self.confirmed.emit()
        # 关闭对话框
        self.accept()

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.title_label.setText(QCoreApplication.translate("Form", u"Title:", None))
        self.description_label.setText(QCoreApplication.translate("Form", u"Description:", None))
        self.confirm_button.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4", None))
        self.cancel_button.setText(QCoreApplication.translate("Form", u"\u53d6\u6d88", None))
    # retranslateUi

