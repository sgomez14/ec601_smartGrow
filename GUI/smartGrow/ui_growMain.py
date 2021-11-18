# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QStatusBar, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_smartGrowGUI(object):
    def setupUi(self, smartGrowGUI):
        if not smartGrowGUI.objectName():
            smartGrowGUI.setObjectName(u"smartGrowGUI")
        smartGrowGUI.resize(1080, 840)
        self.centralwidget = QWidget(smartGrowGUI)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 50))
        self.header.setMaximumSize(QSize(16777215, 50))
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.logo = QFrame(self.header)
        self.logo.setObjectName(u"logo")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setFrameShape(QFrame.StyledPanel)
        self.logo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.logo)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.logoName = QLabel(self.logo)
        self.logoName.setObjectName(u"logoName")
        font = QFont()
        font.setPointSize(15)
        self.logoName.setFont(font)

        self.horizontalLayout_4.addWidget(self.logoName)

        self.logoIcon = QLabel(self.logo)
        self.logoIcon.setObjectName(u"logoIcon")

        self.horizontalLayout_4.addWidget(self.logoIcon)


        self.horizontalLayout_3.addWidget(self.logo, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.header)

        self.body = QFrame(self.centralwidget)
        self.body.setObjectName(u"body")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.body.sizePolicy().hasHeightForWidth())
        self.body.setSizePolicy(sizePolicy1)
        self.body.setFrameShape(QFrame.StyledPanel)
        self.body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.body)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sidebar = QFrame(self.body)
        self.sidebar.setObjectName(u"sidebar")
        self.sidebar.setMinimumSize(QSize(150, 0))
        self.sidebar.setFrameShape(QFrame.StyledPanel)
        self.sidebar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.sidebar)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.sideButtons = QFrame(self.sidebar)
        self.sideButtons.setObjectName(u"sideButtons")
        sizePolicy.setHeightForWidth(self.sideButtons.sizePolicy().hasHeightForWidth())
        self.sideButtons.setSizePolicy(sizePolicy)
        self.sideButtons.setMinimumSize(QSize(150, 0))
        self.sideButtons.setMaximumSize(QSize(0, 16777215))
        font1 = QFont()
        font1.setPointSize(9)
        self.sideButtons.setFont(font1)
        self.sideButtons.setFrameShape(QFrame.StyledPanel)
        self.sideButtons.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.sideButtons)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.addGrowPodButton = QPushButton(self.sideButtons)
        self.addGrowPodButton.setObjectName(u"addGrowPodButton")
        self.addGrowPodButton.setMinimumSize(QSize(0, 200))
        icon = QIcon()
        icon.addFile(u"resources/icons/plus-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.addGrowPodButton.setIcon(icon)

        self.verticalLayout_4.addWidget(self.addGrowPodButton)

        self.refreshGrowPodInfoButton = QPushButton(self.sideButtons)
        self.refreshGrowPodInfoButton.setObjectName(u"refreshGrowPodInfoButton")
        self.refreshGrowPodInfoButton.setMinimumSize(QSize(0, 200))
        icon1 = QIcon()
        icon1.addFile(u"resources/icons/refresh-cw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.refreshGrowPodInfoButton.setIcon(icon1)
        self.refreshGrowPodInfoButton.setIconSize(QSize(20, 20))

        self.verticalLayout_4.addWidget(self.refreshGrowPodInfoButton)


        self.verticalLayout_3.addWidget(self.sideButtons)


        self.horizontalLayout.addWidget(self.sidebar, 0, Qt.AlignLeft|Qt.AlignTop)

        self.main = QFrame(self.body)
        self.main.setObjectName(u"main")
        sizePolicy1.setHeightForWidth(self.main.sizePolicy().hasHeightForWidth())
        self.main.setSizePolicy(sizePolicy1)
        self.main.setMinimumSize(QSize(800, 0))
        self.main.setFrameShape(QFrame.StyledPanel)
        self.main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.main)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.statusCluster = QFrame(self.main)
        self.statusCluster.setObjectName(u"statusCluster")
        sizePolicy.setHeightForWidth(self.statusCluster.sizePolicy().hasHeightForWidth())
        self.statusCluster.setSizePolicy(sizePolicy)
        self.statusCluster.setMinimumSize(QSize(795, 420))
        font2 = QFont()
        font2.setPointSize(6)
        self.statusCluster.setFont(font2)
        self.statusCluster.setFrameShape(QFrame.StyledPanel)
        self.statusCluster.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.statusCluster)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.statusScrollArea = QScrollArea(self.statusCluster)
        self.statusScrollArea.setObjectName(u"statusScrollArea")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.statusScrollArea.sizePolicy().hasHeightForWidth())
        self.statusScrollArea.setSizePolicy(sizePolicy2)
        self.statusScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.statusScrollArea.setWidgetResizable(True)
        self.statusGrid = QWidget()
        self.statusGrid.setObjectName(u"statusGrid")
        self.statusGrid.setGeometry(QRect(0, 0, 847, 543))
        sizePolicy2.setHeightForWidth(self.statusGrid.sizePolicy().hasHeightForWidth())
        self.statusGrid.setSizePolicy(sizePolicy2)
        self.statusGrid.setMinimumSize(QSize(0, 0))
        self.gridLayout = QGridLayout(self.statusGrid)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.statusScrollArea.setWidget(self.statusGrid)

        self.verticalLayout_6.addWidget(self.statusScrollArea)


        self.verticalLayout_2.addWidget(self.statusCluster)

        self.notifications = QFrame(self.main)
        self.notifications.setObjectName(u"notifications")
        self.notifications.setMinimumSize(QSize(0, 100))
        self.notifications.setMaximumSize(QSize(16777215, 150))
        self.notifications.setFrameShape(QFrame.StyledPanel)
        self.notifications.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.notifications)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.msg = QFrame(self.notifications)
        self.msg.setObjectName(u"msg")
        self.msg.setFrameShape(QFrame.StyledPanel)
        self.msg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.msg)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.textEdit = QTextEdit(self.msg)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_7.addWidget(self.textEdit)


        self.horizontalLayout_2.addWidget(self.msg)

        self.msgClear = QFrame(self.notifications)
        self.msgClear.setObjectName(u"msgClear")
        self.msgClear.setMinimumSize(QSize(150, 0))
        self.msgClear.setMaximumSize(QSize(150, 16777215))
        font3 = QFont()
        font3.setPointSize(1)
        self.msgClear.setFont(font3)
        self.msgClear.setFrameShape(QFrame.StyledPanel)
        self.msgClear.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.msgClear)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.msgClear)
        self.pushButton.setObjectName(u"pushButton")
        font4 = QFont()
        font4.setPointSize(11)
        self.pushButton.setFont(font4)

        self.verticalLayout_5.addWidget(self.pushButton)


        self.horizontalLayout_2.addWidget(self.msgClear)


        self.verticalLayout_2.addWidget(self.notifications)


        self.horizontalLayout.addWidget(self.main)


        self.verticalLayout.addWidget(self.body)

        smartGrowGUI.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(smartGrowGUI)
        self.statusbar.setObjectName(u"statusbar")
        smartGrowGUI.setStatusBar(self.statusbar)

        self.retranslateUi(smartGrowGUI)

        QMetaObject.connectSlotsByName(smartGrowGUI)
    # setupUi

    def retranslateUi(self, smartGrowGUI):
        smartGrowGUI.setWindowTitle(QCoreApplication.translate("smartGrowGUI", u"smartGrowGUI", None))
        self.logoName.setText(QCoreApplication.translate("smartGrowGUI", u"Smart Grow App", None))
        self.logoIcon.setText(QCoreApplication.translate("smartGrowGUI", u"Icon", None))
        self.addGrowPodButton.setText(QCoreApplication.translate("smartGrowGUI", u"  Add Grow Pod", None))
        self.refreshGrowPodInfoButton.setText(QCoreApplication.translate("smartGrowGUI", u"  Refresh Info", None))
        self.pushButton.setText(QCoreApplication.translate("smartGrowGUI", u"Reset Messages", None))
    # retranslateUi

