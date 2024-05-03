# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtGui import (QCursor,
                           QFont, QIcon)
from PySide6.QtWidgets import (QCheckBox, QComboBox,
                               QDoubleSpinBox, QFrame, QHBoxLayout, QLabel, QLayout, QListView, QListWidget,
                               QProgressBar, QPushButton,
                               QSizePolicy, QSlider, QSpacerItem, QSpinBox,
                               QSplitter, QVBoxLayout,
                               QWidget, QLineEdit)
from ui.table import TableWithButtons
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1660, 889)
        icon = QIcon()
        icon.addFile(u":/all/img/logo.jpg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.Main_QW = QWidget(MainWindow)
        self.Main_QW.setObjectName(u"Main_QW")
        self.verticalLayout = QVBoxLayout(self.Main_QW)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Main_QF = QFrame(self.Main_QW)
        self.Main_QF.setObjectName(u"Main_QF")
        self.Main_QF.setStyleSheet(u"QFrame#Main_QF{\n"
"	background-color: qlineargradient(x0:0, y0:1, x1:1, y1:1,stop:0.4  rgb(255, 150, 150), stop:1 rgb(100,10,130 ));\n"
"border:0px solid red;\n"
"border-radius:10px\n"
"}")
        self.horizontalLayout_106 = QHBoxLayout(self.Main_QF)
        self.horizontalLayout_106.setObjectName(u"horizontalLayout_106")
        self.LeftMenuBg = QFrame(self.Main_QF)
        self.LeftMenuBg.setObjectName(u"LeftMenuBg")
        self.LeftMenuBg.setMinimumSize(QSize(180, 0))
        self.LeftMenuBg.setMaximumSize(QSize(68, 16777215))
        self.LeftMenuBg.setStyleSheet(u"QFrame#LeftMenuBg{\n"
"	background-color: rgba(255, 255, 255,0);\n"
"border:0px solid red;\n"
"border-radius:30px\n"
"}")
        self.LeftMenuBg.setFrameShape(QFrame.NoFrame)
        self.LeftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.LeftMenuBg)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.TopLogoInfo = QFrame(self.LeftMenuBg)
        self.TopLogoInfo.setObjectName(u"TopLogoInfo")
        self.TopLogoInfo.setEnabled(True)
        self.TopLogoInfo.setMinimumSize(QSize(0, 70))
        self.TopLogoInfo.setMaximumSize(QSize(16777215, 70))
        self.TopLogoInfo.setFrameShape(QFrame.StyledPanel)
        self.TopLogoInfo.setFrameShadow(QFrame.Raised)
        self.logo = QWidget(self.TopLogoInfo)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(10, 10, 50, 50))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMinimumSize(QSize(50, 50))
        self.logo.setMaximumSize(QSize(50, 50))
        self.logo.setStyleSheet(u"image: url(:/all/img/logo.jpg);\n"
"border:2px solid rgb(255, 255, 255);\n"
"\n"
"")
        self.Author = QLabel(self.TopLogoInfo)
        self.Author.setObjectName(u"Author")
        self.Author.setGeometry(QRect(90, 30, 60, 30))
        sizePolicy.setHeightForWidth(self.Author.sizePolicy().hasHeightForWidth())
        self.Author.setSizePolicy(sizePolicy)
        self.Author.setMinimumSize(QSize(60, 30))
        self.Author.setMaximumSize(QSize(60, 30))
        self.Author.setStyleSheet(u"font: italic 11pt \"Segoe UI\";\n"
"color: rgba(255, 255, 255, 255);")
        self.Author.setAlignment(Qt.AlignCenter)
        self.Title = QLabel(self.TopLogoInfo)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(60, 10, 121, 20))
        self.Title.setMaximumSize(QSize(16777215, 30))
        self.Title.setStyleSheet(u"font: 600 13pt \"Segoe UI Semibold\";\n"
"color: rgba(255, 255, 255, 255);")
        self.Title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.TopLogoInfo)

        self.ToggleBox = QFrame(self.LeftMenuBg)
        self.ToggleBox.setObjectName(u"ToggleBox")
        self.ToggleBox.setMinimumSize(QSize(200, 300))
        self.ToggleBox.setMaximumSize(QSize(200, 300))
        self.ToggleBox.setFrameShape(QFrame.NoFrame)
        self.ToggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.ToggleBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.ToggleBotton = QPushButton(self.ToggleBox)
        self.ToggleBotton.setObjectName(u"ToggleBotton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ToggleBotton.sizePolicy().hasHeightForWidth())
        self.ToggleBotton.setSizePolicy(sizePolicy1)
        self.ToggleBotton.setMinimumSize(QSize(0, 45))
        self.ToggleBotton.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"Nirmala UI"])
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.ToggleBotton.setFont(font)
        self.ToggleBotton.setCursor(QCursor(Qt.PointingHandCursor))
        self.ToggleBotton.setMouseTracking(True)
        self.ToggleBotton.setFocusPolicy(Qt.StrongFocus)
        self.ToggleBotton.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.ToggleBotton.setLayoutDirection(Qt.LeftToRight)
        self.ToggleBotton.setAutoFillBackground(False)
        self.ToggleBotton.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/menu.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 23px solid transparent;\n"
"\n"
"text-align: center;\n"
"padding-left: 0px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 12pt \"Nirmala UI\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(114, 129, 214, 59);\n"
"}")
        icon = QIcon()
        iconThemeName = u"zoom-out"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u"C:/Users/13792/.designer/backup", QSize(), QIcon.Normal, QIcon.Off)

        self.ToggleBotton.setIcon(icon)
        self.ToggleBotton.setAutoDefault(False)
        self.ToggleBotton.setFlat(False)

        self.verticalLayout_4.addWidget(self.ToggleBotton)

        self.HomeBotton = QPushButton(self.ToggleBox)
        self.HomeBotton.setObjectName(u"HomeBotton")
        sizePolicy1.setHeightForWidth(self.HomeBotton.sizePolicy().hasHeightForWidth())
        self.HomeBotton.setSizePolicy(sizePolicy1)
        self.HomeBotton.setMinimumSize(QSize(0, 45))
        self.HomeBotton.setMaximumSize(QSize(16777215, 16777215))
        self.HomeBotton.setFont(font)
        self.HomeBotton.setCursor(QCursor(Qt.PointingHandCursor))
        self.HomeBotton.setMouseTracking(True)
        self.HomeBotton.setFocusPolicy(Qt.StrongFocus)
        self.HomeBotton.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.HomeBotton.setLayoutDirection(Qt.LeftToRight)
        self.HomeBotton.setAutoFillBackground(False)
        self.HomeBotton.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/menu.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 23px solid transparent;\n"
"\n"
"text-align: center;\n"
"padding-left: 0px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 12pt \"Nirmala UI\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(114, 129, 214, 59);\n"
"}")
        self.HomeBotton.setIcon(icon)
        self.HomeBotton.setAutoDefault(False)
        self.HomeBotton.setFlat(False)

        self.verticalLayout_4.addWidget(self.HomeBotton)

        self.DataManageButton = QPushButton(self.ToggleBox)
        self.DataManageButton.setObjectName(u"DataManageButton")
        sizePolicy1.setHeightForWidth(self.DataManageButton.sizePolicy().hasHeightForWidth())
        self.DataManageButton.setSizePolicy(sizePolicy1)
        self.DataManageButton.setMinimumSize(QSize(0, 45))
        self.DataManageButton.setFont(font)
        self.DataManageButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.DataManageButton.setMouseTracking(True)
        self.DataManageButton.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/menu.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 23px solid transparent;\n"
"\n"
"text-align: center;\n"
"padding-left: 0px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 12pt \"Nirmala UI\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(114, 129, 214, 59);\n"
"}")
        self.DataManageButton.setIcon(icon)

        self.verticalLayout_4.addWidget(self.DataManageButton)

        self.DetectButton = QPushButton(self.ToggleBox)
        self.DetectButton.setObjectName(u"DetectButton")
        sizePolicy1.setHeightForWidth(self.DetectButton.sizePolicy().hasHeightForWidth())
        self.DetectButton.setSizePolicy(sizePolicy1)
        self.DetectButton.setMinimumSize(QSize(0, 45))
        self.DetectButton.setFont(font)
        self.DetectButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.DetectButton.setMouseTracking(True)
        self.DetectButton.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/menu.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 23px solid transparent;\n"
"\n"
"text-align: center;\n"
"padding-left: 0px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 12pt \"Nirmala UI\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(114, 129, 214, 59);\n"
"}")
        self.DetectButton.setIcon(icon)

        self.verticalLayout_4.addWidget(self.DetectButton)

        self.ReidButton = QPushButton(self.ToggleBox)
        self.ReidButton.setObjectName(u"ReidButton")
        sizePolicy1.setHeightForWidth(self.ReidButton.sizePolicy().hasHeightForWidth())
        self.ReidButton.setSizePolicy(sizePolicy1)
        self.ReidButton.setMinimumSize(QSize(0, 45))
        self.ReidButton.setFont(font)
        self.ReidButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.ReidButton.setMouseTracking(True)
        self.ReidButton.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/menu.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 23px solid transparent;\n"
"\n"
"text-align: center;\n"
"padding-left: 0px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 12pt \"Nirmala UI\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(114, 129, 214, 59);\n"
"}")
        self.ReidButton.setIcon(icon)

        self.verticalLayout_4.addWidget(self.ReidButton)

        self.TaskRecordButton = QPushButton(self.ToggleBox)
        self.TaskRecordButton.setObjectName(u"TaskRecordButton")
        sizePolicy1.setHeightForWidth(self.TaskRecordButton.sizePolicy().hasHeightForWidth())
        self.TaskRecordButton.setSizePolicy(sizePolicy1)
        self.TaskRecordButton.setMinimumSize(QSize(0, 45))
        self.TaskRecordButton.setFont(font)
        self.TaskRecordButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.TaskRecordButton.setMouseTracking(True)
        self.TaskRecordButton.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/menu.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 23px solid transparent;\n"
"\n"
"text-align: center;\n"
"padding-left: 0px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 12pt \"Nirmala UI\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(114, 129, 214, 59);\n"
"}")
        self.TaskRecordButton.setIcon(icon)

        self.verticalLayout_4.addWidget(self.TaskRecordButton)


        self.verticalLayout_2.addWidget(self.ToggleBox)

        self.MenuBox = QFrame(self.LeftMenuBg)
        self.MenuBox.setObjectName(u"MenuBox")
        self.MenuBox.setMinimumSize(QSize(200, 0))
        self.MenuBox.setMaximumSize(QSize(200, 16777215))
        self.MenuBox.setFrameShape(QFrame.NoFrame)
        self.MenuBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.MenuBox)
        self.verticalLayout_5.setSpacing(15)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.verticalLayout_2.addWidget(self.MenuBox)

        self.VersionInfo = QFrame(self.LeftMenuBg)
        self.VersionInfo.setObjectName(u"VersionInfo")
        self.VersionInfo.setMinimumSize(QSize(200, 10))
        self.VersionInfo.setMaximumSize(QSize(200, 15))
        self.VersionInfo.setFrameShape(QFrame.StyledPanel)
        self.VersionInfo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.VersionInfo)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(18, 0, -1, 0)
        self.VersionLabel = QLabel(self.VersionInfo)
        self.VersionLabel.setObjectName(u"VersionLabel")
        self.VersionLabel.setStyleSheet(u"font: 900 italic 10pt \"Segoe UI\";\n"
"color: rgba(255, 255, 255, 199);")
        self.VersionLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.VersionLabel)


        self.verticalLayout_2.addWidget(self.VersionInfo)


        self.horizontalLayout_106.addWidget(self.LeftMenuBg)

        self.ContentBox = QFrame(self.Main_QF)
        self.ContentBox.setObjectName(u"ContentBox")
        self.ContentBox.setFrameShape(QFrame.StyledPanel)
        self.ContentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.ContentBox)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.top = QFrame(self.ContentBox)
        self.top.setObjectName(u"top")
        self.top.setEnabled(True)
        sizePolicy.setHeightForWidth(self.top.sizePolicy().hasHeightForWidth())
        self.top.setSizePolicy(sizePolicy)
        self.top.setMinimumSize(QSize(120, 30))
        self.top.setMaximumSize(QSize(16777215, 30))
        self.top.setFrameShape(QFrame.StyledPanel)
        self.top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.top)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.explain_title = QLabel(self.top)
        self.explain_title.setObjectName(u"explain_title")
        self.explain_title.setMinimumSize(QSize(0, 20))
        self.explain_title.setMaximumSize(QSize(16777215, 20))
        self.explain_title.setStyleSheet(u"font: 700 italic 11pt \"Segoe UI\";color:rgb(255, 255, 255)")
        self.explain_title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.explain_title)

        self.min_sf = QPushButton(self.top)
        self.min_sf.setObjectName(u"min_sf")
        self.min_sf.setMinimumSize(QSize(20, 20))
        self.min_sf.setMaximumSize(QSize(20, 20))
        self.min_sf.setCursor(QCursor(Qt.PointingHandCursor))
        self.min_sf.setStyleSheet(u"QPushButton{\n"
"	border-image: url(:/all/img/min.png);\n"
"}")

        self.horizontalLayout_9.addWidget(self.min_sf)

        self.max_sf = QPushButton(self.top)
        self.max_sf.setObjectName(u"max_sf")
        self.max_sf.setMinimumSize(QSize(20, 20))
        self.max_sf.setMaximumSize(QSize(20, 20))
        self.max_sf.setCursor(QCursor(Qt.PointingHandCursor))
        self.max_sf.setStyleSheet(u"QPushButton{\n"
"	border-image: url(:/all/img/max.png);\n"
"}")

        self.horizontalLayout_9.addWidget(self.max_sf)

        self.close_button = QPushButton(self.top)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setMinimumSize(QSize(20, 20))
        self.close_button.setMaximumSize(QSize(20, 20))
        self.close_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_button.setStyleSheet(u"QPushButton{\n"
"	border-image: url(:/all/img/close.png);\n"
"}")

        self.horizontalLayout_9.addWidget(self.close_button)


        self.verticalLayout_13.addWidget(self.top)

        self.DetectContentBox = QFrame(self.ContentBox)
        self.DetectContentBox.setObjectName(u"DetectContentBox")
        self.DetectContentBox.setMaximumSize(QSize(16777215, 0))
        self.DetectContentBox.setStyleSheet(u"QFrame#DetectContentBox{\n"
"	background-color: rgb(245, 249, 254);\n"
"border:0px solid red;\n"
"border-radius:20px\n"
"}")
        self.DetectContentBox.setFrameShape(QFrame.StyledPanel)
        self.DetectContentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.DetectContentBox)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.detectContent = QFrame(self.DetectContentBox)
        self.detectContent.setObjectName(u"detectContent")
        self.detectContent.setMaximumSize(QSize(16777215, 16777215))
        self.detectContent.setFrameShape(QFrame.StyledPanel)
        self.detectContent.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.detectContent)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, 0, 0)
        self.main_content = QVBoxLayout()
        self.main_content.setSpacing(5)
        self.main_content.setObjectName(u"main_content")
        self.Content_Top = QFrame(self.detectContent)
        self.Content_Top.setObjectName(u"Content_Top")
        self.Content_Top.setMaximumSize(QSize(16777215, 40))
        self.Content_Top.setFrameShape(QFrame.StyledPanel)
        self.Content_Top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Content_Top)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.detect_char_label = QLabel(self.Content_Top)
        self.detect_char_label.setObjectName(u"detect_char_label")
        self.detect_char_label.setMinimumSize(QSize(0, 20))
        self.detect_char_label.setMaximumSize(QSize(16777215, 20))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.detect_char_label.setFont(font1)
        self.detect_char_label.setStyleSheet(u"padding-left:12px;")

        self.horizontalLayout.addWidget(self.detect_char_label)

        self.detect_set_button = QPushButton(self.Content_Top)
        self.detect_set_button.setObjectName(u"detect_set_button")
        sizePolicy.setHeightForWidth(self.detect_set_button.sizePolicy().hasHeightForWidth())
        self.detect_set_button.setSizePolicy(sizePolicy)
        self.detect_set_button.setMaximumSize(QSize(20, 50))
        self.detect_set_button.setStyleSheet(u"QPushButton{\n"
"	border-image: url(:/all/img/set.png);\n"
"}")

        self.horizontalLayout.addWidget(self.detect_set_button)


        self.main_content.addWidget(self.Content_Top)

        self.QF_Group = QFrame(self.detectContent)
        self.QF_Group.setObjectName(u"QF_Group")
        self.QF_Group.setMinimumSize(QSize(0, 100))
        self.QF_Group.setMaximumSize(QSize(16777215, 200))
        self.QF_Group.setStyleSheet(u"QFrame#QF_Group{\n"
"background-color: rgb(200, 242, 255);\n"
"border:2px solid rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"}")
        self.QF_Group.setFrameShape(QFrame.StyledPanel)
        self.QF_Group.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.QF_Group)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 9, -1, 15)
        self.select_button = QFrame(self.QF_Group)
        self.select_button.setObjectName(u"select_button")
        self.select_button.setMaximumSize(QSize(220, 16777215))
        self.select_button.setStyleSheet(u"background-color: rgb(206, 206, 255);")
        self.select_button.setFrameShape(QFrame.StyledPanel)
        self.select_button.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.select_button)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.src_cam_button = QPushButton(self.select_button)
        self.src_cam_button.setObjectName(u"src_cam_button")
        self.src_cam_button.setMinimumSize(QSize(0, 45))
        self.src_cam_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.src_cam_button.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/cam.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"background-color: rgb(100, 138, 255);\n"
"border: none;\n"
"border-left: 23px solid transparent;\n"
"\n"
"text-align: center;\n"
"padding-left: 0px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 12pt \"Nirmala UI\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(157, 200, 255);\n"
"}")

        self.verticalLayout_17.addWidget(self.src_cam_button)

        self.src_rtsp_button = QPushButton(self.select_button)
        self.src_rtsp_button.setObjectName(u"src_rtsp_button")
        self.src_rtsp_button.setMinimumSize(QSize(0, 45))
        self.src_rtsp_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.src_rtsp_button.setAutoFillBackground(False)
        self.src_rtsp_button.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/RTSP.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"background-color: rgb(100, 138, 255);\n"
"border: none;\n"
"border-left: 23px solid transparent;\n"
"\n"
"text-align: center;\n"
"padding-left: 0px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 12pt \"Nirmala UI\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(157, 200, 255);\n"
"}")
        self.src_rtsp_button.setIconSize(QSize(16, 16))

        self.verticalLayout_17.addWidget(self.src_rtsp_button)

        self.src_file_button = QPushButton(self.select_button)
        self.src_file_button.setObjectName(u"src_file_button")
        self.src_file_button.setMinimumSize(QSize(0, 45))
        self.src_file_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.src_file_button.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/file.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"background-color: rgb(100, 138, 255);\n"
"border: none;\n"
"border-left: 23px solid transparent;\n"
"\n"
"text-align: center;\n"
"padding-left: 0px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 12pt \"Nirmala UI\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(157, 200, 255);\n"
"}")

        self.verticalLayout_17.addWidget(self.src_file_button)


        self.horizontalLayout_3.addWidget(self.select_button)

        self.Class_QF = QFrame(self.QF_Group)
        self.Class_QF.setObjectName(u"Class_QF")
        self.Class_QF.setMinimumSize(QSize(170, 80))
        self.Class_QF.setMaximumSize(QSize(170, 80))
        self.Class_QF.setToolTipDuration(0)
        self.Class_QF.setStyleSheet(u"QFrame#Class_QF{\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"background-color: qradialgradient(cx:0, cy:0, radius:1, fx:0.1, fy:0.1, stop:0 rgb(162, 129, 247),  stop:1 rgb(119, 111, 252));\n"
"border: 1px outset rgb(98, 91, 213);\n"
"}\n"
"")
        self.Class_QF.setFrameShape(QFrame.StyledPanel)
        self.Class_QF.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.Class_QF)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.Class_top = QFrame(self.Class_QF)
        self.Class_top.setObjectName(u"Class_top")
        self.Class_top.setStyleSheet(u"border:none")
        self.Class_top.setFrameShape(QFrame.StyledPanel)
        self.Class_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.Class_top)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 3, 0, 3)
        self.class_label = QLabel(self.Class_top)
        self.class_label.setObjectName(u"class_label")
        self.class_label.setMaximumSize(QSize(16777215, 30))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setItalic(True)
        self.class_label.setFont(font2)
        self.class_label.setStyleSheet(u"color: rgba(255, 255, 255,210);\n"
"padding-left:12px;\n"
"font: 700 italic 16pt \"Segoe UI\";")
        self.class_label.setAlignment(Qt.AlignCenter)
        self.class_label.setIndent(0)

        self.horizontalLayout_6.addWidget(self.class_label)


        self.verticalLayout_7.addWidget(self.Class_top)

        self.class_line = QFrame(self.Class_QF)
        self.class_line.setObjectName(u"class_line")
        self.class_line.setMaximumSize(QSize(16777215, 1))
        self.class_line.setStyleSheet(u"background-color: rgba(255, 255, 255, 89);")
        self.class_line.setFrameShape(QFrame.HLine)
        self.class_line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_7.addWidget(self.class_line)

        self.Class_bottom = QFrame(self.Class_QF)
        self.Class_bottom.setObjectName(u"Class_bottom")
        self.Class_bottom.setStyleSheet(u"border:none")
        self.Class_bottom.setFrameShape(QFrame.StyledPanel)
        self.Class_bottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.Class_bottom)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 6, 0, 6)
        self.class_num = QLabel(self.Class_bottom)
        self.class_num.setObjectName(u"class_num")
        self.class_num.setMinimumSize(QSize(0, 30))
        self.class_num.setMaximumSize(QSize(16777215, 30))
        font3 = QFont()
        font3.setFamilies([u"Microsoft YaHei UI"])
        font3.setPointSize(17)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setUnderline(False)
        self.class_num.setFont(font3)
        self.class_num.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 17pt \"Microsoft YaHei UI\";")
        self.class_num.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.class_num, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.Class_bottom)

        self.verticalLayout_7.setStretch(1, 2)
        self.verticalLayout_7.setStretch(2, 1)

        self.horizontalLayout_3.addWidget(self.Class_QF)

        self.Target_QF = QFrame(self.QF_Group)
        self.Target_QF.setObjectName(u"Target_QF")
        self.Target_QF.setMinimumSize(QSize(170, 80))
        self.Target_QF.setMaximumSize(QSize(170, 80))
        self.Target_QF.setToolTipDuration(0)
        self.Target_QF.setStyleSheet(u"QFrame#Target_QF{\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"background-color: qradialgradient(cx:0, cy:0, radius:1, fx:0.1, fy:0.1, stop:0 rgb(253, 139, 133),  stop:1 rgb(248, 194, 152));\n"
"border: 1px outset rgb(252, 194, 149)\n"
"}\n"
"")
        self.Target_QF.setFrameShape(QFrame.StyledPanel)
        self.Target_QF.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.Target_QF)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.Target_top = QFrame(self.Target_QF)
        self.Target_top.setObjectName(u"Target_top")
        self.Target_top.setStyleSheet(u"border:none")
        self.Target_top.setFrameShape(QFrame.StyledPanel)
        self.Target_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.Target_top)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 3, 0, 3)
        self.target_label = QLabel(self.Target_top)
        self.target_label.setObjectName(u"target_label")
        self.target_label.setMaximumSize(QSize(16777215, 30))
        self.target_label.setFont(font2)
        self.target_label.setStyleSheet(u"color: rgba(255, 255, 255,210);\n"
"padding-left:12px;\n"
"font: 700 italic 16pt \"Segoe UI\";")
        self.target_label.setAlignment(Qt.AlignCenter)
        self.target_label.setIndent(0)

        self.horizontalLayout_7.addWidget(self.target_label)


        self.verticalLayout_9.addWidget(self.Target_top)

        self.target_line = QFrame(self.Target_QF)
        self.target_line.setObjectName(u"target_line")
        self.target_line.setMaximumSize(QSize(16777215, 1))
        self.target_line.setStyleSheet(u"background-color: rgba(255, 255, 255, 89);")
        self.target_line.setFrameShape(QFrame.HLine)
        self.target_line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_9.addWidget(self.target_line)

        self.Target_bottom = QFrame(self.Target_QF)
        self.Target_bottom.setObjectName(u"Target_bottom")
        self.Target_bottom.setStyleSheet(u"border:none")
        self.Target_bottom.setFrameShape(QFrame.StyledPanel)
        self.Target_bottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.Target_bottom)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 6, 0, 6)
        self.target_num = QLabel(self.Target_bottom)
        self.target_num.setObjectName(u"target_num")
        self.target_num.setMinimumSize(QSize(0, 30))
        self.target_num.setMaximumSize(QSize(16777215, 30))
        self.target_num.setFont(font3)
        self.target_num.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 17pt \"Microsoft YaHei UI\";")
        self.target_num.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.target_num, 0, Qt.AlignTop)


        self.verticalLayout_9.addWidget(self.Target_bottom)

        self.verticalLayout_9.setStretch(1, 2)
        self.verticalLayout_9.setStretch(2, 1)

        self.horizontalLayout_3.addWidget(self.Target_QF)

        self.Fps_QF = QFrame(self.QF_Group)
        self.Fps_QF.setObjectName(u"Fps_QF")
        self.Fps_QF.setMinimumSize(QSize(170, 80))
        self.Fps_QF.setMaximumSize(QSize(170, 80))
        self.Fps_QF.setToolTipDuration(0)
        self.Fps_QF.setStyleSheet(u"QFrame#Fps_QF{\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"background-color: qradialgradient(cx:0, cy:0, radius:1, fx:0.1, fy:0.1, stop:0 rgb(243, 175, 189),  stop:1 rgb(155, 118, 218));\n"
"border: 1px outset rgb(153, 117, 219)\n"
"}\n"
"")
        self.Fps_QF.setFrameShape(QFrame.StyledPanel)
        self.Fps_QF.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.Fps_QF)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.Fps_top = QFrame(self.Fps_QF)
        self.Fps_top.setObjectName(u"Fps_top")
        self.Fps_top.setStyleSheet(u"border:none")
        self.Fps_top.setFrameShape(QFrame.StyledPanel)
        self.Fps_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.Fps_top)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 3, 7, 3)
        self.fps_label = QLabel(self.Fps_top)
        self.fps_label.setObjectName(u"fps_label")
        self.fps_label.setMaximumSize(QSize(16777215, 30))
        self.fps_label.setFont(font2)
        self.fps_label.setStyleSheet(u"color: rgba(255, 255, 255,210);\n"
"padding-left:12px;\n"
"font: 700 italic 16pt \"Segoe UI\";")
        self.fps_label.setMidLineWidth(-1)
        self.fps_label.setAlignment(Qt.AlignCenter)
        self.fps_label.setWordWrap(False)
        self.fps_label.setIndent(0)

        self.horizontalLayout_8.addWidget(self.fps_label)


        self.verticalLayout_11.addWidget(self.Fps_top)

        self.fps_line = QFrame(self.Fps_QF)
        self.fps_line.setObjectName(u"fps_line")
        self.fps_line.setMaximumSize(QSize(16777215, 1))
        self.fps_line.setStyleSheet(u"background-color: rgba(255, 255, 255, 89);")
        self.fps_line.setFrameShape(QFrame.HLine)
        self.fps_line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_11.addWidget(self.fps_line)

        self.Fps_bottom = QFrame(self.Fps_QF)
        self.Fps_bottom.setObjectName(u"Fps_bottom")
        self.Fps_bottom.setStyleSheet(u"border:none")
        self.Fps_bottom.setFrameShape(QFrame.StyledPanel)
        self.Fps_bottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.Fps_bottom)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 6, 0, 6)
        self.fps_num = QLabel(self.Fps_bottom)
        self.fps_num.setObjectName(u"fps_num")
        self.fps_num.setMinimumSize(QSize(0, 30))
        self.fps_num.setMaximumSize(QSize(16777215, 30))
        self.fps_num.setFont(font3)
        self.fps_num.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 17pt \"Microsoft YaHei UI\";")
        self.fps_num.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.fps_num, 0, Qt.AlignTop)


        self.verticalLayout_11.addWidget(self.Fps_bottom)

        self.verticalLayout_11.setStretch(1, 2)
        self.verticalLayout_11.setStretch(2, 1)

        self.horizontalLayout_3.addWidget(self.Fps_QF)


        self.main_content.addWidget(self.QF_Group)

        self.Result_QF = QFrame(self.detectContent)
        self.Result_QF.setObjectName(u"Result_QF")
        self.Result_QF.setStyleSheet(u"")
        self.Result_QF.setFrameShape(QFrame.StyledPanel)
        self.Result_QF.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.Result_QF)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(self.Result_QF)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setStyleSheet(u"#splitter::handle{background: 1px solid  rgba(200, 200, 200,100);}")
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setHandleWidth(2)
        self.pre_video = QLabel(self.splitter)
        self.pre_video.setObjectName(u"pre_video")
        self.pre_video.setMinimumSize(QSize(200, 100))
        self.pre_video.setStyleSheet(u"background-color: rgb(200, 242, 255);\n"
"border:2px solid rgb(255, 255, 255);\n"
"border-radius:15px")
        self.pre_video.setAlignment(Qt.AlignCenter)
        self.splitter.addWidget(self.pre_video)
        self.res_video = QLabel(self.splitter)
        self.res_video.setObjectName(u"res_video")
        self.res_video.setMinimumSize(QSize(200, 100))
        self.res_video.setStyleSheet(u"background-color: rgb(200, 242, 255);\n"
"border:2px solid rgb(255, 255, 255);\n"
"border-radius:15px")
        self.res_video.setAlignment(Qt.AlignCenter)
        self.splitter.addWidget(self.res_video)

        self.verticalLayout_16.addWidget(self.splitter)


        self.main_content.addWidget(self.Result_QF)

        self.Pause_QF = QFrame(self.detectContent)
        self.Pause_QF.setObjectName(u"Pause_QF")
        self.Pause_QF.setMinimumSize(QSize(0, 30))
        self.Pause_QF.setMaximumSize(QSize(16777215, 30))
        self.Pause_QF.setFrameShape(QFrame.StyledPanel)
        self.Pause_QF.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.Pause_QF)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 3, 0)
        self.run_button = QPushButton(self.Pause_QF)
        self.run_button.setObjectName(u"run_button")
        self.run_button.setMinimumSize(QSize(0, 30))
        self.run_button.setMaximumSize(QSize(16777215, 30))
        self.run_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.run_button.setMouseTracking(True)
        self.run_button.setStyleSheet(u"QPushButton{\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"border: none;\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/all/img/begin.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/all/img/pause.png", QSize(), QIcon.Normal, QIcon.On)
        self.run_button.setIcon(icon1)
        self.run_button.setIconSize(QSize(30, 30))
        self.run_button.setCheckable(True)
        self.run_button.setChecked(False)

        self.horizontalLayout_4.addWidget(self.run_button)

        self.progress_bar = QProgressBar(self.Pause_QF)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setMinimumSize(QSize(0, 20))
        self.progress_bar.setMaximumSize(QSize(16777215, 20))
        self.progress_bar.setStyleSheet(u"QProgressBar{ \n"
"font: 700 10pt \"Microsoft YaHei UI\";\n"
"color: rgb(253, 143, 134); \n"
"text-align:center; \n"
"border:3px solid rgb(255, 255, 255);\n"
"border-radius: 10px; \n"
"background-color: rgba(215, 215, 215,100);\n"
"} \n"
"\n"
"QProgressBar:chunk{ \n"
"border-radius:0px; \n"
"background: rgba(119, 111, 252, 200);\n"
"border-radius: 7px;\n"
"}")
        self.progress_bar.setMaximum(1000)
        self.progress_bar.setValue(0)

        self.horizontalLayout_4.addWidget(self.progress_bar)

        self.stop_button = QPushButton(self.Pause_QF)
        self.stop_button.setObjectName(u"stop_button")
        self.stop_button.setMinimumSize(QSize(0, 30))
        self.stop_button.setMaximumSize(QSize(16777215, 30))
        self.stop_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.stop_button.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/stop.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"}")

        self.horizontalLayout_4.addWidget(self.stop_button)


        self.main_content.addWidget(self.Pause_QF)


        self.horizontalLayout_5.addLayout(self.main_content)

        self.prm_page = QFrame(self.detectContent)
        self.prm_page.setObjectName(u"prm_page")
        self.prm_page.setMinimumSize(QSize(220, 0))
        self.prm_page.setMaximumSize(QSize(0, 16777215))
        self.prm_page.setStyleSheet(u"QFrame#prm_page{\n"
"background-color: qradialgradient(cx:0, cy:0, radius:1, fx:0.1, fy:0.1, stop:0 rgb(243, 175, 189),  stop:1 rgb(155, 118, 218));\n"
"border-top-left-radius:30px;\n"
"border-top-right-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"border-bottom-left-radius:30px;\n"
"}")
        self.prm_page.setFrameShape(QFrame.StyledPanel)
        self.prm_page.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.prm_page)
        self.verticalLayout_22.setSpacing(15)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(15, 15, -1, -1)
        self.setting_label = QLabel(self.prm_page)
        self.setting_label.setObjectName(u"setting_label")
        self.setting_label.setStyleSheet(u"padding-left: 0px;\n"
"padding-bottom: 2px;\n"
"color: rgba(255, 255, 255, 240);\n"
"font: 700 italic 16pt \"Segoe UI\";")
        self.setting_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.setting_label)

        self.Model_QF = QWidget(self.prm_page)
        self.Model_QF.setObjectName(u"Model_QF")
        self.Model_QF.setMinimumSize(QSize(190, 90))
        self.Model_QF.setMaximumSize(QSize(190, 90))
        self.Model_QF.setStyleSheet(u"QWidget#Model_QF{\n"
"border:2px solid rgba(255, 255, 255, 70);\n"
"border-radius:15px;\n"
"}")
        self.verticalLayout_21 = QVBoxLayout(self.Model_QF)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(9, 9, 9, 9)
        self.ToggleBotton_6 = QPushButton(self.Model_QF)
        self.ToggleBotton_6.setObjectName(u"ToggleBotton_6")
        sizePolicy1.setHeightForWidth(self.ToggleBotton_6.sizePolicy().hasHeightForWidth())
        self.ToggleBotton_6.setSizePolicy(sizePolicy1)
        self.ToggleBotton_6.setMinimumSize(QSize(0, 30))
        self.ToggleBotton_6.setMaximumSize(QSize(16777215, 30))
        font4 = QFont()
        font4.setFamilies([u"Nirmala UI"])
        font4.setPointSize(13)
        font4.setBold(True)
        font4.setItalic(False)
        self.ToggleBotton_6.setFont(font4)
        self.ToggleBotton_6.setCursor(QCursor(Qt.ArrowCursor))
        self.ToggleBotton_6.setMouseTracking(True)
        self.ToggleBotton_6.setFocusPolicy(Qt.StrongFocus)
        self.ToggleBotton_6.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.ToggleBotton_6.setLayoutDirection(Qt.LeftToRight)
        self.ToggleBotton_6.setAutoFillBackground(False)
        self.ToggleBotton_6.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/model.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 20px solid transparent;\n"
"\n"
"text-align: left;\n"
"padding-left: 40px;\n"
"padding-bottom: 2px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 13pt \"Nirmala UI\";\n"
"}")
        self.ToggleBotton_6.setIcon(icon)
        self.ToggleBotton_6.setAutoDefault(False)
        self.ToggleBotton_6.setFlat(False)

        self.verticalLayout_21.addWidget(self.ToggleBotton_6)

        self.model_box = QComboBox(self.Model_QF)
        self.model_box.setObjectName(u"model_box")
        self.model_box.setMinimumSize(QSize(170, 20))
        self.model_box.setMaximumSize(QSize(170, 20))
        self.model_box.setStyleSheet(u"\n"
"QComboBox {\n"
"            background-color: rgba(255,255,255,90);\n"
"			color: rgba(0, 0, 0, 200);\n"
"			font: 600 9pt \"Segoe UI\";\n"
"            border: 1px solid lightgray;\n"
"            border-radius: 10px;\n"
"            padding-left: 15px;\n"
"        }\n"
"        \n"
"        QComboBox:on {\n"
"            border: 1px solid #63acfb;\n"
"        }\n"
"\n"
"        QComboBox::drop-down {\n"
"            width: 22px;\n"
"            border-left: 1px solid lightgray;\n"
"            border-top-right-radius: 15px;\n"
"            border-bottom-right-radius: 15px;\n"
"        }\n"
"        \n"
"        QComboBox::drop-down:on {\n"
"            border-left: 1px solid #63acfb;\n"
"        }\n"
"\n"
"        QComboBox::down-arrow {\n"
"            width: 16px;\n"
"            height: 16px;\n"
"            image: url(:/all/img/box_down.png);\n"
"        }\n"
"\n"
"        QComboBox::down-arrow:on {\n"
"            image: url(:/all/img/box_up.png);\n"
"        }\n"
"\n"
"        QComboBox QAbstractI"
                        "temView {\n"
"            border: none;\n"
"            outline: none;\n"
"			padding: 10px;\n"
"            background-color: rgb(223, 188, 220);\n"
"        }\n"
"\n"
"\n"
"        QComboBox QScrollBar:vertical {\n"
"            width: 2px;\n"
"           background-color: rgba(255,255,255,150);\n"
"        }\n"
"\n"
"        QComboBox QScrollBar::handle:vertical {\n"
"            background-color: rgba(255,255,255,90);\n"
"        }")
        self.model_box.setInsertPolicy(QComboBox.NoInsert)
        self.model_box.setMinimumContentsLength(0)

        self.verticalLayout_21.addWidget(self.model_box)


        self.verticalLayout_22.addWidget(self.Model_QF)

        self.IOU_QF = QFrame(self.prm_page)
        self.IOU_QF.setObjectName(u"IOU_QF")
        self.IOU_QF.setMinimumSize(QSize(190, 90))
        self.IOU_QF.setMaximumSize(QSize(190, 90))
        self.IOU_QF.setStyleSheet(u"QFrame#IOU_QF{\n"
"border:2px solid rgba(255, 255, 255, 70);\n"
"border-radius:15px;\n"
"}")
        self.verticalLayout_15 = QVBoxLayout(self.IOU_QF)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.ToggleBotton_2 = QPushButton(self.IOU_QF)
        self.ToggleBotton_2.setObjectName(u"ToggleBotton_2")
        sizePolicy1.setHeightForWidth(self.ToggleBotton_2.sizePolicy().hasHeightForWidth())
        self.ToggleBotton_2.setSizePolicy(sizePolicy1)
        self.ToggleBotton_2.setMinimumSize(QSize(0, 30))
        self.ToggleBotton_2.setMaximumSize(QSize(16777215, 30))
        self.ToggleBotton_2.setFont(font4)
        self.ToggleBotton_2.setCursor(QCursor(Qt.ArrowCursor))
        self.ToggleBotton_2.setMouseTracking(True)
        self.ToggleBotton_2.setFocusPolicy(Qt.StrongFocus)
        self.ToggleBotton_2.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.ToggleBotton_2.setLayoutDirection(Qt.LeftToRight)
        self.ToggleBotton_2.setAutoFillBackground(False)
        self.ToggleBotton_2.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/IOU.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 20px solid transparent;\n"
"\n"
"text-align: left;\n"
"padding-left: 40px;\n"
"padding-bottom: 4px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 13pt \"Nirmala UI\";\n"
"}")
        self.ToggleBotton_2.setIcon(icon)
        self.ToggleBotton_2.setAutoDefault(False)
        self.ToggleBotton_2.setFlat(False)

        self.verticalLayout_15.addWidget(self.ToggleBotton_2)

        self.frame_3 = QFrame(self.IOU_QF)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QSize(0, 20))
        self.frame_3.setMaximumSize(QSize(16777215, 20))
        self.horizontalLayout_10 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(8, 0, 10, 0)
        self.iou_spinbox = QDoubleSpinBox(self.frame_3)
        self.iou_spinbox.setObjectName(u"iou_spinbox")
        self.iou_spinbox.setCursor(QCursor(Qt.PointingHandCursor))
        self.iou_spinbox.setStyleSheet(u"QDoubleSpinBox {\n"
"border: 0px solid lightgray;\n"
"border-radius: 2px;\n"
"background-color: rgba(255,255,255,90);\n"
"font: 600 9pt \"Segoe UI\";\n"
"}\n"
"        \n"
"QDoubleSpinBox::up-button {\n"
"width: 10px;\n"
"height: 9px;\n"
"margin: 0px 3px 0px 0px;\n"
"border-image: url(:/all/img/box_up.png);\n"
"}\n"
"QDoubleSpinBox::up-button:pressed {\n"
"margin-top: 1px;\n"
"}\n"
"            \n"
"QDoubleSpinBox::down-button {\n"
"width: 10px;\n"
"height: 9px;\n"
"margin: 0px 3px 0px 0px;\n"
"border-image: url(:/all/img/box_down.png);\n"
"}\n"
"QDoubleSpinBox::down-button:pressed {\n"
"margin-bottom: 1px;\n"
"}")
        self.iou_spinbox.setMinimum(0.010000000000000)
        self.iou_spinbox.setMaximum(1.000000000000000)
        self.iou_spinbox.setSingleStep(0.050000000000000)
        self.iou_spinbox.setValue(0.450000000000000)

        self.horizontalLayout_10.addWidget(self.iou_spinbox)

        self.iou_slider = QSlider(self.frame_3)
        self.iou_slider.setObjectName(u"iou_slider")
        self.iou_slider.setCursor(QCursor(Qt.PointingHandCursor))
        self.iou_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"border: none;\n"
"height: 10px;\n"
"background-color: rgba(255,255,255,90);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"width: 10px;\n"
"margin: -1px 0px -1px 0px;\n"
"border-radius: 3px;\n"
"background-color: white;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #59969b, stop:1 #04e7fa);\n"
"border-radius: 5px;\n"
"}")
        self.iou_slider.setMinimum(1)
        self.iou_slider.setMaximum(100)
        self.iou_slider.setValue(45)
        self.iou_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_10.addWidget(self.iou_slider)


        self.verticalLayout_15.addWidget(self.frame_3)


        self.verticalLayout_22.addWidget(self.IOU_QF)

        self.Conf_QF = QFrame(self.prm_page)
        self.Conf_QF.setObjectName(u"Conf_QF")
        self.Conf_QF.setMinimumSize(QSize(190, 90))
        self.Conf_QF.setMaximumSize(QSize(190, 90))
        self.Conf_QF.setStyleSheet(u"QFrame#Conf_QF{\n"
"border:2px solid rgba(255, 255, 255, 70);\n"
"border-radius:15px;\n"
"}")
        self.verticalLayout_18 = QVBoxLayout(self.Conf_QF)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.ToggleBotton_3 = QPushButton(self.Conf_QF)
        self.ToggleBotton_3.setObjectName(u"ToggleBotton_3")
        sizePolicy1.setHeightForWidth(self.ToggleBotton_3.sizePolicy().hasHeightForWidth())
        self.ToggleBotton_3.setSizePolicy(sizePolicy1)
        self.ToggleBotton_3.setMinimumSize(QSize(0, 30))
        self.ToggleBotton_3.setMaximumSize(QSize(16777215, 30))
        self.ToggleBotton_3.setFont(font4)
        self.ToggleBotton_3.setCursor(QCursor(Qt.ArrowCursor))
        self.ToggleBotton_3.setMouseTracking(True)
        self.ToggleBotton_3.setFocusPolicy(Qt.StrongFocus)
        self.ToggleBotton_3.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.ToggleBotton_3.setLayoutDirection(Qt.LeftToRight)
        self.ToggleBotton_3.setAutoFillBackground(False)
        self.ToggleBotton_3.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/conf.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 20px solid transparent;\n"
"\n"
"text-align: left;\n"
"padding-left: 40px;\n"
"padding-bottom: 4px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 13pt \"Nirmala UI\";\n"
"}")
        self.ToggleBotton_3.setIcon(icon)
        self.ToggleBotton_3.setAutoDefault(False)
        self.ToggleBotton_3.setFlat(False)

        self.verticalLayout_18.addWidget(self.ToggleBotton_3)

        self.frame = QFrame(self.Conf_QF)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(0, 20))
        self.frame.setMaximumSize(QSize(16777215, 20))
        self.horizontalLayout_11 = QHBoxLayout(self.frame)
        self.horizontalLayout_11.setSpacing(10)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(8, 0, 10, 0)
        self.conf_spinbox = QDoubleSpinBox(self.frame)
        self.conf_spinbox.setObjectName(u"conf_spinbox")
        self.conf_spinbox.setCursor(QCursor(Qt.PointingHandCursor))
        self.conf_spinbox.setStyleSheet(u"QDoubleSpinBox {\n"
"border: 0px solid lightgray;\n"
"border-radius: 2px;\n"
"background-color: rgba(255,255,255,90);\n"
"font: 600 9pt \"Segoe UI\";\n"
"}\n"
"        \n"
"QDoubleSpinBox::up-button {\n"
"width: 10px;\n"
"height: 9px;\n"
"margin: 0px 3px 0px 0px;\n"
"border-image: url(:/all/img/box_up.png);\n"
"}\n"
"QDoubleSpinBox::up-button:pressed {\n"
"margin-top: 1px;\n"
"}\n"
"            \n"
"QDoubleSpinBox::down-button {\n"
"width: 10px;\n"
"height: 9px;\n"
"margin: 0px 3px 0px 0px;\n"
"border-image: url(:/all/img/box_down.png);\n"
"}\n"
"QDoubleSpinBox::down-button:pressed {\n"
"margin-bottom: 1px;\n"
"}")
        self.conf_spinbox.setMinimum(0.010000000000000)
        self.conf_spinbox.setMaximum(1.000000000000000)
        self.conf_spinbox.setSingleStep(0.050000000000000)
        self.conf_spinbox.setValue(0.250000000000000)

        self.horizontalLayout_11.addWidget(self.conf_spinbox)

        self.conf_slider = QSlider(self.frame)
        self.conf_slider.setObjectName(u"conf_slider")
        self.conf_slider.setCursor(QCursor(Qt.PointingHandCursor))
        self.conf_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"border: none;\n"
"height: 10px;\n"
"background-color: rgba(255,255,255,90);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"width: 10px;\n"
"margin: -1px 0px -1px 0px;\n"
"border-radius: 3px;\n"
"background-color: white;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #59969b, stop:1 #04e7fa);\n"
"border-radius: 5px;\n"
"}")
        self.conf_slider.setMinimum(1)
        self.conf_slider.setMaximum(100)
        self.conf_slider.setValue(25)
        self.conf_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_11.addWidget(self.conf_slider)


        self.verticalLayout_18.addWidget(self.frame)


        self.verticalLayout_22.addWidget(self.Conf_QF)

        self.Delay_QF = QFrame(self.prm_page)
        self.Delay_QF.setObjectName(u"Delay_QF")
        self.Delay_QF.setMinimumSize(QSize(190, 90))
        self.Delay_QF.setMaximumSize(QSize(190, 90))
        self.Delay_QF.setStyleSheet(u"QFrame#Delay_QF{\n"
"border:2px solid rgba(255, 255, 255, 70);\n"
"border-radius:15px;\n"
"}")
        self.verticalLayout_19 = QVBoxLayout(self.Delay_QF)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.ToggleBotton_4 = QPushButton(self.Delay_QF)
        self.ToggleBotton_4.setObjectName(u"ToggleBotton_4")
        sizePolicy1.setHeightForWidth(self.ToggleBotton_4.sizePolicy().hasHeightForWidth())
        self.ToggleBotton_4.setSizePolicy(sizePolicy1)
        self.ToggleBotton_4.setMinimumSize(QSize(0, 30))
        self.ToggleBotton_4.setMaximumSize(QSize(16777215, 30))
        self.ToggleBotton_4.setFont(font4)
        self.ToggleBotton_4.setCursor(QCursor(Qt.ArrowCursor))
        self.ToggleBotton_4.setMouseTracking(True)
        self.ToggleBotton_4.setFocusPolicy(Qt.StrongFocus)
        self.ToggleBotton_4.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.ToggleBotton_4.setLayoutDirection(Qt.LeftToRight)
        self.ToggleBotton_4.setAutoFillBackground(False)
        self.ToggleBotton_4.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/delay.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 20px solid transparent;\n"
"\n"
"text-align: left;\n"
"padding-left: 40px;\n"
"padding-bottom: 2px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 13pt \"Nirmala UI\";\n"
"}")
        self.ToggleBotton_4.setIcon(icon)
        self.ToggleBotton_4.setAutoDefault(False)
        self.ToggleBotton_4.setFlat(False)

        self.verticalLayout_19.addWidget(self.ToggleBotton_4)

        self.frame_2 = QFrame(self.Delay_QF)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(0, 20))
        self.frame_2.setMaximumSize(QSize(16777215, 20))
        self.horizontalLayout_12 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_12.setSpacing(10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(8, 0, 10, 0)
        self.speed_spinbox = QSpinBox(self.frame_2)
        self.speed_spinbox.setObjectName(u"speed_spinbox")
        self.speed_spinbox.setStyleSheet(u"QSpinBox {\n"
"border: 0px solid lightgray;\n"
"border-radius: 2px;\n"
"background-color: rgba(255,255,255,90);\n"
"font: 600 9pt \"Segoe UI\";\n"
"}\n"
"        \n"
"QSpinBox::up-button {\n"
"width: 10px;\n"
"height: 9px;\n"
"margin: 0px 3px 0px 0px;\n"
"border-image: url(:/all/img/box_up.png);\n"
"}\n"
"QSpinBox::up-button:pressed {\n"
"margin-top: 1px;\n"
"}\n"
"            \n"
"QSpinBox::down-button {\n"
"width: 10px;\n"
"height: 9px;\n"
"margin: 0px 3px 0px 0px;\n"
"border-image: url(:/all/img/box_down.png);\n"
"}\n"
"QSpinBox::down-button:pressed {\n"
"margin-bottom: 1px;\n"
"}")
        self.speed_spinbox.setMaximum(50)
        self.speed_spinbox.setValue(10)

        self.horizontalLayout_12.addWidget(self.speed_spinbox)

        self.speed_slider = QSlider(self.frame_2)
        self.speed_slider.setObjectName(u"speed_slider")
        self.speed_slider.setCursor(QCursor(Qt.PointingHandCursor))
        self.speed_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"border: none;\n"
"height: 10px;\n"
"background-color: rgba(255,255,255,90);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"width: 10px;\n"
"margin: -1px 0px -1px 0px;\n"
"border-radius: 3px;\n"
"background-color: white;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background-color: qradialgradient(cx:0, cy:0, radius:1, fx:0.1, fy:0.1, stop:0 rgb(253, 139, 133),  stop:1 rgb(248, 194, 152));\n"
"border-radius: 5px;\n"
"}")
        self.speed_slider.setMaximum(50)
        self.speed_slider.setValue(10)
        self.speed_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_12.addWidget(self.speed_slider)


        self.verticalLayout_19.addWidget(self.frame_2)


        self.verticalLayout_22.addWidget(self.Delay_QF)

        self.Save_QF = QFrame(self.prm_page)
        self.Save_QF.setObjectName(u"Save_QF")
        self.Save_QF.setMinimumSize(QSize(190, 120))
        self.Save_QF.setMaximumSize(QSize(190, 120))
        self.Save_QF.setStyleSheet(u"QFrame#Save_QF{\n"
"border:2px solid rgba(255, 255, 255, 70);\n"
"border-radius:15px;\n"
"}")
        self.verticalLayout_20 = QVBoxLayout(self.Save_QF)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(9, 9, 9, 9)
        self.ToggleBotton_5 = QPushButton(self.Save_QF)
        self.ToggleBotton_5.setObjectName(u"ToggleBotton_5")
        sizePolicy1.setHeightForWidth(self.ToggleBotton_5.sizePolicy().hasHeightForWidth())
        self.ToggleBotton_5.setSizePolicy(sizePolicy1)
        self.ToggleBotton_5.setMinimumSize(QSize(0, 30))
        self.ToggleBotton_5.setMaximumSize(QSize(16777215, 30))
        self.ToggleBotton_5.setFont(font4)
        self.ToggleBotton_5.setCursor(QCursor(Qt.ArrowCursor))
        self.ToggleBotton_5.setMouseTracking(True)
        self.ToggleBotton_5.setFocusPolicy(Qt.StrongFocus)
        self.ToggleBotton_5.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.ToggleBotton_5.setLayoutDirection(Qt.LeftToRight)
        self.ToggleBotton_5.setAutoFillBackground(False)
        self.ToggleBotton_5.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/save.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 20px solid transparent;\n"
"\n"
"text-align: left;\n"
"padding-left: 40px;\n"
"padding-bottom: 2px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 13pt \"Nirmala UI\";\n"
"}")
        self.ToggleBotton_5.setIcon(icon)
        self.ToggleBotton_5.setAutoDefault(False)
        self.ToggleBotton_5.setFlat(False)

        self.verticalLayout_20.addWidget(self.ToggleBotton_5)

        self.save_res_button = QCheckBox(self.Save_QF)
        self.save_res_button.setObjectName(u"save_res_button")
        self.save_res_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.save_res_button.setStyleSheet(u"QCheckBox {\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 590 10pt \"Nirmala UI\";\n"
"        }\n"
"\n"
"        QCheckBox::indicator {\n"
"            padding-top: 1px;\n"
"padding-left: 10px;\n"
"            width: 40px;\n"
"            height: 30px;\n"
"            border: none;\n"
"        }\n"
"\n"
"        QCheckBox::indicator:unchecked {\n"
"            image: url(:/all/img/check_no.png);\n"
"        }\n"
"\n"
"        QCheckBox::indicator:checked {\n"
"            image: url(:/all/img/check_yes.png);\n"
"        }")

        self.verticalLayout_20.addWidget(self.save_res_button)

        self.save_txt_button = QCheckBox(self.Save_QF)
        self.save_txt_button.setObjectName(u"save_txt_button")
        self.save_txt_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.save_txt_button.setStyleSheet(u"QCheckBox {\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 590 10pt \"Nirmala UI\";\n"
"        }\n"
"\n"
"        QCheckBox::indicator {\n"
"            padding-top: 1px;\n"
"padding-left: 10px;\n"
"            width: 40px;\n"
"            height: 30px;\n"
"            border: none;\n"
"        }\n"
"\n"
"        QCheckBox::indicator:unchecked {\n"
"            image: url(:/all/img/check_no.png);\n"
"        }\n"
"\n"
"        QCheckBox::indicator:checked {\n"
"            image: url(:/all/img/check_yes.png);\n"
"        }")

        self.verticalLayout_20.addWidget(self.save_txt_button)


        self.verticalLayout_22.addWidget(self.Save_QF)

        self.setting_verticalSpacer = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_22.addItem(self.setting_verticalSpacer)


        self.horizontalLayout_5.addWidget(self.prm_page)


        self.verticalLayout_6.addWidget(self.detectContent)

        self.below = QFrame(self.DetectContentBox)
        self.below.setObjectName(u"below")
        self.below.setMinimumSize(QSize(0, 30))
        self.below.setMaximumSize(QSize(16777215, 30))
        self.below.setFrameShape(QFrame.StyledPanel)
        self.below.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.below)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.status_bar = QLabel(self.below)
        self.status_bar.setObjectName(u"status_bar")
        self.status_bar.setMinimumSize(QSize(0, 20))
        self.status_bar.setStyleSheet(u"font: 700 11pt \"Segoe UI\";\n"
"color: rgba(0, 0, 0, 140);")

        self.verticalLayout_14.addWidget(self.status_bar)

        self.frame_size_grip = QFrame(self.below)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setStyleSheet(u"border-radius:30px;")
        self.frame_size_grip.setFrameShape(QFrame.StyledPanel)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.verticalLayout_14.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.below)


        self.verticalLayout_13.addWidget(self.DetectContentBox)

        self.HomePage = QFrame(self.ContentBox)
        self.HomePage.setObjectName(u"HomePage")
        sizePolicy.setHeightForWidth(self.HomePage.sizePolicy().hasHeightForWidth())
        self.HomePage.setSizePolicy(sizePolicy)
        self.HomePage.setMaximumSize(QSize(16777215, 16777215))
        self.HomePage.setAutoFillBackground(False)
        self.HomePage.setStyleSheet(u"QFrame#HomePage{\n"
"	background-color: rgb(245, 249, 254);\n"
"border:0px solid red;\n"
"border-radius:20px\n"
"}")
        self.HomePage.setFrameShape(QFrame.StyledPanel)
        self.HomePage.setFrameShadow(QFrame.Raised)
        self.verticalLayout_126 = QVBoxLayout(self.HomePage)
        self.verticalLayout_126.setObjectName(u"verticalLayout_126")
        self.home = QFrame(self.HomePage)
        self.home.setObjectName(u"home")
        self.home.setMinimumSize(QSize(0, 30))
        self.home.setMaximumSize(QSize(16777215, 30))
        self.home.setStyleSheet(u"QFrame#top{\n"
"background-color: rgba(255, 255, 255,0);\n"
"}")
        self.home.setFrameShape(QFrame.StyledPanel)
        self.home.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_85 = QHBoxLayout(self.home)
        self.horizontalLayout_85.setSpacing(0)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.horizontalLayout_85.setContentsMargins(20, 0, -1, 0)
        self.explain = QLabel(self.home)
        self.explain.setObjectName(u"explain")
        self.explain.setMinimumSize(QSize(0, 30))
        self.explain.setMaximumSize(QSize(16777215, 30))
        self.explain.setStyleSheet(u"font: 700 italic 11pt \"Segoe UI\";")
        self.explain.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_85.addWidget(self.explain)


        self.verticalLayout_126.addWidget(self.home)


        self.verticalLayout_13.addWidget(self.HomePage)

        self.TaskRecordContentBox = QFrame(self.ContentBox)
        self.TaskRecordContentBox.setObjectName(u"TaskRecordContentBox")
        self.TaskRecordContentBox.setMaximumSize(QSize(16777215, 0))
        self.TaskRecordContentBox.setStyleSheet(u"QFrame#TaskRecordContentBox{\n"
                                                "	background-color: rgb(245, 249, 254);\n"
                                                "border:0px solid red;\n"
                                                "border-radius:20px\n"
                                                "}")
        self.TaskRecordContentBox.setFrameShape(QFrame.StyledPanel)
        self.TaskRecordContentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_96 = QVBoxLayout(self.TaskRecordContentBox)
        self.verticalLayout_96.setObjectName(u"verticalLayout_96")
        self.TaskRecordContent = QFrame(self.TaskRecordContentBox)
        self.TaskRecordContent.setObjectName(u"TaskRecordContent")
        self.TaskRecordContent.setMaximumSize(QSize(16777215, 16777215))
        self.TaskRecordContent.setFrameShape(QFrame.StyledPanel)
        self.TaskRecordContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_97 = QVBoxLayout(self.TaskRecordContent)
        self.verticalLayout_97.setObjectName(u"verticalLayout_97")
        self.verticalLayout_97.setContentsMargins(-1, 0, -1, -1)
        self.widget_2 = QWidget(self.TaskRecordContent)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_98 = QVBoxLayout(self.widget_2)
        self.verticalLayout_98.setObjectName(u"verticalLayout_98")
        self.verticalLayout_98.setContentsMargins(-1, 0, -1, -1)
        self.horizontalWidget_2 = QWidget(self.widget_2)
        self.horizontalWidget_2.setObjectName(u"horizontalWidget_2")
        self.horizontalWidget_2.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_25 = QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalSpacer_4 = QSpacerItem(16777215, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(self.horizontalSpacer_4)
        self.label_3 = QLabel(self.horizontalWidget_2)
        self.label_3.setObjectName(u"label_3")
        self.horizontalLayout_25.addWidget(self.label_3)
        self.page_box_2 = QSpinBox(self.horizontalWidget_2)
        self.page_box_2.setObjectName(u"page_box_2")
        self.horizontalLayout_25.addWidget(self.page_box_2)
        self.horizontalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(self.horizontalSpacer_5)

        self.label_4 = QLabel(self.horizontalWidget_2)
        self.label_4.setObjectName(u"label_4")
        self.horizontalLayout_25.addWidget(self.label_4)
        self.total_page_num_2 = QLabel(self.horizontalWidget_2)
        self.total_page_num_2.setObjectName(u"total_page_num_2")
        self.horizontalLayout_25.addWidget(self.total_page_num_2)
        self.horizontalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(self.horizontalSpacer_6)
        self.type_label_2 = QLabel(self.horizontalWidget_2)
        self.type_label_2.setObjectName(u"type_label_2")
        self.horizontalLayout_25.addWidget(self.type_label_2)
        self.type_box_2 = QComboBox(self.horizontalWidget_2)
        self.type_box_2.addItem("")
        self.type_box_2.addItem("")
        self.type_box_2.addItem("")
        self.type_box_2.setObjectName(u"type_box_2")
        self.horizontalLayout_25.addWidget(self.type_box_2)
        self.title_label_2 = QLabel(self.horizontalWidget_2)
        self.title_label_2.setObjectName(u"title_label_2")
        self.title_label_2.setMaximumSize(QSize(100, 16777215))
        self.horizontalLayout_25.addWidget(self.title_label_2)
        self.line_edit_2 = QLineEdit(self.horizontalWidget_2)
        self.line_edit_2.setObjectName(u"line_edit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.line_edit_2.sizePolicy().hasHeightForWidth())
        self.line_edit_2.setSizePolicy(sizePolicy3)
        self.line_edit_2.setMaximumSize(QSize(100, 16777215))
        self.horizontalLayout_25.addWidget(self.line_edit_2)
        self.search_button_2 = QPushButton(self.horizontalWidget_2)
        self.search_button_2.setObjectName(u"search_button_2")
        self.search_button_2.setMaximumSize(QSize(100, 16777215))
        self.horizontalLayout_25.addWidget(self.search_button_2)
        self.verticalLayout_98.addWidget(self.horizontalWidget_2)

        self.table_widget_2 = TableWithButtons()
        self.table_widget_2.setObjectName(u"table_widget_2")
        self.table_widget_2.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_98.addWidget(self.table_widget_2)

        self.verticalLayout_97.addWidget(self.widget_2)

        self.verticalLayout_96.addWidget(self.TaskRecordContent)

        self.verticalLayout_13.addWidget(self.TaskRecordContentBox)

        self.DataManageContentBox = QFrame(self.ContentBox)
        self.DataManageContentBox.setObjectName(u"DataManageContentBox")
        self.DataManageContentBox.setMaximumSize(QSize(16777215, 0))
        self.DataManageContentBox.setStyleSheet(u"QFrame#DataManageContentBox{\n"
                                                "	background-color: rgb(245, 249, 254);\n"
                                                "border:0px solid red;\n"
                                                "border-radius:20px\n"
                                                "}")
        self.DataManageContentBox.setFrameShape(QFrame.StyledPanel)
        self.DataManageContentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.DataManageContentBox)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.DataManageContent = QFrame(self.DataManageContentBox)
        self.DataManageContent.setObjectName(u"DataManageContent")
        self.DataManageContent.setMaximumSize(QSize(16777215, 16777215))
        self.DataManageContent.setFrameShape(QFrame.StyledPanel)
        self.DataManageContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.DataManageContent)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(-1, 0, -1, -1)
        self.widget = QWidget(self.DataManageContent)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_44 = QVBoxLayout(self.widget)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(-1, 0, -1, -1)
        self.horizontalWidget = QWidget(self.widget)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalWidget.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_24 = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.add_button = QPushButton(self.horizontalWidget)
        self.add_button.setObjectName(u"add_button")
        self.add_button.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_24.addWidget(self.add_button)

        self.horizontalSpacer = QSpacerItem(16777215, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self.horizontalWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_24.addWidget(self.label_2)

        self.page_box = QSpinBox(self.horizontalWidget)
        self.page_box.setObjectName(u"page_box")

        self.horizontalLayout_24.addWidget(self.page_box)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_3)

        self.label = QLabel(self.horizontalWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_24.addWidget(self.label)

        self.total_page_num = QLabel(self.horizontalWidget)
        self.total_page_num.setObjectName(u"total_page_num")

        self.horizontalLayout_24.addWidget(self.total_page_num)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_2)

        self.type_label = QLabel(self.horizontalWidget)
        self.type_label.setObjectName(u"type_label")

        self.horizontalLayout_24.addWidget(self.type_label)

        self.type_box = QComboBox(self.horizontalWidget)
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.type_box.addItem("")
        self.type_box.setObjectName(u"type_box")

        self.horizontalLayout_24.addWidget(self.type_box)

        self.title_label = QLabel(self.horizontalWidget)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_24.addWidget(self.title_label)

        self.line_edit = QLineEdit(self.horizontalWidget)
        self.line_edit.setObjectName(u"line_edit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.line_edit.sizePolicy().hasHeightForWidth())
        self.line_edit.setSizePolicy(sizePolicy2)
        self.line_edit.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_24.addWidget(self.line_edit)

        self.search_button = QPushButton(self.horizontalWidget)
        self.search_button.setObjectName(u"search_button")
        self.search_button.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_24.addWidget(self.search_button)

        self.verticalLayout_44.addWidget(self.horizontalWidget)

        self.table_widget = TableWithButtons()
        self.table_widget.setObjectName(u"table_widget")

        self.verticalLayout_44.addWidget(self.table_widget)

        self.verticalLayout_37.addWidget(self.widget)

        self.verticalLayout_36.addWidget(self.DataManageContent)

        self.verticalLayout_13.addWidget(self.DataManageContentBox)

        self.ReidContentBox = QFrame(self.ContentBox)
        self.ReidContentBox.setObjectName(u"ReidContentBox")
        self.ReidContentBox.setMaximumSize(QSize(16777215, 0))
        self.ReidContentBox.setStyleSheet(u"QFrame#ReidContentBox{\n"
"	background-color: rgb(245, 249, 254);\n"
"border:0px solid red;\n"
"border-radius:20px\n"
"}")
        self.ReidContentBox.setFrameShape(QFrame.StyledPanel)
        self.ReidContentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.ReidContentBox)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.reidContent = QFrame(self.ReidContentBox)
        self.reidContent.setObjectName(u"reidContent")
        self.reidContent.setMaximumSize(QSize(16777215, 16777215))
        self.reidContent.setFrameShape(QFrame.StyledPanel)
        self.reidContent.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.reidContent)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(-1, 0, 0, 0)
        self.main_content_2 = QVBoxLayout()
        self.main_content_2.setSpacing(5)
        self.main_content_2.setObjectName(u"main_content_2")
        self.Content_Top_2 = QFrame(self.reidContent)
        self.Content_Top_2.setObjectName(u"Content_Top_2")
        self.Content_Top_2.setMaximumSize(QSize(16777215, 40))
        self.Content_Top_2.setFrameShape(QFrame.StyledPanel)
        self.Content_Top_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content_Top_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.reid_char_label = QLabel(self.Content_Top_2)
        self.reid_char_label.setObjectName(u"reid_char_label")
        self.reid_char_label.setMinimumSize(QSize(0, 20))
        self.reid_char_label.setMaximumSize(QSize(16777215, 20))
        self.reid_char_label.setFont(font1)
        self.reid_char_label.setStyleSheet(u"padding-left:12px;")

        self.horizontalLayout_2.addWidget(self.reid_char_label)

        self.reid_set_button = QPushButton(self.Content_Top_2)
        self.reid_set_button.setObjectName(u"reid_set_button")
        sizePolicy.setHeightForWidth(self.reid_set_button.sizePolicy().hasHeightForWidth())
        self.reid_set_button.setSizePolicy(sizePolicy)
        self.reid_set_button.setMaximumSize(QSize(20, 50))
        self.reid_set_button.setStyleSheet(u"QPushButton{\n"
"	border-image: url(:/all/img/set.png);\n"
"}")

        self.horizontalLayout_2.addWidget(self.reid_set_button)


        self.main_content_2.addWidget(self.Content_Top_2)

        self.QF_Group_2 = QFrame(self.reidContent)
        self.QF_Group_2.setObjectName(u"QF_Group_2")
        self.QF_Group_2.setMinimumSize(QSize(0, 140))
        self.QF_Group_2.setMaximumSize(QSize(16777215, 140))
        self.QF_Group_2.setStyleSheet(u"QFrame#QF_Group_2{\n"
"background-color: rgb(200, 242, 255);\n"
"border:2px solid rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"}")
        self.QF_Group_2.setFrameShape(QFrame.StyledPanel)
        self.QF_Group_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.QF_Group_2)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(-1, 9, -1, 15)
        self.Target_Select = QFrame(self.QF_Group_2)
        self.Target_Select.setObjectName(u"Target_Select")
        self.Target_Select.setMinimumSize(QSize(120, 80))
        self.Target_Select.setMaximumSize(QSize(120, 80))
        self.Target_Select.setFrameShape(QFrame.StyledPanel)
        self.Target_Select.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.Target_Select)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.target_label_3 = QLabel(self.Target_Select)
        self.target_label_3.setObjectName(u"target_label_3")
        font5 = QFont()
        font5.setBold(True)
        self.target_label_3.setFont(font5)

        self.verticalLayout_42.addWidget(self.target_label_3)

        self.target_select_button = QPushButton(self.Target_Select)
        self.target_select_button.setObjectName(u"target_select_button")
        self.target_select_button.setMinimumSize(QSize(0, 45))
        self.target_select_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.target_select_button.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/file.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"background-color: rgb(100, 138, 255);\n"
"border: none;\n"
"border-left: 23px solid transparent;\n"
"\n"
"text-align: center;\n"
"padding-left: 0px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 12pt \"Nirmala UI\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(157, 200, 255);\n"
"}")

        self.verticalLayout_42.addWidget(self.target_select_button)


        self.horizontalLayout_16.addWidget(self.Target_Select)

        self.select_button_2 = QFrame(self.QF_Group_2)
        self.select_button_2.setObjectName(u"select_button_2")
        self.select_button_2.setMaximumSize(QSize(220, 16777215))
        self.select_button_2.setStyleSheet(u"background-color: rgb(206, 206, 255);")
        self.select_button_2.setFrameShape(QFrame.StyledPanel)
        self.select_button_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.select_button_2)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.src_cam_button_2 = QPushButton(self.select_button_2)
        self.src_cam_button_2.setObjectName(u"src_cam_button_2")
        self.src_cam_button_2.setMinimumSize(QSize(0, 30))
        self.src_cam_button_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.src_cam_button_2.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/cam.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"background-color: rgb(100, 138, 255);\n"
"border: none;\n"
"border-left: 23px solid transparent;\n"
"\n"
"text-align: center;\n"
"padding-left: 0px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 12pt \"Nirmala UI\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(157, 200, 255);\n"
"}")

        self.verticalLayout_30.addWidget(self.src_cam_button_2)

        self.src_rtsp_button_2 = QPushButton(self.select_button_2)
        self.src_rtsp_button_2.setObjectName(u"src_rtsp_button_2")
        self.src_rtsp_button_2.setMinimumSize(QSize(0, 30))
        self.src_rtsp_button_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.src_rtsp_button_2.setAutoFillBackground(False)
        self.src_rtsp_button_2.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/RTSP.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"background-color: rgb(100, 138, 255);\n"
"border: none;\n"
"border-left: 23px solid transparent;\n"
"\n"
"text-align: center;\n"
"padding-left: 0px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 12pt \"Nirmala UI\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(157, 200, 255);\n"
"}")
        self.src_rtsp_button_2.setIconSize(QSize(16, 16))

        self.verticalLayout_30.addWidget(self.src_rtsp_button_2)

        self.src_file_button_2 = QPushButton(self.select_button_2)
        self.src_file_button_2.setObjectName(u"src_file_button_2")
        self.src_file_button_2.setMinimumSize(QSize(0, 30))
        self.src_file_button_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.src_file_button_2.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/file.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"background-color: rgb(100, 138, 255);\n"
"border: none;\n"
"border-left: 23px solid transparent;\n"
"\n"
"text-align: center;\n"
"padding-left: 0px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 12pt \"Nirmala UI\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(157, 200, 255);\n"
"}")

        self.verticalLayout_30.addWidget(self.src_file_button_2)


        self.horizontalLayout_16.addWidget(self.select_button_2)

        self.Class_QF_2 = QFrame(self.QF_Group_2)
        self.Class_QF_2.setObjectName(u"Class_QF_2")
        self.Class_QF_2.setMinimumSize(QSize(170, 80))
        self.Class_QF_2.setMaximumSize(QSize(170, 80))
        self.Class_QF_2.setToolTipDuration(0)
        self.Class_QF_2.setStyleSheet(u"QFrame#Class_QF_2{\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"background-color: qradialgradient(cx:0, cy:0, radius:1, fx:0.1, fy:0.1, stop:0 rgb(162, 129, 247),  stop:1 rgb(119, 111, 252));\n"
"border: 1px outset rgb(98, 91, 213);\n"
"}\n"
"")
        self.Class_QF_2.setFrameShape(QFrame.StyledPanel)
        self.Class_QF_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.Class_QF_2)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.Class_top_2 = QFrame(self.Class_QF_2)
        self.Class_top_2.setObjectName(u"Class_top_2")
        self.Class_top_2.setStyleSheet(u"border:none")
        self.Class_top_2.setFrameShape(QFrame.StyledPanel)
        self.Class_top_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.Class_top_2)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 3, 0, 3)
        self.class_label_2 = QLabel(self.Class_top_2)
        self.class_label_2.setObjectName(u"class_label_2")
        self.class_label_2.setMaximumSize(QSize(16777215, 30))
        self.class_label_2.setFont(font2)
        self.class_label_2.setStyleSheet(u"color: rgba(255, 255, 255,210);\n"
"padding-left:12px;\n"
"font: 700 italic 16pt \"Segoe UI\";")
        self.class_label_2.setAlignment(Qt.AlignCenter)
        self.class_label_2.setIndent(0)

        self.horizontalLayout_17.addWidget(self.class_label_2)


        self.verticalLayout_31.addWidget(self.Class_top_2)

        self.class_line_2 = QFrame(self.Class_QF_2)
        self.class_line_2.setObjectName(u"class_line_2")
        self.class_line_2.setMaximumSize(QSize(16777215, 1))
        self.class_line_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 89);")
        self.class_line_2.setFrameShape(QFrame.HLine)
        self.class_line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_31.addWidget(self.class_line_2)

        self.Class_bottom_2 = QFrame(self.Class_QF_2)
        self.Class_bottom_2.setObjectName(u"Class_bottom_2")
        self.Class_bottom_2.setStyleSheet(u"border:none")
        self.Class_bottom_2.setFrameShape(QFrame.StyledPanel)
        self.Class_bottom_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.Class_bottom_2)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 6, 0, 6)
        self.class_num_2 = QLabel(self.Class_bottom_2)
        self.class_num_2.setObjectName(u"class_num_2")
        self.class_num_2.setMinimumSize(QSize(0, 30))
        self.class_num_2.setMaximumSize(QSize(16777215, 30))
        self.class_num_2.setFont(font3)
        self.class_num_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 17pt \"Microsoft YaHei UI\";")
        self.class_num_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.class_num_2, 0, Qt.AlignTop)


        self.verticalLayout_31.addWidget(self.Class_bottom_2)

        self.verticalLayout_31.setStretch(1, 2)
        self.verticalLayout_31.setStretch(2, 1)

        self.horizontalLayout_16.addWidget(self.Class_QF_2)

        self.Target_QF_2 = QFrame(self.QF_Group_2)
        self.Target_QF_2.setObjectName(u"Target_QF_2")
        self.Target_QF_2.setMinimumSize(QSize(170, 80))
        self.Target_QF_2.setMaximumSize(QSize(170, 80))
        self.Target_QF_2.setToolTipDuration(0)
        self.Target_QF_2.setStyleSheet(u"QFrame#Target_QF_2{\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"background-color: qradialgradient(cx:0, cy:0, radius:1, fx:0.1, fy:0.1, stop:0 rgb(253, 139, 133),  stop:1 rgb(248, 194, 152));\n"
"border: 1px outset rgb(252, 194, 149)\n"
"}\n"
"")
        self.Target_QF_2.setFrameShape(QFrame.StyledPanel)
        self.Target_QF_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.Target_QF_2)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.Target_top_2 = QFrame(self.Target_QF_2)
        self.Target_top_2.setObjectName(u"Target_top_2")
        self.Target_top_2.setStyleSheet(u"border:none")
        self.Target_top_2.setFrameShape(QFrame.StyledPanel)
        self.Target_top_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.Target_top_2)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 3, 0, 3)
        self.target_label_2 = QLabel(self.Target_top_2)
        self.target_label_2.setObjectName(u"target_label_2")
        self.target_label_2.setMaximumSize(QSize(16777215, 30))
        self.target_label_2.setFont(font2)
        self.target_label_2.setStyleSheet(u"color: rgba(255, 255, 255,210);\n"
"padding-left:12px;\n"
"font: 700 italic 16pt \"Segoe UI\";")
        self.target_label_2.setAlignment(Qt.AlignCenter)
        self.target_label_2.setIndent(0)

        self.horizontalLayout_18.addWidget(self.target_label_2)


        self.verticalLayout_33.addWidget(self.Target_top_2)

        self.target_line_2 = QFrame(self.Target_QF_2)
        self.target_line_2.setObjectName(u"target_line_2")
        self.target_line_2.setMaximumSize(QSize(16777215, 1))
        self.target_line_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 89);")
        self.target_line_2.setFrameShape(QFrame.HLine)
        self.target_line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_33.addWidget(self.target_line_2)

        self.Target_bottom_2 = QFrame(self.Target_QF_2)
        self.Target_bottom_2.setObjectName(u"Target_bottom_2")
        self.Target_bottom_2.setStyleSheet(u"border:none")
        self.Target_bottom_2.setFrameShape(QFrame.StyledPanel)
        self.Target_bottom_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.Target_bottom_2)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 6, 0, 6)
        self.target_num_2 = QLabel(self.Target_bottom_2)
        self.target_num_2.setObjectName(u"target_num_2")
        self.target_num_2.setMinimumSize(QSize(0, 30))
        self.target_num_2.setMaximumSize(QSize(16777215, 30))
        self.target_num_2.setFont(font3)
        self.target_num_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 17pt \"Microsoft YaHei UI\";")
        self.target_num_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_34.addWidget(self.target_num_2, 0, Qt.AlignTop)


        self.verticalLayout_33.addWidget(self.Target_bottom_2)

        self.verticalLayout_33.setStretch(1, 2)
        self.verticalLayout_33.setStretch(2, 1)

        self.horizontalLayout_16.addWidget(self.Target_QF_2)

        self.Fps_QF_2 = QFrame(self.QF_Group_2)
        self.Fps_QF_2.setObjectName(u"Fps_QF_2")
        self.Fps_QF_2.setMinimumSize(QSize(170, 80))
        self.Fps_QF_2.setMaximumSize(QSize(170, 80))
        self.Fps_QF_2.setToolTipDuration(0)
        self.Fps_QF_2.setStyleSheet(u"QFrame#Fps_QF_2{\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"background-color: qradialgradient(cx:0, cy:0, radius:1, fx:0.1, fy:0.1, stop:0 rgb(243, 175, 189),  stop:1 rgb(155, 118, 218));\n"
"border: 1px outset rgb(153, 117, 219)\n"
"}\n"
"")
        self.Fps_QF_2.setFrameShape(QFrame.StyledPanel)
        self.Fps_QF_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.Fps_QF_2)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.Fps_top_2 = QFrame(self.Fps_QF_2)
        self.Fps_top_2.setObjectName(u"Fps_top_2")
        self.Fps_top_2.setStyleSheet(u"border:none")
        self.Fps_top_2.setFrameShape(QFrame.StyledPanel)
        self.Fps_top_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.Fps_top_2)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 3, 7, 3)
        self.fps_label_2 = QLabel(self.Fps_top_2)
        self.fps_label_2.setObjectName(u"fps_label_2")
        self.fps_label_2.setMaximumSize(QSize(16777215, 30))
        self.fps_label_2.setFont(font2)
        self.fps_label_2.setStyleSheet(u"color: rgba(255, 255, 255,210);\n"
"padding-left:12px;\n"
"font: 700 italic 16pt \"Segoe UI\";")
        self.fps_label_2.setMidLineWidth(-1)
        self.fps_label_2.setAlignment(Qt.AlignCenter)
        self.fps_label_2.setWordWrap(False)
        self.fps_label_2.setIndent(0)

        self.horizontalLayout_19.addWidget(self.fps_label_2)


        self.verticalLayout_35.addWidget(self.Fps_top_2)

        self.fps_line_2 = QFrame(self.Fps_QF_2)
        self.fps_line_2.setObjectName(u"fps_line_2")
        self.fps_line_2.setMaximumSize(QSize(16777215, 1))
        self.fps_line_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 89);")
        self.fps_line_2.setFrameShape(QFrame.HLine)
        self.fps_line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_35.addWidget(self.fps_line_2)

        self.Fps_bottom_2 = QFrame(self.Fps_QF_2)
        self.Fps_bottom_2.setObjectName(u"Fps_bottom_2")
        self.Fps_bottom_2.setStyleSheet(u"border:none")
        self.Fps_bottom_2.setFrameShape(QFrame.StyledPanel)
        self.Fps_bottom_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.Fps_bottom_2)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 6, 0, 6)
        self.fps_num_2 = QLabel(self.Fps_bottom_2)
        self.fps_num_2.setObjectName(u"fps_num_2")
        self.fps_num_2.setMinimumSize(QSize(0, 30))
        self.fps_num_2.setMaximumSize(QSize(16777215, 30))
        self.fps_num_2.setFont(font3)
        self.fps_num_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 17pt \"Microsoft YaHei UI\";")
        self.fps_num_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_38.addWidget(self.fps_num_2, 0, Qt.AlignTop)


        self.verticalLayout_35.addWidget(self.Fps_bottom_2)

        self.verticalLayout_35.setStretch(1, 2)
        self.verticalLayout_35.setStretch(2, 1)

        self.horizontalLayout_16.addWidget(self.Fps_QF_2)


        self.main_content_2.addWidget(self.QF_Group_2)

        self.Result_List = QFrame(self.reidContent)
        self.Result_List.setObjectName(u"Result_List")
        self.Result_List.setMinimumSize(QSize(0, 100))
        self.Result_List.setMaximumSize(QSize(16777215, 150))
        self.Result_List.setStyleSheet(u"QFrame#Result_List{\n"
"background-color: rgb(200, 242, 255);\n"
"border:2px solid rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"}")
        self.Result_List.setFrameShape(QFrame.StyledPanel)
        self.Result_List.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.Result_List)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.listWidget = QListWidget(self.Result_List)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setStyleSheet(u"background-color: rgb(200, 242, 255);\n"
"border:2px solid rgb(255, 255, 255);\n"
"border-radius:15px")
        self.listWidget.setIconSize(QSize(128, 64))
        self.listWidget.setFlow(QListView.LeftToRight)
        self.listWidget.setResizeMode(QListView.Adjust)
        self.verticalLayout_43.addWidget(self.listWidget)


        self.main_content_2.addWidget(self.Result_List)

        self.Result_QF_2 = QFrame(self.reidContent)
        self.Result_QF_2.setObjectName(u"Result_QF_2")
        self.Result_QF_2.setStyleSheet(u"")
        self.Result_QF_2.setFrameShape(QFrame.StyledPanel)
        self.Result_QF_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.Result_QF_2)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.splitter_2 = QSplitter(self.Result_QF_2)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setStyleSheet(u"#splitter::handle{background: 1px solid  rgba(200, 200, 200,100);}")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.splitter_2.setHandleWidth(2)
        self.pre_video_2 = QLabel(self.splitter_2)
        self.pre_video_2.setObjectName(u"pre_video_2")
        self.pre_video_2.setMinimumSize(QSize(200, 100))
        self.pre_video_2.setStyleSheet(u"background-color: rgb(200, 242, 255);\n"
"border:2px solid rgb(255, 255, 255);\n"
"border-radius:15px")
        self.pre_video_2.setAlignment(Qt.AlignCenter)
        self.splitter_2.addWidget(self.pre_video_2)
        self.res_video_2 = QLabel(self.splitter_2)
        self.res_video_2.setObjectName(u"res_video_2")
        self.res_video_2.setMinimumSize(QSize(200, 100))
        self.res_video_2.setStyleSheet(u"background-color: rgb(200, 242, 255);\n"
"border:2px solid rgb(255, 255, 255);\n"
"border-radius:15px")
        self.res_video_2.setAlignment(Qt.AlignCenter)
        self.splitter_2.addWidget(self.res_video_2)

        self.verticalLayout_39.addWidget(self.splitter_2)


        self.main_content_2.addWidget(self.Result_QF_2)

        self.Pause_QF_2 = QFrame(self.reidContent)
        self.Pause_QF_2.setObjectName(u"Pause_QF_2")
        self.Pause_QF_2.setMinimumSize(QSize(0, 30))
        self.Pause_QF_2.setMaximumSize(QSize(16777215, 30))
        self.Pause_QF_2.setFrameShape(QFrame.StyledPanel)
        self.Pause_QF_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.Pause_QF_2)
        self.horizontalLayout_20.setSpacing(10)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 3, 0)
        self.run_button_2 = QPushButton(self.Pause_QF_2)
        self.run_button_2.setObjectName(u"run_button_2")
        self.run_button_2.setMinimumSize(QSize(0, 30))
        self.run_button_2.setMaximumSize(QSize(16777215, 30))
        self.run_button_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.run_button_2.setMouseTracking(True)
        self.run_button_2.setStyleSheet(u"QPushButton{\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"border: none;\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"}")
        self.run_button_2.setIcon(icon1)
        self.run_button_2.setIconSize(QSize(30, 30))
        self.run_button_2.setCheckable(True)
        self.run_button_2.setChecked(False)

        self.horizontalLayout_20.addWidget(self.run_button_2)

        self.progress_bar_2 = QProgressBar(self.Pause_QF_2)
        self.progress_bar_2.setObjectName(u"progress_bar_2")
        self.progress_bar_2.setMinimumSize(QSize(0, 20))
        self.progress_bar_2.setMaximumSize(QSize(16777215, 20))
        self.progress_bar_2.setStyleSheet(u"QProgressBar{ \n"
"font: 700 10pt \"Microsoft YaHei UI\";\n"
"color: rgb(253, 143, 134); \n"
"text-align:center; \n"
"border:3px solid rgb(255, 255, 255);\n"
"border-radius: 10px; \n"
"background-color: rgba(215, 215, 215,100);\n"
"} \n"
"\n"
"QProgressBar:chunk{ \n"
"border-radius:0px; \n"
"background: rgba(119, 111, 252, 200);\n"
"border-radius: 7px;\n"
"}")
        self.progress_bar_2.setMaximum(1000)
        self.progress_bar_2.setValue(0)

        self.horizontalLayout_20.addWidget(self.progress_bar_2)

        self.stop_button_2 = QPushButton(self.Pause_QF_2)
        self.stop_button_2.setObjectName(u"stop_button_2")
        self.stop_button_2.setMinimumSize(QSize(0, 30))
        self.stop_button_2.setMaximumSize(QSize(16777215, 30))
        self.stop_button_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.stop_button_2.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/stop.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"}")

        self.horizontalLayout_20.addWidget(self.stop_button_2)


        self.main_content_2.addWidget(self.Pause_QF_2)


        self.horizontalLayout_21.addLayout(self.main_content_2)

        self.prm_page_2 = QFrame(self.reidContent)
        self.prm_page_2.setObjectName(u"prm_page_2")
        self.prm_page_2.setMinimumSize(QSize(220, 0))
        self.prm_page_2.setMaximumSize(QSize(0, 16777215))
        self.prm_page_2.setStyleSheet(u"QFrame#prm_page_2{\n"
"background-color: qradialgradient(cx:0, cy:0, radius:1, fx:0.1, fy:0.1, stop:0 rgb(243, 175, 189),  stop:1 rgb(155, 118, 218));\n"
"border-top-left-radius:30px;\n"
"border-top-right-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"border-bottom-left-radius:30px;\n"
"}")
        self.prm_page_2.setFrameShape(QFrame.StyledPanel)
        self.prm_page_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.prm_page_2)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.setting_label_2 = QLabel(self.prm_page_2)
        self.setting_label_2.setObjectName(u"setting_label_2")
        self.setting_label_2.setStyleSheet(u"padding-left: 0px;\n"
"padding-bottom: 2px;\n"
"color: rgba(255, 255, 255, 240);\n"
"font: 700 italic 16pt \"Segoe UI\";")
        self.setting_label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.setting_label_2)

        self.Reid_Model_QF = QWidget(self.prm_page_2)
        self.Reid_Model_QF.setObjectName(u"Reid_Model_QF")
        self.Reid_Model_QF.setMinimumSize(QSize(190, 90))
        self.Reid_Model_QF.setMaximumSize(QSize(190, 90))
        self.Reid_Model_QF.setStyleSheet(u"QWidget#Reid_Model_QF{\n"
"border:2px solid rgba(255, 255, 255, 70);\n"
"border-radius:15px;\n"
"}")
        self.verticalLayout_41 = QVBoxLayout(self.Reid_Model_QF)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(9, 9, 9, 9)
        self.ToggleBotton_12 = QPushButton(self.Reid_Model_QF)
        self.ToggleBotton_12.setObjectName(u"ToggleBotton_12")
        sizePolicy1.setHeightForWidth(self.ToggleBotton_12.sizePolicy().hasHeightForWidth())
        self.ToggleBotton_12.setSizePolicy(sizePolicy1)
        self.ToggleBotton_12.setMinimumSize(QSize(0, 30))
        self.ToggleBotton_12.setMaximumSize(QSize(16777215, 30))
        self.ToggleBotton_12.setFont(font4)
        self.ToggleBotton_12.setCursor(QCursor(Qt.ArrowCursor))
        self.ToggleBotton_12.setMouseTracking(True)
        self.ToggleBotton_12.setFocusPolicy(Qt.StrongFocus)
        self.ToggleBotton_12.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.ToggleBotton_12.setLayoutDirection(Qt.LeftToRight)
        self.ToggleBotton_12.setAutoFillBackground(False)
        self.ToggleBotton_12.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/model.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 20px solid transparent;\n"
"\n"
"text-align: left;\n"
"padding-left: 40px;\n"
"padding-bottom: 2px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 13pt \"Nirmala UI\";\n"
"}")
        self.ToggleBotton_12.setIcon(icon)
        self.ToggleBotton_12.setAutoDefault(False)
        self.ToggleBotton_12.setFlat(False)

        self.verticalLayout_41.addWidget(self.ToggleBotton_12)

        self.reid_model_box = QComboBox(self.Reid_Model_QF)
        self.reid_model_box.setObjectName(u"reid_model_box")
        self.reid_model_box.setMinimumSize(QSize(170, 20))
        self.reid_model_box.setMaximumSize(QSize(170, 20))
        self.reid_model_box.setStyleSheet(u"\n"
"QComboBox {\n"
"            background-color: rgba(255,255,255,90);\n"
"			color: rgba(0, 0, 0, 200);\n"
"			font: 600 9pt \"Segoe UI\";\n"
"            border: 1px solid lightgray;\n"
"            border-radius: 10px;\n"
"            padding-left: 15px;\n"
"        }\n"
"        \n"
"        QComboBox:on {\n"
"            border: 1px solid #63acfb;\n"
"        }\n"
"\n"
"        QComboBox::drop-down {\n"
"            width: 22px;\n"
"            border-left: 1px solid lightgray;\n"
"            border-top-right-radius: 15px;\n"
"            border-bottom-right-radius: 15px;\n"
"        }\n"
"        \n"
"        QComboBox::drop-down:on {\n"
"            border-left: 1px solid #63acfb;\n"
"        }\n"
"\n"
"        QComboBox::down-arrow {\n"
"            width: 16px;\n"
"            height: 16px;\n"
"            image: url(:/all/img/box_down.png);\n"
"        }\n"
"\n"
"        QComboBox::down-arrow:on {\n"
"            image: url(:/all/img/box_up.png);\n"
"        }\n"
"\n"
"        QComboBox QAbstractI"
                        "temView {\n"
"            border: none;\n"
"            outline: none;\n"
"			padding: 10px;\n"
"            background-color: rgb(223, 188, 220);\n"
"        }\n"
"\n"
"\n"
"        QComboBox QScrollBar:vertical {\n"
"            width: 2px;\n"
"           background-color: rgba(255,255,255,150);\n"
"        }\n"
"\n"
"        QComboBox QScrollBar::handle:vertical {\n"
"            background-color: rgba(255,255,255,90);\n"
"        }")
        self.reid_model_box.setInsertPolicy(QComboBox.NoInsert)
        self.reid_model_box.setMinimumContentsLength(0)

        self.verticalLayout_41.addWidget(self.reid_model_box)


        self.verticalLayout_24.addWidget(self.Reid_Model_QF)

        self.Model_QF_2 = QWidget(self.prm_page_2)
        self.Model_QF_2.setObjectName(u"Model_QF_2")
        self.Model_QF_2.setMinimumSize(QSize(190, 90))
        self.Model_QF_2.setMaximumSize(QSize(190, 90))
        self.Model_QF_2.setStyleSheet(u"QWidget#Model_QF_2{\n"
"border:2px solid rgba(255, 255, 255, 70);\n"
"border-radius:15px;\n"
"}")
        self.verticalLayout_25 = QVBoxLayout(self.Model_QF_2)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(9, 9, 9, 9)
        self.ToggleBotton_7 = QPushButton(self.Model_QF_2)
        self.ToggleBotton_7.setObjectName(u"ToggleBotton_7")
        sizePolicy1.setHeightForWidth(self.ToggleBotton_7.sizePolicy().hasHeightForWidth())
        self.ToggleBotton_7.setSizePolicy(sizePolicy1)
        self.ToggleBotton_7.setMinimumSize(QSize(0, 30))
        self.ToggleBotton_7.setMaximumSize(QSize(16777215, 30))
        self.ToggleBotton_7.setFont(font4)
        self.ToggleBotton_7.setCursor(QCursor(Qt.ArrowCursor))
        self.ToggleBotton_7.setMouseTracking(True)
        self.ToggleBotton_7.setFocusPolicy(Qt.StrongFocus)
        self.ToggleBotton_7.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.ToggleBotton_7.setLayoutDirection(Qt.LeftToRight)
        self.ToggleBotton_7.setAutoFillBackground(False)
        self.ToggleBotton_7.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/model.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 20px solid transparent;\n"
"\n"
"text-align: left;\n"
"padding-left: 40px;\n"
"padding-bottom: 2px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 13pt \"Nirmala UI\";\n"
"}")
        self.ToggleBotton_7.setIcon(icon)
        self.ToggleBotton_7.setAutoDefault(False)
        self.ToggleBotton_7.setFlat(False)

        self.verticalLayout_25.addWidget(self.ToggleBotton_7)

        self.model_box_2 = QComboBox(self.Model_QF_2)
        self.model_box_2.setObjectName(u"model_box_2")
        self.model_box_2.setMinimumSize(QSize(170, 20))
        self.model_box_2.setMaximumSize(QSize(170, 20))
        self.model_box_2.setStyleSheet(u"\n"
"QComboBox {\n"
"            background-color: rgba(255,255,255,90);\n"
"			color: rgba(0, 0, 0, 200);\n"
"			font: 600 9pt \"Segoe UI\";\n"
"            border: 1px solid lightgray;\n"
"            border-radius: 10px;\n"
"            padding-left: 15px;\n"
"        }\n"
"        \n"
"        QComboBox:on {\n"
"            border: 1px solid #63acfb;\n"
"        }\n"
"\n"
"        QComboBox::drop-down {\n"
"            width: 22px;\n"
"            border-left: 1px solid lightgray;\n"
"            border-top-right-radius: 15px;\n"
"            border-bottom-right-radius: 15px;\n"
"        }\n"
"        \n"
"        QComboBox::drop-down:on {\n"
"            border-left: 1px solid #63acfb;\n"
"        }\n"
"\n"
"        QComboBox::down-arrow {\n"
"            width: 16px;\n"
"            height: 16px;\n"
"            image: url(:/all/img/box_down.png);\n"
"        }\n"
"\n"
"        QComboBox::down-arrow:on {\n"
"            image: url(:/all/img/box_up.png);\n"
"        }\n"
"\n"
"        QComboBox QAbstractI"
                        "temView {\n"
"            border: none;\n"
"            outline: none;\n"
"			padding: 10px;\n"
"            background-color: rgb(223, 188, 220);\n"
"        }\n"
"\n"
"\n"
"        QComboBox QScrollBar:vertical {\n"
"            width: 2px;\n"
"           background-color: rgba(255,255,255,150);\n"
"        }\n"
"\n"
"        QComboBox QScrollBar::handle:vertical {\n"
"            background-color: rgba(255,255,255,90);\n"
"        }")
        self.model_box_2.setInsertPolicy(QComboBox.NoInsert)
        self.model_box_2.setMinimumContentsLength(0)

        self.verticalLayout_25.addWidget(self.model_box_2)


        self.verticalLayout_24.addWidget(self.Model_QF_2)

        self.IOU_QF_2 = QFrame(self.prm_page_2)
        self.IOU_QF_2.setObjectName(u"IOU_QF_2")
        self.IOU_QF_2.setMinimumSize(QSize(190, 90))
        self.IOU_QF_2.setMaximumSize(QSize(190, 90))
        self.IOU_QF_2.setStyleSheet(u"QFrame#IOU_QF_2{\n"
"border:2px solid rgba(255, 255, 255, 70);\n"
"border-radius:15px;\n"
"}")
        self.verticalLayout_26 = QVBoxLayout(self.IOU_QF_2)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.ToggleBotton_8 = QPushButton(self.IOU_QF_2)
        self.ToggleBotton_8.setObjectName(u"ToggleBotton_8")
        sizePolicy1.setHeightForWidth(self.ToggleBotton_8.sizePolicy().hasHeightForWidth())
        self.ToggleBotton_8.setSizePolicy(sizePolicy1)
        self.ToggleBotton_8.setMinimumSize(QSize(0, 30))
        self.ToggleBotton_8.setMaximumSize(QSize(16777215, 30))
        self.ToggleBotton_8.setFont(font4)
        self.ToggleBotton_8.setCursor(QCursor(Qt.ArrowCursor))
        self.ToggleBotton_8.setMouseTracking(True)
        self.ToggleBotton_8.setFocusPolicy(Qt.StrongFocus)
        self.ToggleBotton_8.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.ToggleBotton_8.setLayoutDirection(Qt.LeftToRight)
        self.ToggleBotton_8.setAutoFillBackground(False)
        self.ToggleBotton_8.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/IOU.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 20px solid transparent;\n"
"\n"
"text-align: left;\n"
"padding-left: 40px;\n"
"padding-bottom: 4px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 13pt \"Nirmala UI\";\n"
"}")
        self.ToggleBotton_8.setIcon(icon)
        self.ToggleBotton_8.setAutoDefault(False)
        self.ToggleBotton_8.setFlat(False)

        self.verticalLayout_26.addWidget(self.ToggleBotton_8)

        self.frame_4 = QFrame(self.IOU_QF_2)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QSize(0, 20))
        self.frame_4.setMaximumSize(QSize(16777215, 20))
        self.horizontalLayout_13 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_13.setSpacing(10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(8, 0, 10, 0)
        self.iou_spinbox_2 = QDoubleSpinBox(self.frame_4)
        self.iou_spinbox_2.setObjectName(u"iou_spinbox_2")
        self.iou_spinbox_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.iou_spinbox_2.setStyleSheet(u"QDoubleSpinBox {\n"
"border: 0px solid lightgray;\n"
"border-radius: 2px;\n"
"background-color: rgba(255,255,255,90);\n"
"font: 600 9pt \"Segoe UI\";\n"
"}\n"
"        \n"
"QDoubleSpinBox::up-button {\n"
"width: 10px;\n"
"height: 9px;\n"
"margin: 0px 3px 0px 0px;\n"
"border-image: url(:/all/img/box_up.png);\n"
"}\n"
"QDoubleSpinBox::up-button:pressed {\n"
"margin-top: 1px;\n"
"}\n"
"            \n"
"QDoubleSpinBox::down-button {\n"
"width: 10px;\n"
"height: 9px;\n"
"margin: 0px 3px 0px 0px;\n"
"border-image: url(:/all/img/box_down.png);\n"
"}\n"
"QDoubleSpinBox::down-button:pressed {\n"
"margin-bottom: 1px;\n"
"}")
        self.iou_spinbox_2.setMinimum(0.010000000000000)
        self.iou_spinbox_2.setMaximum(1.000000000000000)
        self.iou_spinbox_2.setSingleStep(0.050000000000000)
        self.iou_spinbox_2.setValue(0.450000000000000)

        self.horizontalLayout_13.addWidget(self.iou_spinbox_2)

        self.iou_slider_2 = QSlider(self.frame_4)
        self.iou_slider_2.setObjectName(u"iou_slider_2")
        self.iou_slider_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.iou_slider_2.setStyleSheet(u"QSlider::groove:horizontal {\n"
"border: none;\n"
"height: 10px;\n"
"background-color: rgba(255,255,255,90);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"width: 10px;\n"
"margin: -1px 0px -1px 0px;\n"
"border-radius: 3px;\n"
"background-color: white;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #59969b, stop:1 #04e7fa);\n"
"border-radius: 5px;\n"
"}")
        self.iou_slider_2.setMinimum(1)
        self.iou_slider_2.setMaximum(100)
        self.iou_slider_2.setValue(45)
        self.iou_slider_2.setOrientation(Qt.Horizontal)

        self.horizontalLayout_13.addWidget(self.iou_slider_2)


        self.verticalLayout_26.addWidget(self.frame_4)


        self.verticalLayout_24.addWidget(self.IOU_QF_2)

        self.Conf_QF_2 = QFrame(self.prm_page_2)
        self.Conf_QF_2.setObjectName(u"Conf_QF_2")
        self.Conf_QF_2.setMinimumSize(QSize(190, 90))
        self.Conf_QF_2.setMaximumSize(QSize(190, 90))
        self.Conf_QF_2.setStyleSheet(u"QFrame#Conf_QF_2{\n"
"border:2px solid rgba(255, 255, 255, 70);\n"
"border-radius:15px;\n"
"}")
        self.verticalLayout_27 = QVBoxLayout(self.Conf_QF_2)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.ToggleBotton_9 = QPushButton(self.Conf_QF_2)
        self.ToggleBotton_9.setObjectName(u"ToggleBotton_9")
        sizePolicy1.setHeightForWidth(self.ToggleBotton_9.sizePolicy().hasHeightForWidth())
        self.ToggleBotton_9.setSizePolicy(sizePolicy1)
        self.ToggleBotton_9.setMinimumSize(QSize(0, 30))
        self.ToggleBotton_9.setMaximumSize(QSize(16777215, 30))
        self.ToggleBotton_9.setFont(font4)
        self.ToggleBotton_9.setCursor(QCursor(Qt.ArrowCursor))
        self.ToggleBotton_9.setMouseTracking(True)
        self.ToggleBotton_9.setFocusPolicy(Qt.StrongFocus)
        self.ToggleBotton_9.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.ToggleBotton_9.setLayoutDirection(Qt.LeftToRight)
        self.ToggleBotton_9.setAutoFillBackground(False)
        self.ToggleBotton_9.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/conf.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 20px solid transparent;\n"
"\n"
"text-align: left;\n"
"padding-left: 40px;\n"
"padding-bottom: 4px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 13pt \"Nirmala UI\";\n"
"}")
        self.ToggleBotton_9.setIcon(icon)
        self.ToggleBotton_9.setAutoDefault(False)
        self.ToggleBotton_9.setFlat(False)

        self.verticalLayout_27.addWidget(self.ToggleBotton_9)

        self.frame_5 = QFrame(self.Conf_QF_2)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMinimumSize(QSize(0, 20))
        self.frame_5.setMaximumSize(QSize(16777215, 20))
        self.horizontalLayout_14 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_14.setSpacing(10)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(8, 0, 10, 0)
        self.conf_spinbox_2 = QDoubleSpinBox(self.frame_5)
        self.conf_spinbox_2.setObjectName(u"conf_spinbox_2")
        self.conf_spinbox_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.conf_spinbox_2.setStyleSheet(u"QDoubleSpinBox {\n"
"border: 0px solid lightgray;\n"
"border-radius: 2px;\n"
"background-color: rgba(255,255,255,90);\n"
"font: 600 9pt \"Segoe UI\";\n"
"}\n"
"        \n"
"QDoubleSpinBox::up-button {\n"
"width: 10px;\n"
"height: 9px;\n"
"margin: 0px 3px 0px 0px;\n"
"border-image: url(:/all/img/box_up.png);\n"
"}\n"
"QDoubleSpinBox::up-button:pressed {\n"
"margin-top: 1px;\n"
"}\n"
"            \n"
"QDoubleSpinBox::down-button {\n"
"width: 10px;\n"
"height: 9px;\n"
"margin: 0px 3px 0px 0px;\n"
"border-image: url(:/all/img/box_down.png);\n"
"}\n"
"QDoubleSpinBox::down-button:pressed {\n"
"margin-bottom: 1px;\n"
"}")
        self.conf_spinbox_2.setMinimum(0.010000000000000)
        self.conf_spinbox_2.setMaximum(1.000000000000000)
        self.conf_spinbox_2.setSingleStep(0.050000000000000)
        self.conf_spinbox_2.setValue(0.250000000000000)

        self.horizontalLayout_14.addWidget(self.conf_spinbox_2)

        self.conf_slider_2 = QSlider(self.frame_5)
        self.conf_slider_2.setObjectName(u"conf_slider_2")
        self.conf_slider_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.conf_slider_2.setStyleSheet(u"QSlider::groove:horizontal {\n"
"border: none;\n"
"height: 10px;\n"
"background-color: rgba(255,255,255,90);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"width: 10px;\n"
"margin: -1px 0px -1px 0px;\n"
"border-radius: 3px;\n"
"background-color: white;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #59969b, stop:1 #04e7fa);\n"
"border-radius: 5px;\n"
"}")
        self.conf_slider_2.setMinimum(1)
        self.conf_slider_2.setMaximum(100)
        self.conf_slider_2.setValue(25)
        self.conf_slider_2.setOrientation(Qt.Horizontal)

        self.horizontalLayout_14.addWidget(self.conf_slider_2)


        self.verticalLayout_27.addWidget(self.frame_5)


        self.verticalLayout_24.addWidget(self.Conf_QF_2)

        self.Delay_QF_2 = QFrame(self.prm_page_2)
        self.Delay_QF_2.setObjectName(u"Delay_QF_2")
        self.Delay_QF_2.setMinimumSize(QSize(190, 90))
        self.Delay_QF_2.setMaximumSize(QSize(190, 90))
        self.Delay_QF_2.setStyleSheet(u"QFrame#Delay_QF_2{\n"
"border:2px solid rgba(255, 255, 255, 70);\n"
"border-radius:15px;\n"
"}")
        self.verticalLayout_28 = QVBoxLayout(self.Delay_QF_2)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.ToggleBotton_10 = QPushButton(self.Delay_QF_2)
        self.ToggleBotton_10.setObjectName(u"ToggleBotton_10")
        sizePolicy1.setHeightForWidth(self.ToggleBotton_10.sizePolicy().hasHeightForWidth())
        self.ToggleBotton_10.setSizePolicy(sizePolicy1)
        self.ToggleBotton_10.setMinimumSize(QSize(0, 30))
        self.ToggleBotton_10.setMaximumSize(QSize(16777215, 30))
        self.ToggleBotton_10.setFont(font4)
        self.ToggleBotton_10.setCursor(QCursor(Qt.ArrowCursor))
        self.ToggleBotton_10.setMouseTracking(True)
        self.ToggleBotton_10.setFocusPolicy(Qt.StrongFocus)
        self.ToggleBotton_10.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.ToggleBotton_10.setLayoutDirection(Qt.LeftToRight)
        self.ToggleBotton_10.setAutoFillBackground(False)
        self.ToggleBotton_10.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/delay.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 20px solid transparent;\n"
"\n"
"text-align: left;\n"
"padding-left: 40px;\n"
"padding-bottom: 2px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 13pt \"Nirmala UI\";\n"
"}")
        self.ToggleBotton_10.setIcon(icon)
        self.ToggleBotton_10.setAutoDefault(False)
        self.ToggleBotton_10.setFlat(False)

        self.verticalLayout_28.addWidget(self.ToggleBotton_10)

        self.frame_6 = QFrame(self.Delay_QF_2)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setMinimumSize(QSize(0, 20))
        self.frame_6.setMaximumSize(QSize(16777215, 20))
        self.horizontalLayout_15 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_15.setSpacing(10)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(8, 0, 10, 0)
        self.speed_spinbox_2 = QSpinBox(self.frame_6)
        self.speed_spinbox_2.setObjectName(u"speed_spinbox_2")
        self.speed_spinbox_2.setStyleSheet(u"QSpinBox {\n"
"border: 0px solid lightgray;\n"
"border-radius: 2px;\n"
"background-color: rgba(255,255,255,90);\n"
"font: 600 9pt \"Segoe UI\";\n"
"}\n"
"        \n"
"QSpinBox::up-button {\n"
"width: 10px;\n"
"height: 9px;\n"
"margin: 0px 3px 0px 0px;\n"
"border-image: url(:/all/img/box_up.png);\n"
"}\n"
"QSpinBox::up-button:pressed {\n"
"margin-top: 1px;\n"
"}\n"
"            \n"
"QSpinBox::down-button {\n"
"width: 10px;\n"
"height: 9px;\n"
"margin: 0px 3px 0px 0px;\n"
"border-image: url(:/all/img/box_down.png);\n"
"}\n"
"QSpinBox::down-button:pressed {\n"
"margin-bottom: 1px;\n"
"}")
        self.speed_spinbox_2.setMaximum(50)
        self.speed_spinbox_2.setValue(10)

        self.horizontalLayout_15.addWidget(self.speed_spinbox_2)

        self.speed_slider_2 = QSlider(self.frame_6)
        self.speed_slider_2.setObjectName(u"speed_slider_2")
        self.speed_slider_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.speed_slider_2.setStyleSheet(u"QSlider::groove:horizontal {\n"
"border: none;\n"
"height: 10px;\n"
"background-color: rgba(255,255,255,90);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"width: 10px;\n"
"margin: -1px 0px -1px 0px;\n"
"border-radius: 3px;\n"
"background-color: white;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background-color: qradialgradient(cx:0, cy:0, radius:1, fx:0.1, fy:0.1, stop:0 rgb(253, 139, 133),  stop:1 rgb(248, 194, 152));\n"
"border-radius: 5px;\n"
"}")
        self.speed_slider_2.setMaximum(50)
        self.speed_slider_2.setValue(10)
        self.speed_slider_2.setOrientation(Qt.Horizontal)

        self.horizontalLayout_15.addWidget(self.speed_slider_2)


        self.verticalLayout_28.addWidget(self.frame_6)


        self.verticalLayout_24.addWidget(self.Delay_QF_2)

        self.Save_QF_2 = QFrame(self.prm_page_2)
        self.Save_QF_2.setObjectName(u"Save_QF_2")
        self.Save_QF_2.setMinimumSize(QSize(190, 120))
        self.Save_QF_2.setMaximumSize(QSize(190, 120))
        self.Save_QF_2.setStyleSheet(u"QFrame#Save_QF_2{\n"
"border:2px solid rgba(255, 255, 255, 70);\n"
"border-radius:15px;\n"
"}")
        self.verticalLayout_29 = QVBoxLayout(self.Save_QF_2)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(9, 9, 9, 9)
        self.ToggleBotton_11 = QPushButton(self.Save_QF_2)
        self.ToggleBotton_11.setObjectName(u"ToggleBotton_11")
        sizePolicy1.setHeightForWidth(self.ToggleBotton_11.sizePolicy().hasHeightForWidth())
        self.ToggleBotton_11.setSizePolicy(sizePolicy1)
        self.ToggleBotton_11.setMinimumSize(QSize(0, 30))
        self.ToggleBotton_11.setMaximumSize(QSize(16777215, 30))
        self.ToggleBotton_11.setFont(font4)
        self.ToggleBotton_11.setCursor(QCursor(Qt.ArrowCursor))
        self.ToggleBotton_11.setMouseTracking(True)
        self.ToggleBotton_11.setFocusPolicy(Qt.StrongFocus)
        self.ToggleBotton_11.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.ToggleBotton_11.setLayoutDirection(Qt.LeftToRight)
        self.ToggleBotton_11.setAutoFillBackground(False)
        self.ToggleBotton_11.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/all/img/save.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 20px solid transparent;\n"
"\n"
"text-align: left;\n"
"padding-left: 40px;\n"
"padding-bottom: 2px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 13pt \"Nirmala UI\";\n"
"}")
        self.ToggleBotton_11.setIcon(icon)
        self.ToggleBotton_11.setAutoDefault(False)
        self.ToggleBotton_11.setFlat(False)

        self.verticalLayout_29.addWidget(self.ToggleBotton_11)

        self.save_res_button_2 = QCheckBox(self.Save_QF_2)
        self.save_res_button_2.setObjectName(u"save_res_button_2")
        self.save_res_button_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.save_res_button_2.setStyleSheet(u"QCheckBox {\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 590 10pt \"Nirmala UI\";\n"
"        }\n"
"\n"
"        QCheckBox::indicator {\n"
"            padding-top: 1px;\n"
"padding-left: 10px;\n"
"            width: 40px;\n"
"            height: 30px;\n"
"            border: none;\n"
"        }\n"
"\n"
"        QCheckBox::indicator:unchecked {\n"
"            image: url(:/all/img/check_no.png);\n"
"        }\n"
"\n"
"        QCheckBox::indicator:checked {\n"
"            image: url(:/all/img/check_yes.png);\n"
"        }")

        self.verticalLayout_29.addWidget(self.save_res_button_2)

        self.save_txt_button_2 = QCheckBox(self.Save_QF_2)
        self.save_txt_button_2.setObjectName(u"save_txt_button_2")
        self.save_txt_button_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.save_txt_button_2.setStyleSheet(u"QCheckBox {\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 590 10pt \"Nirmala UI\";\n"
"        }\n"
"\n"
"        QCheckBox::indicator {\n"
"            padding-top: 1px;\n"
"padding-left: 10px;\n"
"            width: 40px;\n"
"            height: 30px;\n"
"            border: none;\n"
"        }\n"
"\n"
"        QCheckBox::indicator:unchecked {\n"
"            image: url(:/all/img/check_no.png);\n"
"        }\n"
"\n"
"        QCheckBox::indicator:checked {\n"
"            image: url(:/all/img/check_yes.png);\n"
"        }")

        self.verticalLayout_29.addWidget(self.save_txt_button_2)


        self.verticalLayout_24.addWidget(self.Save_QF_2)

        self.setting_verticalSpacer_2 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_24.addItem(self.setting_verticalSpacer_2)


        self.horizontalLayout_21.addWidget(self.prm_page_2)


        self.verticalLayout_40.addWidget(self.reidContent)

        self.below_2 = QFrame(self.ReidContentBox)
        self.below_2.setObjectName(u"below_2")
        self.below_2.setMinimumSize(QSize(0, 30))
        self.below_2.setMaximumSize(QSize(16777215, 30))
        self.below_2.setFrameShape(QFrame.StyledPanel)
        self.below_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.below_2)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.status_bar_2 = QLabel(self.below_2)
        self.status_bar_2.setObjectName(u"status_bar_2")
        self.status_bar_2.setMinimumSize(QSize(0, 20))
        self.status_bar_2.setStyleSheet(u"font: 700 11pt \"Segoe UI\";\n"
"color: rgba(0, 0, 0, 140);")

        self.verticalLayout_23.addWidget(self.status_bar_2)

        self.frame_size_grip_2 = QFrame(self.below_2)
        self.frame_size_grip_2.setObjectName(u"frame_size_grip_2")
        self.frame_size_grip_2.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip_2.setStyleSheet(u"border-radius:30px;")
        self.frame_size_grip_2.setFrameShape(QFrame.StyledPanel)
        self.frame_size_grip_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_23.addWidget(self.frame_size_grip_2)


        self.verticalLayout_40.addWidget(self.below_2)


        self.verticalLayout_13.addWidget(self.ReidContentBox)


        self.horizontalLayout_106.addWidget(self.ContentBox)


        self.verticalLayout.addWidget(self.Main_QF)

        MainWindow.setCentralWidget(self.Main_QW)

        self.retranslateUi(MainWindow)

        self.ToggleBotton.setDefault(False)
        self.HomeBotton.setDefault(False)
        self.ToggleBotton_6.setDefault(False)
        self.ToggleBotton_2.setDefault(False)
        self.ToggleBotton_3.setDefault(False)
        self.ToggleBotton_4.setDefault(False)
        self.ToggleBotton_5.setDefault(False)
        self.ToggleBotton_12.setDefault(False)
        self.ToggleBotton_7.setDefault(False)
        self.ToggleBotton_8.setDefault(False)
        self.ToggleBotton_9.setDefault(False)
        self.ToggleBotton_10.setDefault(False)
        self.ToggleBotton_11.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Author.setText(QCoreApplication.translate("MainWindow", u"By Lyle", None))
        self.Title.setText(QCoreApplication.translate("MainWindow", u"YCRPer ", None))
        self.ToggleBotton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.HomeBotton.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.DataManageButton.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.DetectButton.setText(QCoreApplication.translate("MainWindow", u"Detect", None))
        self.ReidButton.setText(QCoreApplication.translate("MainWindow", u"Reid", None))
        self.TaskRecordButton.setText(QCoreApplication.translate("MainWindow", u"TaskRecord", None))
        self.VersionLabel.setText(QCoreApplication.translate("MainWindow", u"Version: 1.0", None))
        self.explain_title.setText(QCoreApplication.translate("MainWindow", u"Pedestrian Re-Identification System Based on YOLOv8 and CLIP-ReID", None))
        self.min_sf.setText("")
        self.max_sf.setText("")
        self.close_button.setText("")
        self.detect_char_label.setText(QCoreApplication.translate("MainWindow", u"Detection", None))
        self.detect_set_button.setText("")
        self.src_cam_button.setText(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.src_rtsp_button.setText(QCoreApplication.translate("MainWindow", u"Rtsp", None))
        self.src_file_button.setText(QCoreApplication.translate("MainWindow", u"Local File", None))
        self.class_label.setText(QCoreApplication.translate("MainWindow", u"Total Classes", None))
        self.class_num.setText("")
        self.target_label.setText(QCoreApplication.translate("MainWindow", u"Total Targets", None))
        self.target_num.setText("")
        self.fps_label.setText(QCoreApplication.translate("MainWindow", u"Fps", None))
        self.fps_num.setText("")
        self.pre_video.setText("")
        self.res_video.setText("")
        self.run_button.setText("")
        self.stop_button.setText("")
        self.setting_label.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.ToggleBotton_6.setText(QCoreApplication.translate("MainWindow", u"Model", None))
        self.model_box.setPlaceholderText("")
        self.ToggleBotton_2.setText(QCoreApplication.translate("MainWindow", u"IOU", None))
        self.ToggleBotton_3.setText(QCoreApplication.translate("MainWindow", u"Conf", None))
        self.ToggleBotton_4.setText(QCoreApplication.translate("MainWindow", u"Delay(ms)", None))
        self.ToggleBotton_5.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.save_res_button.setText(QCoreApplication.translate("MainWindow", u"Save MP4/JPG", None))
        self.save_txt_button.setText(QCoreApplication.translate("MainWindow", u"Save Labels(.txt)", None))
        self.status_bar.setText(QCoreApplication.translate("MainWindow", u"Welcome!", None))
        self.explain.setText(QCoreApplication.translate("MainWindow", u"Welcome to YCRPer!", None))

        self.add_button.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Current page:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Total pages:", None))
        self.total_page_num.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.type_label.setText(QCoreApplication.translate("MainWindow", u"Data type\uff1a", None))
        self.type_box.setItemText(0, QCoreApplication.translate("MainWindow", u"All", None))
        self.type_box.setItemText(1, QCoreApplication.translate("MainWindow", u"Video", None))
        self.type_box.setItemText(2, QCoreApplication.translate("MainWindow", u"Picture", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"Title\uff1a", None))
        self.search_button.setText(QCoreApplication.translate("MainWindow", u"Search", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Current page:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Total pages:", None))
        self.total_page_num_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.type_label_2.setText(QCoreApplication.translate("MainWindow", u"Record type\uff1a", None))
        self.type_box_2.setItemText(0, QCoreApplication.translate("MainWindow", u"All", None))
        self.type_box_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Detect", None))
        self.type_box_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Re-identify", None))
        self.title_label_2.setText(QCoreApplication.translate("MainWindow", u"Title\uff1a", None))
        self.search_button_2.setText(QCoreApplication.translate("MainWindow", u"Search", None))

        self.reid_char_label.setText(QCoreApplication.translate("MainWindow", u"Re-identification", None))
        self.reid_set_button.setText("")
        self.target_label_3.setText(QCoreApplication.translate("MainWindow", u"Select target", None))
        self.target_select_button.setText(QCoreApplication.translate("MainWindow", u"File", None))
        self.src_cam_button_2.setText(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.src_rtsp_button_2.setText(QCoreApplication.translate("MainWindow", u"Rtsp", None))
        self.src_file_button_2.setText(QCoreApplication.translate("MainWindow", u"Local File", None))
        self.class_label_2.setText(QCoreApplication.translate("MainWindow", u"Total Classes", None))
        self.class_num_2.setText("")
        self.target_label_2.setText(QCoreApplication.translate("MainWindow", u"Total Targets", None))
        self.target_num_2.setText("")
        self.fps_label_2.setText(QCoreApplication.translate("MainWindow", u"Fps", None))
        self.fps_num_2.setText("")
        self.pre_video_2.setText("")
        self.res_video_2.setText("")
        self.run_button_2.setText("")
        self.stop_button_2.setText("")
        self.setting_label_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.ToggleBotton_12.setText(QCoreApplication.translate("MainWindow", u"ReidModel", None))
        self.reid_model_box.setPlaceholderText("")
        self.ToggleBotton_7.setText(QCoreApplication.translate("MainWindow", u"YolovModel", None))
        self.model_box_2.setPlaceholderText("")
        self.ToggleBotton_8.setText(QCoreApplication.translate("MainWindow", u"IOU", None))
        self.ToggleBotton_9.setText(QCoreApplication.translate("MainWindow", u"Conf", None))
        self.ToggleBotton_10.setText(QCoreApplication.translate("MainWindow", u"Delay(ms)", None))
        self.ToggleBotton_11.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.save_res_button_2.setText(QCoreApplication.translate("MainWindow", u"Save MP4/JPG", None))
        self.save_txt_button_2.setText(QCoreApplication.translate("MainWindow", u"Save Labels(.txt)", None))
        self.status_bar_2.setText(QCoreApplication.translate("MainWindow", u"Welcome!", None))
    # retranslateUi