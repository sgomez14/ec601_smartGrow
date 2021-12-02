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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFormLayout, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QSpinBox,
    QStatusBar, QTextEdit, QVBoxLayout, QWidget)

class Ui_smartGrowGUI(object):
    def setupUi(self, smartGrowGUI):
        if not smartGrowGUI.objectName():
            smartGrowGUI.setObjectName(u"smartGrowGUI")
        smartGrowGUI.resize(1500, 800)
        icon = QIcon()
        icon.addFile(u"resources/icons/hydroponics2.png", QSize(), QIcon.Normal, QIcon.Off)
        smartGrowGUI.setWindowIcon(icon)
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
        self.horizontalSpacer_2 = QSpacerItem(100, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

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
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.logoName = QLabel(self.logo)
        self.logoName.setObjectName(u"logoName")
        font = QFont()
        font.setPointSize(20)
        self.logoName.setFont(font)

        self.horizontalLayout_4.addWidget(self.logoName)


        self.horizontalLayout_3.addWidget(self.logo, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label = QLabel(self.header)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(60, 60))
        self.label.setPixmap(QPixmap(u"resources/icons/hydroponics2.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.horizontalLayout_3.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.header, 0, Qt.AlignHCenter)

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
        self.refreshGrowPodInfoButton = QPushButton(self.sideButtons)
        self.refreshGrowPodInfoButton.setObjectName(u"refreshGrowPodInfoButton")
        self.refreshGrowPodInfoButton.setMinimumSize(QSize(0, 200))
        icon1 = QIcon()
        icon1.addFile(u"resources/icons/refresh-cw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.refreshGrowPodInfoButton.setIcon(icon1)
        self.refreshGrowPodInfoButton.setIconSize(QSize(20, 20))

        self.verticalLayout_4.addWidget(self.refreshGrowPodInfoButton)

        self.addGrowPodButton = QPushButton(self.sideButtons)
        self.addGrowPodButton.setObjectName(u"addGrowPodButton")
        self.addGrowPodButton.setMinimumSize(QSize(0, 200))
        icon2 = QIcon()
        icon2.addFile(u"resources/icons/plus-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.addGrowPodButton.setIcon(icon2)

        self.verticalLayout_4.addWidget(self.addGrowPodButton)


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
        font2.setPointSize(8)
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
        self.statusScrollArea.setFont(font2)
        self.statusScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.statusScrollArea.setWidgetResizable(True)
        self.statusGrid = QWidget()
        self.statusGrid.setObjectName(u"statusGrid")
        self.statusGrid.setGeometry(QRect(0, -1317, 1246, 2485))
        sizePolicy.setHeightForWidth(self.statusGrid.sizePolicy().hasHeightForWidth())
        self.statusGrid.setSizePolicy(sizePolicy)
        self.statusGrid.setMinimumSize(QSize(0, 0))
        self.gridLayout_10 = QGridLayout(self.statusGrid)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.growPodContainer_1 = QGroupBox(self.statusGrid)
        self.growPodContainer_1.setObjectName(u"growPodContainer_1")
        font3 = QFont()
        font3.setPointSize(11)
        self.growPodContainer_1.setFont(font3)
        self.verticalLayout_63 = QVBoxLayout(self.growPodContainer_1)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.growPodInfo_1 = QFrame(self.growPodContainer_1)
        self.growPodInfo_1.setObjectName(u"growPodInfo_1")
        sizePolicy.setHeightForWidth(self.growPodInfo_1.sizePolicy().hasHeightForWidth())
        self.growPodInfo_1.setSizePolicy(sizePolicy)
        font4 = QFont()
        font4.setPointSize(10)
        self.growPodInfo_1.setFont(font4)
        self.growPodInfo_1.setFrameShape(QFrame.StyledPanel)
        self.growPodInfo_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_64 = QVBoxLayout(self.growPodInfo_1)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.growPodInfoFrame_1 = QFrame(self.growPodInfo_1)
        self.growPodInfoFrame_1.setObjectName(u"growPodInfoFrame_1")
        self.growPodInfoFrame_1.setFrameShape(QFrame.StyledPanel)
        self.growPodInfoFrame_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_65 = QVBoxLayout(self.growPodInfoFrame_1)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.plantNameSection_1 = QGroupBox(self.growPodInfoFrame_1)
        self.plantNameSection_1.setObjectName(u"plantNameSection_1")
        sizePolicy.setHeightForWidth(self.plantNameSection_1.sizePolicy().hasHeightForWidth())
        self.plantNameSection_1.setSizePolicy(sizePolicy)
        self.verticalLayout_66 = QVBoxLayout(self.plantNameSection_1)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.plantNameForm_1 = QFormLayout()
        self.plantNameForm_1.setObjectName(u"plantNameForm_1")
        self.plantNameLabel_1 = QLabel(self.plantNameSection_1)
        self.plantNameLabel_1.setObjectName(u"plantNameLabel_1")

        self.plantNameForm_1.setWidget(0, QFormLayout.LabelRole, self.plantNameLabel_1)

        self.plantNameLineEdit_1 = QLineEdit(self.plantNameSection_1)
        self.plantNameLineEdit_1.setObjectName(u"plantNameLineEdit_1")

        self.plantNameForm_1.setWidget(0, QFormLayout.FieldRole, self.plantNameLineEdit_1)

        self.plantTypeLabel_1 = QLabel(self.plantNameSection_1)
        self.plantTypeLabel_1.setObjectName(u"plantTypeLabel_1")

        self.plantNameForm_1.setWidget(1, QFormLayout.LabelRole, self.plantTypeLabel_1)

        self.plantTypeLineEdit_1 = QLineEdit(self.plantNameSection_1)
        self.plantTypeLineEdit_1.setObjectName(u"plantTypeLineEdit_1")

        self.plantNameForm_1.setWidget(1, QFormLayout.FieldRole, self.plantTypeLineEdit_1)


        self.verticalLayout_66.addLayout(self.plantNameForm_1)


        self.verticalLayout_65.addWidget(self.plantNameSection_1)

        self.feedInfoSection_1 = QGroupBox(self.growPodInfoFrame_1)
        self.feedInfoSection_1.setObjectName(u"feedInfoSection_1")
        self.verticalLayout_67 = QVBoxLayout(self.feedInfoSection_1)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.feedInfoForm_1 = QFormLayout()
        self.feedInfoForm_1.setObjectName(u"feedInfoForm_1")
        self.feedScheduleLabel_1 = QLabel(self.feedInfoSection_1)
        self.feedScheduleLabel_1.setObjectName(u"feedScheduleLabel_1")

        self.feedInfoForm_1.setWidget(0, QFormLayout.LabelRole, self.feedScheduleLabel_1)

        self.feedScheduleSpinBox_1 = QSpinBox(self.feedInfoSection_1)
        self.feedScheduleSpinBox_1.setObjectName(u"feedScheduleSpinBox_1")
        self.feedScheduleSpinBox_1.setReadOnly(False)
        self.feedScheduleSpinBox_1.setMaximum(100000)

        self.feedInfoForm_1.setWidget(0, QFormLayout.FieldRole, self.feedScheduleSpinBox_1)

        self.feedDosageLabel_1 = QLabel(self.feedInfoSection_1)
        self.feedDosageLabel_1.setObjectName(u"feedDosageLabel_1")

        self.feedInfoForm_1.setWidget(1, QFormLayout.LabelRole, self.feedDosageLabel_1)

        self.feedDosageDoubleSpinBox_1 = QDoubleSpinBox(self.feedInfoSection_1)
        self.feedDosageDoubleSpinBox_1.setObjectName(u"feedDosageDoubleSpinBox_1")
        self.feedDosageDoubleSpinBox_1.setReadOnly(False)
        self.feedDosageDoubleSpinBox_1.setMaximum(100000.000000000000000)

        self.feedInfoForm_1.setWidget(1, QFormLayout.FieldRole, self.feedDosageDoubleSpinBox_1)


        self.verticalLayout_67.addLayout(self.feedInfoForm_1)


        self.verticalLayout_65.addWidget(self.feedInfoSection_1)

        self.lightScheduleSection_1 = QGroupBox(self.growPodInfoFrame_1)
        self.lightScheduleSection_1.setObjectName(u"lightScheduleSection_1")
        self.verticalLayout_68 = QVBoxLayout(self.lightScheduleSection_1)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.lightScheduleForm_1 = QFormLayout()
        self.lightScheduleForm_1.setObjectName(u"lightScheduleForm_1")
        self.hoursOnLabel_1 = QLabel(self.lightScheduleSection_1)
        self.hoursOnLabel_1.setObjectName(u"hoursOnLabel_1")

        self.lightScheduleForm_1.setWidget(0, QFormLayout.LabelRole, self.hoursOnLabel_1)

        self.hoursOnSpinBox_1 = QSpinBox(self.lightScheduleSection_1)
        self.hoursOnSpinBox_1.setObjectName(u"hoursOnSpinBox_1")
        self.hoursOnSpinBox_1.setReadOnly(False)
        self.hoursOnSpinBox_1.setMaximum(100000)

        self.lightScheduleForm_1.setWidget(0, QFormLayout.FieldRole, self.hoursOnSpinBox_1)

        self.hoursOffLabel_1 = QLabel(self.lightScheduleSection_1)
        self.hoursOffLabel_1.setObjectName(u"hoursOffLabel_1")

        self.lightScheduleForm_1.setWidget(1, QFormLayout.LabelRole, self.hoursOffLabel_1)

        self.hoursOffSpinBox_1 = QSpinBox(self.lightScheduleSection_1)
        self.hoursOffSpinBox_1.setObjectName(u"hoursOffSpinBox_1")
        self.hoursOffSpinBox_1.setReadOnly(False)
        self.hoursOffSpinBox_1.setMaximum(100000)

        self.lightScheduleForm_1.setWidget(1, QFormLayout.FieldRole, self.hoursOffSpinBox_1)


        self.verticalLayout_68.addLayout(self.lightScheduleForm_1)


        self.verticalLayout_65.addWidget(self.lightScheduleSection_1)


        self.verticalLayout_64.addWidget(self.growPodInfoFrame_1)

        self.growPodFeedbackFrame_1 = QFrame(self.growPodInfo_1)
        self.growPodFeedbackFrame_1.setObjectName(u"growPodFeedbackFrame_1")
        self.growPodFeedbackFrame_1.setFrameShape(QFrame.StyledPanel)
        self.growPodFeedbackFrame_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_69 = QVBoxLayout(self.growPodFeedbackFrame_1)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.environmentStatusSection_1 = QGroupBox(self.growPodFeedbackFrame_1)
        self.environmentStatusSection_1.setObjectName(u"environmentStatusSection_1")
        self.verticalLayout_70 = QVBoxLayout(self.environmentStatusSection_1)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.environmentStatusForm_1 = QFormLayout()
        self.environmentStatusForm_1.setObjectName(u"environmentStatusForm_1")
        self.luminosityLabel_1 = QLabel(self.environmentStatusSection_1)
        self.luminosityLabel_1.setObjectName(u"luminosityLabel_1")

        self.environmentStatusForm_1.setWidget(0, QFormLayout.LabelRole, self.luminosityLabel_1)

        self.luminositySpinBox_1 = QSpinBox(self.environmentStatusSection_1)
        self.luminositySpinBox_1.setObjectName(u"luminositySpinBox_1")
        self.luminositySpinBox_1.setFont(font4)
        self.luminositySpinBox_1.setStyleSheet(u"background-color: Gainsboro")
        self.luminositySpinBox_1.setReadOnly(True)
        self.luminositySpinBox_1.setMaximum(100000)

        self.environmentStatusForm_1.setWidget(0, QFormLayout.FieldRole, self.luminositySpinBox_1)

        self.humidityLabel_1 = QLabel(self.environmentStatusSection_1)
        self.humidityLabel_1.setObjectName(u"humidityLabel_1")

        self.environmentStatusForm_1.setWidget(2, QFormLayout.LabelRole, self.humidityLabel_1)

        self.humidityDoubleSpinBox_1 = QDoubleSpinBox(self.environmentStatusSection_1)
        self.humidityDoubleSpinBox_1.setObjectName(u"humidityDoubleSpinBox_1")
        self.humidityDoubleSpinBox_1.setFont(font4)
        self.humidityDoubleSpinBox_1.setStyleSheet(u"background-color: Gainsboro")
        self.humidityDoubleSpinBox_1.setReadOnly(True)
        self.humidityDoubleSpinBox_1.setMaximum(100000.000000000000000)

        self.environmentStatusForm_1.setWidget(2, QFormLayout.FieldRole, self.humidityDoubleSpinBox_1)

        self.temperatureLabel_1 = QLabel(self.environmentStatusSection_1)
        self.temperatureLabel_1.setObjectName(u"temperatureLabel_1")

        self.environmentStatusForm_1.setWidget(1, QFormLayout.LabelRole, self.temperatureLabel_1)

        self.temperatureDoubleSpinBox_1 = QDoubleSpinBox(self.environmentStatusSection_1)
        self.temperatureDoubleSpinBox_1.setObjectName(u"temperatureDoubleSpinBox_1")
        self.temperatureDoubleSpinBox_1.setFont(font4)
        self.temperatureDoubleSpinBox_1.setStyleSheet(u"background-color: Gainsboro")
        self.temperatureDoubleSpinBox_1.setReadOnly(True)
        self.temperatureDoubleSpinBox_1.setMaximum(100000.000000000000000)

        self.environmentStatusForm_1.setWidget(1, QFormLayout.FieldRole, self.temperatureDoubleSpinBox_1)


        self.verticalLayout_70.addLayout(self.environmentStatusForm_1)


        self.verticalLayout_69.addWidget(self.environmentStatusSection_1)

        self.powerStatusSection_1 = QGroupBox(self.growPodFeedbackFrame_1)
        self.powerStatusSection_1.setObjectName(u"powerStatusSection_1")
        self.verticalLayout_71 = QVBoxLayout(self.powerStatusSection_1)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.powerStatusForm_1 = QFormLayout()
        self.powerStatusForm_1.setObjectName(u"powerStatusForm_1")
        self.voltageLabel_1 = QLabel(self.powerStatusSection_1)
        self.voltageLabel_1.setObjectName(u"voltageLabel_1")

        self.powerStatusForm_1.setWidget(0, QFormLayout.LabelRole, self.voltageLabel_1)

        self.voltageDoubleSpinBox_1 = QDoubleSpinBox(self.powerStatusSection_1)
        self.voltageDoubleSpinBox_1.setObjectName(u"voltageDoubleSpinBox_1")
        self.voltageDoubleSpinBox_1.setStyleSheet(u"background-color: Gainsboro")
        self.voltageDoubleSpinBox_1.setReadOnly(True)
        self.voltageDoubleSpinBox_1.setMaximum(100000.000000000000000)

        self.powerStatusForm_1.setWidget(0, QFormLayout.FieldRole, self.voltageDoubleSpinBox_1)

        self.ampsLabel_1 = QLabel(self.powerStatusSection_1)
        self.ampsLabel_1.setObjectName(u"ampsLabel_1")

        self.powerStatusForm_1.setWidget(1, QFormLayout.LabelRole, self.ampsLabel_1)

        self.ampsDoubleSpinBox_1 = QDoubleSpinBox(self.powerStatusSection_1)
        self.ampsDoubleSpinBox_1.setObjectName(u"ampsDoubleSpinBox_1")
        self.ampsDoubleSpinBox_1.setStyleSheet(u"background-color: Gainsboro")
        self.ampsDoubleSpinBox_1.setReadOnly(True)
        self.ampsDoubleSpinBox_1.setMaximum(100000.000000000000000)

        self.powerStatusForm_1.setWidget(1, QFormLayout.FieldRole, self.ampsDoubleSpinBox_1)


        self.verticalLayout_71.addLayout(self.powerStatusForm_1)


        self.verticalLayout_69.addWidget(self.powerStatusSection_1)

        self.pumpStatusSection_1 = QGroupBox(self.growPodFeedbackFrame_1)
        self.pumpStatusSection_1.setObjectName(u"pumpStatusSection_1")
        sizePolicy.setHeightForWidth(self.pumpStatusSection_1.sizePolicy().hasHeightForWidth())
        self.pumpStatusSection_1.setSizePolicy(sizePolicy)
        self.verticalLayout_72 = QVBoxLayout(self.pumpStatusSection_1)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.pumpStatusForm_1 = QFormLayout()
        self.pumpStatusForm_1.setObjectName(u"pumpStatusForm_1")
        self.airPumpLabel_1 = QLabel(self.pumpStatusSection_1)
        self.airPumpLabel_1.setObjectName(u"airPumpLabel_1")

        self.pumpStatusForm_1.setWidget(1, QFormLayout.LabelRole, self.airPumpLabel_1)

        self.airPumpLineEdit_1 = QLineEdit(self.pumpStatusSection_1)
        self.airPumpLineEdit_1.setObjectName(u"airPumpLineEdit_1")
        self.airPumpLineEdit_1.setFont(font4)
        self.airPumpLineEdit_1.setStyleSheet(u"background-color: Gainsboro")
        self.airPumpLineEdit_1.setReadOnly(True)

        self.pumpStatusForm_1.setWidget(1, QFormLayout.FieldRole, self.airPumpLineEdit_1)

        self.sourcePumpLabel_1 = QLabel(self.pumpStatusSection_1)
        self.sourcePumpLabel_1.setObjectName(u"sourcePumpLabel_1")

        self.pumpStatusForm_1.setWidget(2, QFormLayout.LabelRole, self.sourcePumpLabel_1)

        self.sourcePumpLineEdit_1 = QLineEdit(self.pumpStatusSection_1)
        self.sourcePumpLineEdit_1.setObjectName(u"sourcePumpLineEdit_1")
        self.sourcePumpLineEdit_1.setFont(font4)
        self.sourcePumpLineEdit_1.setStyleSheet(u"background-color: Gainsboro")
        self.sourcePumpLineEdit_1.setReadOnly(True)

        self.pumpStatusForm_1.setWidget(2, QFormLayout.FieldRole, self.sourcePumpLineEdit_1)

        self.drainPumpLabel_1 = QLabel(self.pumpStatusSection_1)
        self.drainPumpLabel_1.setObjectName(u"drainPumpLabel_1")

        self.pumpStatusForm_1.setWidget(3, QFormLayout.LabelRole, self.drainPumpLabel_1)

        self.drainPumpLineEdit_1 = QLineEdit(self.pumpStatusSection_1)
        self.drainPumpLineEdit_1.setObjectName(u"drainPumpLineEdit_1")
        self.drainPumpLineEdit_1.setFont(font4)
        self.drainPumpLineEdit_1.setStyleSheet(u"background-color: Gainsboro")
        self.drainPumpLineEdit_1.setReadOnly(True)

        self.pumpStatusForm_1.setWidget(3, QFormLayout.FieldRole, self.drainPumpLineEdit_1)

        self.nutrientsPumpLabel_1 = QLabel(self.pumpStatusSection_1)
        self.nutrientsPumpLabel_1.setObjectName(u"nutrientsPumpLabel_1")

        self.pumpStatusForm_1.setWidget(4, QFormLayout.LabelRole, self.nutrientsPumpLabel_1)

        self.nutrientsPumpLineEdit_1 = QLineEdit(self.pumpStatusSection_1)
        self.nutrientsPumpLineEdit_1.setObjectName(u"nutrientsPumpLineEdit_1")
        self.nutrientsPumpLineEdit_1.setFont(font4)
        self.nutrientsPumpLineEdit_1.setStyleSheet(u"background-color: Gainsboro")
        self.nutrientsPumpLineEdit_1.setReadOnly(True)

        self.pumpStatusForm_1.setWidget(4, QFormLayout.FieldRole, self.nutrientsPumpLineEdit_1)

        self.lightStatusLabel_1 = QLabel(self.pumpStatusSection_1)
        self.lightStatusLabel_1.setObjectName(u"lightStatusLabel_1")

        self.pumpStatusForm_1.setWidget(0, QFormLayout.LabelRole, self.lightStatusLabel_1)

        self.lightStatusLineEdit_1 = QLineEdit(self.pumpStatusSection_1)
        self.lightStatusLineEdit_1.setObjectName(u"lightStatusLineEdit_1")
        self.lightStatusLineEdit_1.setFont(font4)
        self.lightStatusLineEdit_1.setStyleSheet(u"background-color: Gainsboro")
        self.lightStatusLineEdit_1.setReadOnly(True)

        self.pumpStatusForm_1.setWidget(0, QFormLayout.FieldRole, self.lightStatusLineEdit_1)


        self.verticalLayout_72.addLayout(self.pumpStatusForm_1)


        self.verticalLayout_69.addWidget(self.pumpStatusSection_1)


        self.verticalLayout_64.addWidget(self.growPodFeedbackFrame_1)

        self.notesFrame_1 = QFrame(self.growPodInfo_1)
        self.notesFrame_1.setObjectName(u"notesFrame_1")
        self.notesFrame_1.setFrameShape(QFrame.StyledPanel)
        self.notesFrame_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_73 = QVBoxLayout(self.notesFrame_1)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.growPodNotesSection_1 = QGroupBox(self.notesFrame_1)
        self.growPodNotesSection_1.setObjectName(u"growPodNotesSection_1")
        self.growPodNotesSection_1.setMaximumSize(QSize(16777215, 150))
        self.verticalLayout_74 = QVBoxLayout(self.growPodNotesSection_1)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.growPodNotesText_1 = QTextEdit(self.growPodNotesSection_1)
        self.growPodNotesText_1.setObjectName(u"growPodNotesText_1")

        self.verticalLayout_74.addWidget(self.growPodNotesText_1)


        self.verticalLayout_73.addWidget(self.growPodNotesSection_1)


        self.verticalLayout_64.addWidget(self.notesFrame_1, 0, Qt.AlignBottom)


        self.verticalLayout_63.addWidget(self.growPodInfo_1)

        self.growStatusControlButtons_1 = QFrame(self.growPodContainer_1)
        self.growStatusControlButtons_1.setObjectName(u"growStatusControlButtons_1")
        self.growStatusControlButtons_1.setFont(font3)
        self.growStatusControlButtons_1.setFrameShape(QFrame.StyledPanel)
        self.growStatusControlButtons_1.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.growStatusControlButtons_1)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.saveInfoButton_1 = QPushButton(self.growStatusControlButtons_1)
        self.saveInfoButton_1.setObjectName(u"saveInfoButton_1")

        self.gridLayout_7.addWidget(self.saveInfoButton_1, 1, 1, 1, 1)

        self.saveInitializeLaterButton_1 = QPushButton(self.growStatusControlButtons_1)
        self.saveInitializeLaterButton_1.setObjectName(u"saveInitializeLaterButton_1")

        self.gridLayout_7.addWidget(self.saveInitializeLaterButton_1, 0, 1, 1, 1)

        self.initializeGrowPodButton_1 = QPushButton(self.growStatusControlButtons_1)
        self.initializeGrowPodButton_1.setObjectName(u"initializeGrowPodButton_1")

        self.gridLayout_7.addWidget(self.initializeGrowPodButton_1, 0, 0, 1, 1)

        self.editButton_1 = QPushButton(self.growStatusControlButtons_1)
        self.editButton_1.setObjectName(u"editButton_1")

        self.gridLayout_7.addWidget(self.editButton_1, 1, 0, 1, 1)

        self.enableResetButton_1 = QPushButton(self.growStatusControlButtons_1)
        self.enableResetButton_1.setObjectName(u"enableResetButton_1")

        self.gridLayout_7.addWidget(self.enableResetButton_1, 2, 0, 1, 1)

        self.resetGrowPodButton_1 = QPushButton(self.growStatusControlButtons_1)
        self.resetGrowPodButton_1.setObjectName(u"resetGrowPodButton_1")

        self.gridLayout_7.addWidget(self.resetGrowPodButton_1, 2, 1, 1, 1)


        self.verticalLayout_63.addWidget(self.growStatusControlButtons_1)


        self.gridLayout_10.addWidget(self.growPodContainer_1, 0, 0, 1, 1)

        self.growPodContainer_2 = QGroupBox(self.statusGrid)
        self.growPodContainer_2.setObjectName(u"growPodContainer_2")
        font5 = QFont()
        font5.setPointSize(11)
        font5.setBold(False)
        self.growPodContainer_2.setFont(font5)
        self.verticalLayout_75 = QVBoxLayout(self.growPodContainer_2)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.growPodInfo_20 = QFrame(self.growPodContainer_2)
        self.growPodInfo_20.setObjectName(u"growPodInfo_20")
        sizePolicy.setHeightForWidth(self.growPodInfo_20.sizePolicy().hasHeightForWidth())
        self.growPodInfo_20.setSizePolicy(sizePolicy)
        font6 = QFont()
        font6.setPointSize(10)
        font6.setBold(False)
        self.growPodInfo_20.setFont(font6)
        self.growPodInfo_20.setFrameShape(QFrame.StyledPanel)
        self.growPodInfo_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_76 = QVBoxLayout(self.growPodInfo_20)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.growPodInfoFrame_20 = QFrame(self.growPodInfo_20)
        self.growPodInfoFrame_20.setObjectName(u"growPodInfoFrame_20")
        self.growPodInfoFrame_20.setFrameShape(QFrame.StyledPanel)
        self.growPodInfoFrame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_77 = QVBoxLayout(self.growPodInfoFrame_20)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.plantNameSection_20 = QGroupBox(self.growPodInfoFrame_20)
        self.plantNameSection_20.setObjectName(u"plantNameSection_20")
        sizePolicy.setHeightForWidth(self.plantNameSection_20.sizePolicy().hasHeightForWidth())
        self.plantNameSection_20.setSizePolicy(sizePolicy)
        self.verticalLayout_78 = QVBoxLayout(self.plantNameSection_20)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.plantNameForm_20 = QFormLayout()
        self.plantNameForm_20.setObjectName(u"plantNameForm_20")
        self.plantNameLabel_20 = QLabel(self.plantNameSection_20)
        self.plantNameLabel_20.setObjectName(u"plantNameLabel_20")

        self.plantNameForm_20.setWidget(0, QFormLayout.LabelRole, self.plantNameLabel_20)

        self.plantNameLineEdit_20 = QLineEdit(self.plantNameSection_20)
        self.plantNameLineEdit_20.setObjectName(u"plantNameLineEdit_20")

        self.plantNameForm_20.setWidget(0, QFormLayout.FieldRole, self.plantNameLineEdit_20)

        self.plantTypeLabel_20 = QLabel(self.plantNameSection_20)
        self.plantTypeLabel_20.setObjectName(u"plantTypeLabel_20")

        self.plantNameForm_20.setWidget(1, QFormLayout.LabelRole, self.plantTypeLabel_20)

        self.plantTypeLineEdit_20 = QLineEdit(self.plantNameSection_20)
        self.plantTypeLineEdit_20.setObjectName(u"plantTypeLineEdit_20")

        self.plantNameForm_20.setWidget(1, QFormLayout.FieldRole, self.plantTypeLineEdit_20)


        self.verticalLayout_78.addLayout(self.plantNameForm_20)


        self.verticalLayout_77.addWidget(self.plantNameSection_20)

        self.feedInfoSection_20 = QGroupBox(self.growPodInfoFrame_20)
        self.feedInfoSection_20.setObjectName(u"feedInfoSection_20")
        self.verticalLayout_79 = QVBoxLayout(self.feedInfoSection_20)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.feedInfoForm_20 = QFormLayout()
        self.feedInfoForm_20.setObjectName(u"feedInfoForm_20")
        self.feedScheduleLabel_20 = QLabel(self.feedInfoSection_20)
        self.feedScheduleLabel_20.setObjectName(u"feedScheduleLabel_20")

        self.feedInfoForm_20.setWidget(0, QFormLayout.LabelRole, self.feedScheduleLabel_20)

        self.feedScheduleSpinBox_20 = QSpinBox(self.feedInfoSection_20)
        self.feedScheduleSpinBox_20.setObjectName(u"feedScheduleSpinBox_20")
        self.feedScheduleSpinBox_20.setReadOnly(False)
        self.feedScheduleSpinBox_20.setMaximum(100000)

        self.feedInfoForm_20.setWidget(0, QFormLayout.FieldRole, self.feedScheduleSpinBox_20)

        self.feedDosageLabel_20 = QLabel(self.feedInfoSection_20)
        self.feedDosageLabel_20.setObjectName(u"feedDosageLabel_20")

        self.feedInfoForm_20.setWidget(1, QFormLayout.LabelRole, self.feedDosageLabel_20)

        self.feedDosageDoubleSpinBox_20 = QDoubleSpinBox(self.feedInfoSection_20)
        self.feedDosageDoubleSpinBox_20.setObjectName(u"feedDosageDoubleSpinBox_20")
        self.feedDosageDoubleSpinBox_20.setReadOnly(False)
        self.feedDosageDoubleSpinBox_20.setMaximum(100000.000000000000000)

        self.feedInfoForm_20.setWidget(1, QFormLayout.FieldRole, self.feedDosageDoubleSpinBox_20)


        self.verticalLayout_79.addLayout(self.feedInfoForm_20)


        self.verticalLayout_77.addWidget(self.feedInfoSection_20)

        self.lightScheduleSection_20 = QGroupBox(self.growPodInfoFrame_20)
        self.lightScheduleSection_20.setObjectName(u"lightScheduleSection_20")
        self.verticalLayout_80 = QVBoxLayout(self.lightScheduleSection_20)
        self.verticalLayout_80.setObjectName(u"verticalLayout_80")
        self.lightScheduleForm_20 = QFormLayout()
        self.lightScheduleForm_20.setObjectName(u"lightScheduleForm_20")
        self.hoursOnLabel_20 = QLabel(self.lightScheduleSection_20)
        self.hoursOnLabel_20.setObjectName(u"hoursOnLabel_20")

        self.lightScheduleForm_20.setWidget(0, QFormLayout.LabelRole, self.hoursOnLabel_20)

        self.hoursOnSpinBox_20 = QSpinBox(self.lightScheduleSection_20)
        self.hoursOnSpinBox_20.setObjectName(u"hoursOnSpinBox_20")
        self.hoursOnSpinBox_20.setReadOnly(False)
        self.hoursOnSpinBox_20.setMaximum(100000)

        self.lightScheduleForm_20.setWidget(0, QFormLayout.FieldRole, self.hoursOnSpinBox_20)

        self.hoursOffLabel_20 = QLabel(self.lightScheduleSection_20)
        self.hoursOffLabel_20.setObjectName(u"hoursOffLabel_20")

        self.lightScheduleForm_20.setWidget(1, QFormLayout.LabelRole, self.hoursOffLabel_20)

        self.hoursOffSpinBox_20 = QSpinBox(self.lightScheduleSection_20)
        self.hoursOffSpinBox_20.setObjectName(u"hoursOffSpinBox_20")
        self.hoursOffSpinBox_20.setReadOnly(False)
        self.hoursOffSpinBox_20.setMaximum(100000)

        self.lightScheduleForm_20.setWidget(1, QFormLayout.FieldRole, self.hoursOffSpinBox_20)


        self.verticalLayout_80.addLayout(self.lightScheduleForm_20)


        self.verticalLayout_77.addWidget(self.lightScheduleSection_20)


        self.verticalLayout_76.addWidget(self.growPodInfoFrame_20)

        self.growPodFeedbackFrame_20 = QFrame(self.growPodInfo_20)
        self.growPodFeedbackFrame_20.setObjectName(u"growPodFeedbackFrame_20")
        self.growPodFeedbackFrame_20.setFrameShape(QFrame.StyledPanel)
        self.growPodFeedbackFrame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_81 = QVBoxLayout(self.growPodFeedbackFrame_20)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.environmentStatusSection_20 = QGroupBox(self.growPodFeedbackFrame_20)
        self.environmentStatusSection_20.setObjectName(u"environmentStatusSection_20")
        self.verticalLayout_82 = QVBoxLayout(self.environmentStatusSection_20)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.environmentStatusForm_20 = QFormLayout()
        self.environmentStatusForm_20.setObjectName(u"environmentStatusForm_20")
        self.luminosityLabel_20 = QLabel(self.environmentStatusSection_20)
        self.luminosityLabel_20.setObjectName(u"luminosityLabel_20")

        self.environmentStatusForm_20.setWidget(0, QFormLayout.LabelRole, self.luminosityLabel_20)

        self.luminositySpinBox_20 = QSpinBox(self.environmentStatusSection_20)
        self.luminositySpinBox_20.setObjectName(u"luminositySpinBox_20")
        self.luminositySpinBox_20.setFont(font6)
        self.luminositySpinBox_20.setStyleSheet(u"background-color: Gainsboro")
        self.luminositySpinBox_20.setReadOnly(True)
        self.luminositySpinBox_20.setMaximum(100000)

        self.environmentStatusForm_20.setWidget(0, QFormLayout.FieldRole, self.luminositySpinBox_20)

        self.humidityLabel_20 = QLabel(self.environmentStatusSection_20)
        self.humidityLabel_20.setObjectName(u"humidityLabel_20")

        self.environmentStatusForm_20.setWidget(2, QFormLayout.LabelRole, self.humidityLabel_20)

        self.humidityDoubleSpinBox_20 = QDoubleSpinBox(self.environmentStatusSection_20)
        self.humidityDoubleSpinBox_20.setObjectName(u"humidityDoubleSpinBox_20")
        self.humidityDoubleSpinBox_20.setFont(font6)
        self.humidityDoubleSpinBox_20.setStyleSheet(u"background-color: Gainsboro")
        self.humidityDoubleSpinBox_20.setReadOnly(True)
        self.humidityDoubleSpinBox_20.setMaximum(100000.000000000000000)

        self.environmentStatusForm_20.setWidget(2, QFormLayout.FieldRole, self.humidityDoubleSpinBox_20)

        self.temperatureLabel_20 = QLabel(self.environmentStatusSection_20)
        self.temperatureLabel_20.setObjectName(u"temperatureLabel_20")

        self.environmentStatusForm_20.setWidget(1, QFormLayout.LabelRole, self.temperatureLabel_20)

        self.temperatureDoubleSpinBox_20 = QDoubleSpinBox(self.environmentStatusSection_20)
        self.temperatureDoubleSpinBox_20.setObjectName(u"temperatureDoubleSpinBox_20")
        self.temperatureDoubleSpinBox_20.setFont(font6)
        self.temperatureDoubleSpinBox_20.setStyleSheet(u"background-color: Gainsboro")
        self.temperatureDoubleSpinBox_20.setReadOnly(True)
        self.temperatureDoubleSpinBox_20.setMaximum(100000.000000000000000)

        self.environmentStatusForm_20.setWidget(1, QFormLayout.FieldRole, self.temperatureDoubleSpinBox_20)


        self.verticalLayout_82.addLayout(self.environmentStatusForm_20)


        self.verticalLayout_81.addWidget(self.environmentStatusSection_20)

        self.powerStatusSection_20 = QGroupBox(self.growPodFeedbackFrame_20)
        self.powerStatusSection_20.setObjectName(u"powerStatusSection_20")
        self.verticalLayout_83 = QVBoxLayout(self.powerStatusSection_20)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.powerStatusForm_20 = QFormLayout()
        self.powerStatusForm_20.setObjectName(u"powerStatusForm_20")
        self.voltageLabel_20 = QLabel(self.powerStatusSection_20)
        self.voltageLabel_20.setObjectName(u"voltageLabel_20")

        self.powerStatusForm_20.setWidget(0, QFormLayout.LabelRole, self.voltageLabel_20)

        self.voltageDoubleSpinBox_20 = QDoubleSpinBox(self.powerStatusSection_20)
        self.voltageDoubleSpinBox_20.setObjectName(u"voltageDoubleSpinBox_20")
        self.voltageDoubleSpinBox_20.setFont(font6)
        self.voltageDoubleSpinBox_20.setStyleSheet(u"background-color: Gainsboro")
        self.voltageDoubleSpinBox_20.setReadOnly(True)
        self.voltageDoubleSpinBox_20.setMaximum(100000.000000000000000)

        self.powerStatusForm_20.setWidget(0, QFormLayout.FieldRole, self.voltageDoubleSpinBox_20)

        self.ampsLabel_20 = QLabel(self.powerStatusSection_20)
        self.ampsLabel_20.setObjectName(u"ampsLabel_20")

        self.powerStatusForm_20.setWidget(1, QFormLayout.LabelRole, self.ampsLabel_20)

        self.ampsDoubleSpinBox_20 = QDoubleSpinBox(self.powerStatusSection_20)
        self.ampsDoubleSpinBox_20.setObjectName(u"ampsDoubleSpinBox_20")
        self.ampsDoubleSpinBox_20.setFont(font6)
        self.ampsDoubleSpinBox_20.setStyleSheet(u"background-color: Gainsboro")
        self.ampsDoubleSpinBox_20.setReadOnly(True)
        self.ampsDoubleSpinBox_20.setMaximum(100000.000000000000000)

        self.powerStatusForm_20.setWidget(1, QFormLayout.FieldRole, self.ampsDoubleSpinBox_20)


        self.verticalLayout_83.addLayout(self.powerStatusForm_20)


        self.verticalLayout_81.addWidget(self.powerStatusSection_20)

        self.pumpStatusSection_20 = QGroupBox(self.growPodFeedbackFrame_20)
        self.pumpStatusSection_20.setObjectName(u"pumpStatusSection_20")
        sizePolicy.setHeightForWidth(self.pumpStatusSection_20.sizePolicy().hasHeightForWidth())
        self.pumpStatusSection_20.setSizePolicy(sizePolicy)
        self.verticalLayout_84 = QVBoxLayout(self.pumpStatusSection_20)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.pumpStatusForm_20 = QFormLayout()
        self.pumpStatusForm_20.setObjectName(u"pumpStatusForm_20")
        self.airPumpLabel_20 = QLabel(self.pumpStatusSection_20)
        self.airPumpLabel_20.setObjectName(u"airPumpLabel_20")

        self.pumpStatusForm_20.setWidget(1, QFormLayout.LabelRole, self.airPumpLabel_20)

        self.airPumpLineEdit_20 = QLineEdit(self.pumpStatusSection_20)
        self.airPumpLineEdit_20.setObjectName(u"airPumpLineEdit_20")
        self.airPumpLineEdit_20.setFont(font6)
        self.airPumpLineEdit_20.setStyleSheet(u"background-color: Gainsboro")
        self.airPumpLineEdit_20.setReadOnly(True)

        self.pumpStatusForm_20.setWidget(1, QFormLayout.FieldRole, self.airPumpLineEdit_20)

        self.sourcePumpLabel_20 = QLabel(self.pumpStatusSection_20)
        self.sourcePumpLabel_20.setObjectName(u"sourcePumpLabel_20")

        self.pumpStatusForm_20.setWidget(2, QFormLayout.LabelRole, self.sourcePumpLabel_20)

        self.sourcePumpLineEdit_20 = QLineEdit(self.pumpStatusSection_20)
        self.sourcePumpLineEdit_20.setObjectName(u"sourcePumpLineEdit_20")
        self.sourcePumpLineEdit_20.setFont(font6)
        self.sourcePumpLineEdit_20.setStyleSheet(u"background-color: Gainsboro")
        self.sourcePumpLineEdit_20.setReadOnly(True)

        self.pumpStatusForm_20.setWidget(2, QFormLayout.FieldRole, self.sourcePumpLineEdit_20)

        self.drainPumpLabel_20 = QLabel(self.pumpStatusSection_20)
        self.drainPumpLabel_20.setObjectName(u"drainPumpLabel_20")

        self.pumpStatusForm_20.setWidget(3, QFormLayout.LabelRole, self.drainPumpLabel_20)

        self.drainPumpLineEdit_20 = QLineEdit(self.pumpStatusSection_20)
        self.drainPumpLineEdit_20.setObjectName(u"drainPumpLineEdit_20")
        self.drainPumpLineEdit_20.setFont(font6)
        self.drainPumpLineEdit_20.setStyleSheet(u"background-color: Gainsboro")
        self.drainPumpLineEdit_20.setReadOnly(True)

        self.pumpStatusForm_20.setWidget(3, QFormLayout.FieldRole, self.drainPumpLineEdit_20)

        self.nutrientsPumpLabel_20 = QLabel(self.pumpStatusSection_20)
        self.nutrientsPumpLabel_20.setObjectName(u"nutrientsPumpLabel_20")

        self.pumpStatusForm_20.setWidget(4, QFormLayout.LabelRole, self.nutrientsPumpLabel_20)

        self.nutrientsPumpLineEdit_20 = QLineEdit(self.pumpStatusSection_20)
        self.nutrientsPumpLineEdit_20.setObjectName(u"nutrientsPumpLineEdit_20")
        self.nutrientsPumpLineEdit_20.setFont(font6)
        self.nutrientsPumpLineEdit_20.setStyleSheet(u"background-color: Gainsboro")
        self.nutrientsPumpLineEdit_20.setReadOnly(True)

        self.pumpStatusForm_20.setWidget(4, QFormLayout.FieldRole, self.nutrientsPumpLineEdit_20)

        self.lightStatusLabel_20 = QLabel(self.pumpStatusSection_20)
        self.lightStatusLabel_20.setObjectName(u"lightStatusLabel_20")

        self.pumpStatusForm_20.setWidget(0, QFormLayout.LabelRole, self.lightStatusLabel_20)

        self.lightStatusLineEdit_20 = QLineEdit(self.pumpStatusSection_20)
        self.lightStatusLineEdit_20.setObjectName(u"lightStatusLineEdit_20")
        self.lightStatusLineEdit_20.setFont(font6)
        self.lightStatusLineEdit_20.setStyleSheet(u"background-color: Gainsboro")
        self.lightStatusLineEdit_20.setReadOnly(True)

        self.pumpStatusForm_20.setWidget(0, QFormLayout.FieldRole, self.lightStatusLineEdit_20)


        self.verticalLayout_84.addLayout(self.pumpStatusForm_20)


        self.verticalLayout_81.addWidget(self.pumpStatusSection_20)


        self.verticalLayout_76.addWidget(self.growPodFeedbackFrame_20)

        self.notesFrame_20 = QFrame(self.growPodInfo_20)
        self.notesFrame_20.setObjectName(u"notesFrame_20")
        self.notesFrame_20.setFrameShape(QFrame.StyledPanel)
        self.notesFrame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_85 = QVBoxLayout(self.notesFrame_20)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.growPodNotesSection_20 = QGroupBox(self.notesFrame_20)
        self.growPodNotesSection_20.setObjectName(u"growPodNotesSection_20")
        self.growPodNotesSection_20.setMaximumSize(QSize(16777215, 150))
        self.verticalLayout_86 = QVBoxLayout(self.growPodNotesSection_20)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.growPodNotesText_20 = QTextEdit(self.growPodNotesSection_20)
        self.growPodNotesText_20.setObjectName(u"growPodNotesText_20")

        self.verticalLayout_86.addWidget(self.growPodNotesText_20)


        self.verticalLayout_85.addWidget(self.growPodNotesSection_20)


        self.verticalLayout_76.addWidget(self.notesFrame_20, 0, Qt.AlignBottom)


        self.verticalLayout_75.addWidget(self.growPodInfo_20)

        self.growStatusControlButtons_20 = QFrame(self.growPodContainer_2)
        self.growStatusControlButtons_20.setObjectName(u"growStatusControlButtons_20")
        self.growStatusControlButtons_20.setFont(font5)
        self.growStatusControlButtons_20.setFrameShape(QFrame.StyledPanel)
        self.growStatusControlButtons_20.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.growStatusControlButtons_20)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.saveInitializeLaterButton_20 = QPushButton(self.growStatusControlButtons_20)
        self.saveInitializeLaterButton_20.setObjectName(u"saveInitializeLaterButton_20")

        self.gridLayout_8.addWidget(self.saveInitializeLaterButton_20, 0, 1, 1, 1)

        self.initializeGrowPodButton_20 = QPushButton(self.growStatusControlButtons_20)
        self.initializeGrowPodButton_20.setObjectName(u"initializeGrowPodButton_20")

        self.gridLayout_8.addWidget(self.initializeGrowPodButton_20, 0, 0, 1, 1)

        self.editButton_20 = QPushButton(self.growStatusControlButtons_20)
        self.editButton_20.setObjectName(u"editButton_20")

        self.gridLayout_8.addWidget(self.editButton_20, 1, 0, 1, 1)

        self.saveInfoButton_20 = QPushButton(self.growStatusControlButtons_20)
        self.saveInfoButton_20.setObjectName(u"saveInfoButton_20")

        self.gridLayout_8.addWidget(self.saveInfoButton_20, 1, 1, 1, 1)

        self.enableResetButton_20 = QPushButton(self.growStatusControlButtons_20)
        self.enableResetButton_20.setObjectName(u"enableResetButton_20")

        self.gridLayout_8.addWidget(self.enableResetButton_20, 2, 0, 1, 1)

        self.resetGrowPodButton_20 = QPushButton(self.growStatusControlButtons_20)
        self.resetGrowPodButton_20.setObjectName(u"resetGrowPodButton_20")

        self.gridLayout_8.addWidget(self.resetGrowPodButton_20, 2, 1, 1, 1)


        self.verticalLayout_75.addWidget(self.growStatusControlButtons_20)


        self.gridLayout_10.addWidget(self.growPodContainer_2, 0, 2, 1, 1)

        self.growPodContainer_3 = QGroupBox(self.statusGrid)
        self.growPodContainer_3.setObjectName(u"growPodContainer_3")
        self.growPodContainer_3.setFont(font3)
        self.verticalLayout_87 = QVBoxLayout(self.growPodContainer_3)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.growPodInfo_30 = QFrame(self.growPodContainer_3)
        self.growPodInfo_30.setObjectName(u"growPodInfo_30")
        sizePolicy.setHeightForWidth(self.growPodInfo_30.sizePolicy().hasHeightForWidth())
        self.growPodInfo_30.setSizePolicy(sizePolicy)
        self.growPodInfo_30.setFont(font4)
        self.growPodInfo_30.setFrameShape(QFrame.StyledPanel)
        self.growPodInfo_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_88 = QVBoxLayout(self.growPodInfo_30)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.growPodInfoFrame_30 = QFrame(self.growPodInfo_30)
        self.growPodInfoFrame_30.setObjectName(u"growPodInfoFrame_30")
        self.growPodInfoFrame_30.setFrameShape(QFrame.StyledPanel)
        self.growPodInfoFrame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_89 = QVBoxLayout(self.growPodInfoFrame_30)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.plantNameSection_30 = QGroupBox(self.growPodInfoFrame_30)
        self.plantNameSection_30.setObjectName(u"plantNameSection_30")
        sizePolicy.setHeightForWidth(self.plantNameSection_30.sizePolicy().hasHeightForWidth())
        self.plantNameSection_30.setSizePolicy(sizePolicy)
        self.verticalLayout_90 = QVBoxLayout(self.plantNameSection_30)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
        self.plantNameForm_30 = QFormLayout()
        self.plantNameForm_30.setObjectName(u"plantNameForm_30")
        self.plantNameLabel_30 = QLabel(self.plantNameSection_30)
        self.plantNameLabel_30.setObjectName(u"plantNameLabel_30")

        self.plantNameForm_30.setWidget(0, QFormLayout.LabelRole, self.plantNameLabel_30)

        self.plantNameLineEdit_30 = QLineEdit(self.plantNameSection_30)
        self.plantNameLineEdit_30.setObjectName(u"plantNameLineEdit_30")

        self.plantNameForm_30.setWidget(0, QFormLayout.FieldRole, self.plantNameLineEdit_30)

        self.plantTypeLabel_30 = QLabel(self.plantNameSection_30)
        self.plantTypeLabel_30.setObjectName(u"plantTypeLabel_30")

        self.plantNameForm_30.setWidget(1, QFormLayout.LabelRole, self.plantTypeLabel_30)

        self.plantTypeLineEdit_30 = QLineEdit(self.plantNameSection_30)
        self.plantTypeLineEdit_30.setObjectName(u"plantTypeLineEdit_30")

        self.plantNameForm_30.setWidget(1, QFormLayout.FieldRole, self.plantTypeLineEdit_30)


        self.verticalLayout_90.addLayout(self.plantNameForm_30)


        self.verticalLayout_89.addWidget(self.plantNameSection_30)

        self.feedInfoSection_30 = QGroupBox(self.growPodInfoFrame_30)
        self.feedInfoSection_30.setObjectName(u"feedInfoSection_30")
        self.verticalLayout_91 = QVBoxLayout(self.feedInfoSection_30)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.feedInfoForm_30 = QFormLayout()
        self.feedInfoForm_30.setObjectName(u"feedInfoForm_30")
        self.feedScheduleLabel_30 = QLabel(self.feedInfoSection_30)
        self.feedScheduleLabel_30.setObjectName(u"feedScheduleLabel_30")

        self.feedInfoForm_30.setWidget(0, QFormLayout.LabelRole, self.feedScheduleLabel_30)

        self.feedScheduleSpinBox_30 = QSpinBox(self.feedInfoSection_30)
        self.feedScheduleSpinBox_30.setObjectName(u"feedScheduleSpinBox_30")
        self.feedScheduleSpinBox_30.setReadOnly(False)
        self.feedScheduleSpinBox_30.setMaximum(100000)

        self.feedInfoForm_30.setWidget(0, QFormLayout.FieldRole, self.feedScheduleSpinBox_30)

        self.feedDosageLabel_30 = QLabel(self.feedInfoSection_30)
        self.feedDosageLabel_30.setObjectName(u"feedDosageLabel_30")

        self.feedInfoForm_30.setWidget(1, QFormLayout.LabelRole, self.feedDosageLabel_30)

        self.feedDosageDoubleSpinBox_30 = QDoubleSpinBox(self.feedInfoSection_30)
        self.feedDosageDoubleSpinBox_30.setObjectName(u"feedDosageDoubleSpinBox_30")
        self.feedDosageDoubleSpinBox_30.setReadOnly(False)
        self.feedDosageDoubleSpinBox_30.setMaximum(100000.000000000000000)

        self.feedInfoForm_30.setWidget(1, QFormLayout.FieldRole, self.feedDosageDoubleSpinBox_30)


        self.verticalLayout_91.addLayout(self.feedInfoForm_30)


        self.verticalLayout_89.addWidget(self.feedInfoSection_30)

        self.lightScheduleSection_30 = QGroupBox(self.growPodInfoFrame_30)
        self.lightScheduleSection_30.setObjectName(u"lightScheduleSection_30")
        self.verticalLayout_92 = QVBoxLayout(self.lightScheduleSection_30)
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")
        self.lightScheduleForm_30 = QFormLayout()
        self.lightScheduleForm_30.setObjectName(u"lightScheduleForm_30")
        self.hoursOnLabel_30 = QLabel(self.lightScheduleSection_30)
        self.hoursOnLabel_30.setObjectName(u"hoursOnLabel_30")

        self.lightScheduleForm_30.setWidget(0, QFormLayout.LabelRole, self.hoursOnLabel_30)

        self.hoursOnSpinBox_30 = QSpinBox(self.lightScheduleSection_30)
        self.hoursOnSpinBox_30.setObjectName(u"hoursOnSpinBox_30")
        self.hoursOnSpinBox_30.setFont(font4)
        self.hoursOnSpinBox_30.setStyleSheet(u"")
        self.hoursOnSpinBox_30.setReadOnly(False)
        self.hoursOnSpinBox_30.setMaximum(100000)

        self.lightScheduleForm_30.setWidget(0, QFormLayout.FieldRole, self.hoursOnSpinBox_30)

        self.hoursOffLabel_30 = QLabel(self.lightScheduleSection_30)
        self.hoursOffLabel_30.setObjectName(u"hoursOffLabel_30")

        self.lightScheduleForm_30.setWidget(1, QFormLayout.LabelRole, self.hoursOffLabel_30)

        self.hoursOffSpinBox_30 = QSpinBox(self.lightScheduleSection_30)
        self.hoursOffSpinBox_30.setObjectName(u"hoursOffSpinBox_30")
        self.hoursOffSpinBox_30.setFont(font4)
        self.hoursOffSpinBox_30.setStyleSheet(u"")
        self.hoursOffSpinBox_30.setReadOnly(False)
        self.hoursOffSpinBox_30.setMaximum(100000)

        self.lightScheduleForm_30.setWidget(1, QFormLayout.FieldRole, self.hoursOffSpinBox_30)


        self.verticalLayout_92.addLayout(self.lightScheduleForm_30)


        self.verticalLayout_89.addWidget(self.lightScheduleSection_30)


        self.verticalLayout_88.addWidget(self.growPodInfoFrame_30)

        self.growPodFeedbackFrame_30 = QFrame(self.growPodInfo_30)
        self.growPodFeedbackFrame_30.setObjectName(u"growPodFeedbackFrame_30")
        self.growPodFeedbackFrame_30.setFrameShape(QFrame.StyledPanel)
        self.growPodFeedbackFrame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_93 = QVBoxLayout(self.growPodFeedbackFrame_30)
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.environmentStatusSection_30 = QGroupBox(self.growPodFeedbackFrame_30)
        self.environmentStatusSection_30.setObjectName(u"environmentStatusSection_30")
        self.verticalLayout_94 = QVBoxLayout(self.environmentStatusSection_30)
        self.verticalLayout_94.setObjectName(u"verticalLayout_94")
        self.environmentStatusForm_30 = QFormLayout()
        self.environmentStatusForm_30.setObjectName(u"environmentStatusForm_30")
        self.luminosityLabel_30 = QLabel(self.environmentStatusSection_30)
        self.luminosityLabel_30.setObjectName(u"luminosityLabel_30")

        self.environmentStatusForm_30.setWidget(0, QFormLayout.LabelRole, self.luminosityLabel_30)

        self.luminositySpinBox_30 = QSpinBox(self.environmentStatusSection_30)
        self.luminositySpinBox_30.setObjectName(u"luminositySpinBox_30")
        self.luminositySpinBox_30.setFont(font4)
        self.luminositySpinBox_30.setStyleSheet(u"background-color: Gainsboro")
        self.luminositySpinBox_30.setReadOnly(True)
        self.luminositySpinBox_30.setMaximum(100000)

        self.environmentStatusForm_30.setWidget(0, QFormLayout.FieldRole, self.luminositySpinBox_30)

        self.humidityLabel_30 = QLabel(self.environmentStatusSection_30)
        self.humidityLabel_30.setObjectName(u"humidityLabel_30")

        self.environmentStatusForm_30.setWidget(2, QFormLayout.LabelRole, self.humidityLabel_30)

        self.humidityDoubleSpinBox_30 = QDoubleSpinBox(self.environmentStatusSection_30)
        self.humidityDoubleSpinBox_30.setObjectName(u"humidityDoubleSpinBox_30")
        self.humidityDoubleSpinBox_30.setFont(font4)
        self.humidityDoubleSpinBox_30.setStyleSheet(u"background-color: Gainsboro")
        self.humidityDoubleSpinBox_30.setReadOnly(True)
        self.humidityDoubleSpinBox_30.setMaximum(100000.000000000000000)

        self.environmentStatusForm_30.setWidget(2, QFormLayout.FieldRole, self.humidityDoubleSpinBox_30)

        self.temperatureLabel_30 = QLabel(self.environmentStatusSection_30)
        self.temperatureLabel_30.setObjectName(u"temperatureLabel_30")

        self.environmentStatusForm_30.setWidget(1, QFormLayout.LabelRole, self.temperatureLabel_30)

        self.temperatureDoubleSpinBox_30 = QDoubleSpinBox(self.environmentStatusSection_30)
        self.temperatureDoubleSpinBox_30.setObjectName(u"temperatureDoubleSpinBox_30")
        self.temperatureDoubleSpinBox_30.setFont(font4)
        self.temperatureDoubleSpinBox_30.setStyleSheet(u"background-color: Gainsboro")
        self.temperatureDoubleSpinBox_30.setReadOnly(True)
        self.temperatureDoubleSpinBox_30.setMaximum(100000.000000000000000)

        self.environmentStatusForm_30.setWidget(1, QFormLayout.FieldRole, self.temperatureDoubleSpinBox_30)


        self.verticalLayout_94.addLayout(self.environmentStatusForm_30)


        self.verticalLayout_93.addWidget(self.environmentStatusSection_30)

        self.powerStatusSection_30 = QGroupBox(self.growPodFeedbackFrame_30)
        self.powerStatusSection_30.setObjectName(u"powerStatusSection_30")
        self.verticalLayout_95 = QVBoxLayout(self.powerStatusSection_30)
        self.verticalLayout_95.setObjectName(u"verticalLayout_95")
        self.powerStatusForm_30 = QFormLayout()
        self.powerStatusForm_30.setObjectName(u"powerStatusForm_30")
        self.voltageLabel_30 = QLabel(self.powerStatusSection_30)
        self.voltageLabel_30.setObjectName(u"voltageLabel_30")

        self.powerStatusForm_30.setWidget(0, QFormLayout.LabelRole, self.voltageLabel_30)

        self.voltageDoubleSpinBox_30 = QDoubleSpinBox(self.powerStatusSection_30)
        self.voltageDoubleSpinBox_30.setObjectName(u"voltageDoubleSpinBox_30")
        self.voltageDoubleSpinBox_30.setFont(font4)
        self.voltageDoubleSpinBox_30.setStyleSheet(u"background-color: Gainsboro")
        self.voltageDoubleSpinBox_30.setReadOnly(True)
        self.voltageDoubleSpinBox_30.setMaximum(100000.000000000000000)

        self.powerStatusForm_30.setWidget(0, QFormLayout.FieldRole, self.voltageDoubleSpinBox_30)

        self.ampsLabel_30 = QLabel(self.powerStatusSection_30)
        self.ampsLabel_30.setObjectName(u"ampsLabel_30")

        self.powerStatusForm_30.setWidget(1, QFormLayout.LabelRole, self.ampsLabel_30)

        self.ampsDoubleSpinBox_30 = QDoubleSpinBox(self.powerStatusSection_30)
        self.ampsDoubleSpinBox_30.setObjectName(u"ampsDoubleSpinBox_30")
        self.ampsDoubleSpinBox_30.setFont(font4)
        self.ampsDoubleSpinBox_30.setStyleSheet(u"background-color: Gainsboro")
        self.ampsDoubleSpinBox_30.setReadOnly(True)
        self.ampsDoubleSpinBox_30.setMaximum(100000.000000000000000)

        self.powerStatusForm_30.setWidget(1, QFormLayout.FieldRole, self.ampsDoubleSpinBox_30)


        self.verticalLayout_95.addLayout(self.powerStatusForm_30)


        self.verticalLayout_93.addWidget(self.powerStatusSection_30)

        self.pumpStatusSection_30 = QGroupBox(self.growPodFeedbackFrame_30)
        self.pumpStatusSection_30.setObjectName(u"pumpStatusSection_30")
        sizePolicy.setHeightForWidth(self.pumpStatusSection_30.sizePolicy().hasHeightForWidth())
        self.pumpStatusSection_30.setSizePolicy(sizePolicy)
        self.verticalLayout_96 = QVBoxLayout(self.pumpStatusSection_30)
        self.verticalLayout_96.setObjectName(u"verticalLayout_96")
        self.pumpStatusForm_30 = QFormLayout()
        self.pumpStatusForm_30.setObjectName(u"pumpStatusForm_30")
        self.airPumpLabel_30 = QLabel(self.pumpStatusSection_30)
        self.airPumpLabel_30.setObjectName(u"airPumpLabel_30")

        self.pumpStatusForm_30.setWidget(1, QFormLayout.LabelRole, self.airPumpLabel_30)

        self.airPumpLineEdit_30 = QLineEdit(self.pumpStatusSection_30)
        self.airPumpLineEdit_30.setObjectName(u"airPumpLineEdit_30")
        self.airPumpLineEdit_30.setFont(font4)
        self.airPumpLineEdit_30.setStyleSheet(u"background-color: Gainsboro")
        self.airPumpLineEdit_30.setReadOnly(True)

        self.pumpStatusForm_30.setWidget(1, QFormLayout.FieldRole, self.airPumpLineEdit_30)

        self.sourcePumpLabel_30 = QLabel(self.pumpStatusSection_30)
        self.sourcePumpLabel_30.setObjectName(u"sourcePumpLabel_30")

        self.pumpStatusForm_30.setWidget(2, QFormLayout.LabelRole, self.sourcePumpLabel_30)

        self.sourcePumpLineEdit_30 = QLineEdit(self.pumpStatusSection_30)
        self.sourcePumpLineEdit_30.setObjectName(u"sourcePumpLineEdit_30")
        self.sourcePumpLineEdit_30.setFont(font4)
        self.sourcePumpLineEdit_30.setStyleSheet(u"background-color: Gainsboro")
        self.sourcePumpLineEdit_30.setReadOnly(True)

        self.pumpStatusForm_30.setWidget(2, QFormLayout.FieldRole, self.sourcePumpLineEdit_30)

        self.drainPumpLabel_30 = QLabel(self.pumpStatusSection_30)
        self.drainPumpLabel_30.setObjectName(u"drainPumpLabel_30")

        self.pumpStatusForm_30.setWidget(3, QFormLayout.LabelRole, self.drainPumpLabel_30)

        self.drainPumpLineEdit_30 = QLineEdit(self.pumpStatusSection_30)
        self.drainPumpLineEdit_30.setObjectName(u"drainPumpLineEdit_30")
        self.drainPumpLineEdit_30.setFont(font4)
        self.drainPumpLineEdit_30.setStyleSheet(u"background-color: Gainsboro")
        self.drainPumpLineEdit_30.setReadOnly(True)

        self.pumpStatusForm_30.setWidget(3, QFormLayout.FieldRole, self.drainPumpLineEdit_30)

        self.nutrientsPumpLabel_30 = QLabel(self.pumpStatusSection_30)
        self.nutrientsPumpLabel_30.setObjectName(u"nutrientsPumpLabel_30")

        self.pumpStatusForm_30.setWidget(4, QFormLayout.LabelRole, self.nutrientsPumpLabel_30)

        self.nutrientsPumpLineEdit_30 = QLineEdit(self.pumpStatusSection_30)
        self.nutrientsPumpLineEdit_30.setObjectName(u"nutrientsPumpLineEdit_30")
        self.nutrientsPumpLineEdit_30.setFont(font4)
        self.nutrientsPumpLineEdit_30.setStyleSheet(u"background-color: Gainsboro")
        self.nutrientsPumpLineEdit_30.setReadOnly(True)

        self.pumpStatusForm_30.setWidget(4, QFormLayout.FieldRole, self.nutrientsPumpLineEdit_30)

        self.lightStatusLabel_30 = QLabel(self.pumpStatusSection_30)
        self.lightStatusLabel_30.setObjectName(u"lightStatusLabel_30")

        self.pumpStatusForm_30.setWidget(0, QFormLayout.LabelRole, self.lightStatusLabel_30)

        self.lightStatusLineEdit_30 = QLineEdit(self.pumpStatusSection_30)
        self.lightStatusLineEdit_30.setObjectName(u"lightStatusLineEdit_30")
        self.lightStatusLineEdit_30.setFont(font4)
        self.lightStatusLineEdit_30.setStyleSheet(u"background-color: Gainsboro")
        self.lightStatusLineEdit_30.setReadOnly(True)

        self.pumpStatusForm_30.setWidget(0, QFormLayout.FieldRole, self.lightStatusLineEdit_30)


        self.verticalLayout_96.addLayout(self.pumpStatusForm_30)


        self.verticalLayout_93.addWidget(self.pumpStatusSection_30)


        self.verticalLayout_88.addWidget(self.growPodFeedbackFrame_30)

        self.notesFrame_30 = QFrame(self.growPodInfo_30)
        self.notesFrame_30.setObjectName(u"notesFrame_30")
        self.notesFrame_30.setFrameShape(QFrame.StyledPanel)
        self.notesFrame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_97 = QVBoxLayout(self.notesFrame_30)
        self.verticalLayout_97.setObjectName(u"verticalLayout_97")
        self.growPodNotesSection_30 = QGroupBox(self.notesFrame_30)
        self.growPodNotesSection_30.setObjectName(u"growPodNotesSection_30")
        self.growPodNotesSection_30.setMaximumSize(QSize(16777215, 150))
        self.verticalLayout_98 = QVBoxLayout(self.growPodNotesSection_30)
        self.verticalLayout_98.setObjectName(u"verticalLayout_98")
        self.growPodNotesText_30 = QTextEdit(self.growPodNotesSection_30)
        self.growPodNotesText_30.setObjectName(u"growPodNotesText_30")

        self.verticalLayout_98.addWidget(self.growPodNotesText_30)


        self.verticalLayout_97.addWidget(self.growPodNotesSection_30)


        self.verticalLayout_88.addWidget(self.notesFrame_30, 0, Qt.AlignBottom)


        self.verticalLayout_87.addWidget(self.growPodInfo_30)

        self.growStatusControlButtons_30 = QFrame(self.growPodContainer_3)
        self.growStatusControlButtons_30.setObjectName(u"growStatusControlButtons_30")
        self.growStatusControlButtons_30.setFont(font3)
        self.growStatusControlButtons_30.setFrameShape(QFrame.StyledPanel)
        self.growStatusControlButtons_30.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.growStatusControlButtons_30)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.saveInfoButton_30 = QPushButton(self.growStatusControlButtons_30)
        self.saveInfoButton_30.setObjectName(u"saveInfoButton_30")

        self.gridLayout_9.addWidget(self.saveInfoButton_30, 1, 1, 1, 1)

        self.saveInitializeLaterButton_30 = QPushButton(self.growStatusControlButtons_30)
        self.saveInitializeLaterButton_30.setObjectName(u"saveInitializeLaterButton_30")

        self.gridLayout_9.addWidget(self.saveInitializeLaterButton_30, 0, 1, 1, 1)

        self.initializeGrowPodButton_30 = QPushButton(self.growStatusControlButtons_30)
        self.initializeGrowPodButton_30.setObjectName(u"initializeGrowPodButton_30")

        self.gridLayout_9.addWidget(self.initializeGrowPodButton_30, 0, 0, 1, 1)

        self.editButton_30 = QPushButton(self.growStatusControlButtons_30)
        self.editButton_30.setObjectName(u"editButton_30")

        self.gridLayout_9.addWidget(self.editButton_30, 1, 0, 1, 1)

        self.enableResetButton_30 = QPushButton(self.growStatusControlButtons_30)
        self.enableResetButton_30.setObjectName(u"enableResetButton_30")

        self.gridLayout_9.addWidget(self.enableResetButton_30, 2, 0, 1, 1)

        self.resetGrowPodButton_30 = QPushButton(self.growStatusControlButtons_30)
        self.resetGrowPodButton_30.setObjectName(u"resetGrowPodButton_30")

        self.gridLayout_9.addWidget(self.resetGrowPodButton_30, 2, 1, 1, 1)


        self.verticalLayout_87.addWidget(self.growStatusControlButtons_30)


        self.gridLayout_10.addWidget(self.growPodContainer_3, 1, 0, 1, 1)

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
        self.messageArea = QFrame(self.notifications)
        self.messageArea.setObjectName(u"messageArea")
        self.messageArea.setFrameShape(QFrame.StyledPanel)
        self.messageArea.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.messageArea)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 11, 0)
        self.messageAreaLabel = QLabel(self.messageArea)
        self.messageAreaLabel.setObjectName(u"messageAreaLabel")
        font7 = QFont()
        font7.setPointSize(16)
        self.messageAreaLabel.setFont(font7)

        self.verticalLayout_7.addWidget(self.messageAreaLabel)

        self.messageAreaText = QTextEdit(self.messageArea)
        self.messageAreaText.setObjectName(u"messageAreaText")
        self.messageAreaText.setFont(font1)

        self.verticalLayout_7.addWidget(self.messageAreaText)


        self.horizontalLayout_2.addWidget(self.messageArea)

        self.msgClear = QFrame(self.notifications)
        self.msgClear.setObjectName(u"msgClear")
        self.msgClear.setMinimumSize(QSize(150, 0))
        self.msgClear.setMaximumSize(QSize(150, 16777215))
        font8 = QFont()
        font8.setPointSize(1)
        self.msgClear.setFont(font8)
        self.msgClear.setFrameShape(QFrame.StyledPanel)
        self.msgClear.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.msgClear)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.messageAreaClearButton = QPushButton(self.msgClear)
        self.messageAreaClearButton.setObjectName(u"messageAreaClearButton")
        self.messageAreaClearButton.setFont(font3)

        self.verticalLayout_5.addWidget(self.messageAreaClearButton)


        self.horizontalLayout_2.addWidget(self.msgClear)


        self.verticalLayout_2.addWidget(self.notifications)


        self.horizontalLayout.addWidget(self.main)


        self.verticalLayout.addWidget(self.body)

        smartGrowGUI.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(smartGrowGUI)
        self.statusbar.setObjectName(u"statusbar")
        smartGrowGUI.setStatusBar(self.statusbar)

        self.retranslateUi(smartGrowGUI)

        self.saveInitializeLaterButton_1.setDefault(False)
        self.saveInitializeLaterButton_20.setDefault(False)
        self.saveInitializeLaterButton_30.setDefault(False)


        QMetaObject.connectSlotsByName(smartGrowGUI)
    # setupUi

    def retranslateUi(self, smartGrowGUI):
        smartGrowGUI.setWindowTitle(QCoreApplication.translate("smartGrowGUI", u"smartGrowGUI", None))
        self.logoName.setText(QCoreApplication.translate("smartGrowGUI", u"Smart Grow App", None))
        self.label.setText("")
        self.refreshGrowPodInfoButton.setText(QCoreApplication.translate("smartGrowGUI", u"  Refresh Info", None))
        self.addGrowPodButton.setText(QCoreApplication.translate("smartGrowGUI", u"  Add Grow Pod", None))
        self.growPodContainer_1.setTitle(QCoreApplication.translate("smartGrowGUI", u"Grow Pod 1 Status View", None))
        self.plantNameSection_1.setTitle(QCoreApplication.translate("smartGrowGUI", u"Plant Name and Type", None))
        self.plantNameLabel_1.setText(QCoreApplication.translate("smartGrowGUI", u"Plant Name", None))
        self.plantTypeLabel_1.setText(QCoreApplication.translate("smartGrowGUI", u"Plant Type", None))
        self.feedInfoSection_1.setTitle(QCoreApplication.translate("smartGrowGUI", u"Feeding Information", None))
        self.feedScheduleLabel_1.setText(QCoreApplication.translate("smartGrowGUI", u"Feed Schedule (every x minutes)", None))
        self.feedDosageLabel_1.setText(QCoreApplication.translate("smartGrowGUI", u"Feed Dosage (mL)", None))
        self.lightScheduleSection_1.setTitle(QCoreApplication.translate("smartGrowGUI", u"Light Schedule", None))
        self.hoursOnLabel_1.setText(QCoreApplication.translate("smartGrowGUI", u"Minutes On", None))
        self.hoursOffLabel_1.setText(QCoreApplication.translate("smartGrowGUI", u"Minutes Off", None))
        self.environmentStatusSection_1.setTitle(QCoreApplication.translate("smartGrowGUI", u"Environment", None))
        self.luminosityLabel_1.setText(QCoreApplication.translate("smartGrowGUI", u"Luminosity (LUX)", None))
        self.humidityLabel_1.setText(QCoreApplication.translate("smartGrowGUI", u"Humidity (%)", None))
        self.temperatureLabel_1.setText(QCoreApplication.translate("smartGrowGUI", u"Temperature (F)", None))
        self.powerStatusSection_1.setTitle(QCoreApplication.translate("smartGrowGUI", u"Power", None))
        self.voltageLabel_1.setText(QCoreApplication.translate("smartGrowGUI", u"Voltage (mV)", None))
        self.ampsLabel_1.setText(QCoreApplication.translate("smartGrowGUI", u"Amps (mA)", None))
        self.pumpStatusSection_1.setTitle(QCoreApplication.translate("smartGrowGUI", u"Light and Pumps", None))
        self.airPumpLabel_1.setText(QCoreApplication.translate("smartGrowGUI", u"Air Pump", None))
        self.sourcePumpLabel_1.setText(QCoreApplication.translate("smartGrowGUI", u"Source Pump", None))
        self.drainPumpLabel_1.setText(QCoreApplication.translate("smartGrowGUI", u"Drain Pump", None))
        self.nutrientsPumpLabel_1.setText(QCoreApplication.translate("smartGrowGUI", u"Nutrients Pump", None))
        self.lightStatusLabel_1.setText(QCoreApplication.translate("smartGrowGUI", u"Light Status", None))
        self.growPodNotesSection_1.setTitle(QCoreApplication.translate("smartGrowGUI", u"Notes", None))
        self.saveInfoButton_1.setText(QCoreApplication.translate("smartGrowGUI", u"Save Info", None))
        self.saveInitializeLaterButton_1.setText(QCoreApplication.translate("smartGrowGUI", u"Save Info, Initialize Later", None))
        self.initializeGrowPodButton_1.setText(QCoreApplication.translate("smartGrowGUI", u"Initilize Grow Pod", None))
        self.editButton_1.setText(QCoreApplication.translate("smartGrowGUI", u"Edit", None))
        self.enableResetButton_1.setText(QCoreApplication.translate("smartGrowGUI", u"Enable Reset Button", None))
        self.resetGrowPodButton_1.setText(QCoreApplication.translate("smartGrowGUI", u"Reset Grow Pod", None))
        self.growPodContainer_2.setTitle(QCoreApplication.translate("smartGrowGUI", u"Grow Pod 2 Status View", None))
        self.plantNameSection_20.setTitle(QCoreApplication.translate("smartGrowGUI", u"Plant Name and Type", None))
        self.plantNameLabel_20.setText(QCoreApplication.translate("smartGrowGUI", u"Plant Name", None))
        self.plantTypeLabel_20.setText(QCoreApplication.translate("smartGrowGUI", u"Plant Type", None))
        self.feedInfoSection_20.setTitle(QCoreApplication.translate("smartGrowGUI", u"Feeding Information", None))
        self.feedScheduleLabel_20.setText(QCoreApplication.translate("smartGrowGUI", u"Feed Schedule (every x minutes)", None))
        self.feedDosageLabel_20.setText(QCoreApplication.translate("smartGrowGUI", u"Feed Dosage (mL)", None))
        self.lightScheduleSection_20.setTitle(QCoreApplication.translate("smartGrowGUI", u"Light Schedule", None))
        self.hoursOnLabel_20.setText(QCoreApplication.translate("smartGrowGUI", u"Minutes On", None))
        self.hoursOffLabel_20.setText(QCoreApplication.translate("smartGrowGUI", u"Minutes Off", None))
        self.environmentStatusSection_20.setTitle(QCoreApplication.translate("smartGrowGUI", u"Environment", None))
        self.luminosityLabel_20.setText(QCoreApplication.translate("smartGrowGUI", u"Luminosity (LUX)", None))
        self.humidityLabel_20.setText(QCoreApplication.translate("smartGrowGUI", u"Humidity (%)", None))
        self.temperatureLabel_20.setText(QCoreApplication.translate("smartGrowGUI", u"Temperature (F)", None))
        self.powerStatusSection_20.setTitle(QCoreApplication.translate("smartGrowGUI", u"Power", None))
        self.voltageLabel_20.setText(QCoreApplication.translate("smartGrowGUI", u"Voltage (mV)", None))
        self.ampsLabel_20.setText(QCoreApplication.translate("smartGrowGUI", u"Amps (mA)", None))
        self.pumpStatusSection_20.setTitle(QCoreApplication.translate("smartGrowGUI", u"Light and Pumps", None))
        self.airPumpLabel_20.setText(QCoreApplication.translate("smartGrowGUI", u"Air Pump", None))
        self.sourcePumpLabel_20.setText(QCoreApplication.translate("smartGrowGUI", u"Source Pump", None))
        self.drainPumpLabel_20.setText(QCoreApplication.translate("smartGrowGUI", u"Drain Pump", None))
        self.nutrientsPumpLabel_20.setText(QCoreApplication.translate("smartGrowGUI", u"Nutrients Pump", None))
        self.lightStatusLabel_20.setText(QCoreApplication.translate("smartGrowGUI", u"Light Status", None))
        self.growPodNotesSection_20.setTitle(QCoreApplication.translate("smartGrowGUI", u"Notes", None))
        self.saveInitializeLaterButton_20.setText(QCoreApplication.translate("smartGrowGUI", u"Save Info, Initialize Later", None))
        self.initializeGrowPodButton_20.setText(QCoreApplication.translate("smartGrowGUI", u"Initilize Grow Pod", None))
        self.editButton_20.setText(QCoreApplication.translate("smartGrowGUI", u"Edit", None))
        self.saveInfoButton_20.setText(QCoreApplication.translate("smartGrowGUI", u"Save Info", None))
        self.enableResetButton_20.setText(QCoreApplication.translate("smartGrowGUI", u"Enable Reset Button", None))
        self.resetGrowPodButton_20.setText(QCoreApplication.translate("smartGrowGUI", u"Reset Grow Pod", None))
        self.growPodContainer_3.setTitle(QCoreApplication.translate("smartGrowGUI", u"Grow Pod 3 Status View", None))
        self.plantNameSection_30.setTitle(QCoreApplication.translate("smartGrowGUI", u"Plant Name and Type", None))
        self.plantNameLabel_30.setText(QCoreApplication.translate("smartGrowGUI", u"Plant Name", None))
        self.plantTypeLabel_30.setText(QCoreApplication.translate("smartGrowGUI", u"Plant Type", None))
        self.feedInfoSection_30.setTitle(QCoreApplication.translate("smartGrowGUI", u"Feeding Information", None))
        self.feedScheduleLabel_30.setText(QCoreApplication.translate("smartGrowGUI", u"Feed Schedule (every x minutes)", None))
        self.feedDosageLabel_30.setText(QCoreApplication.translate("smartGrowGUI", u"Feed Dosage (mL)", None))
        self.lightScheduleSection_30.setTitle(QCoreApplication.translate("smartGrowGUI", u"Light Schedule", None))
        self.hoursOnLabel_30.setText(QCoreApplication.translate("smartGrowGUI", u"Minutes On", None))
        self.hoursOffLabel_30.setText(QCoreApplication.translate("smartGrowGUI", u"Minutes Off", None))
        self.environmentStatusSection_30.setTitle(QCoreApplication.translate("smartGrowGUI", u"Environment", None))
        self.luminosityLabel_30.setText(QCoreApplication.translate("smartGrowGUI", u"Luminosity (LUX)", None))
        self.humidityLabel_30.setText(QCoreApplication.translate("smartGrowGUI", u"Humidity (%)", None))
        self.temperatureLabel_30.setText(QCoreApplication.translate("smartGrowGUI", u"Temperature (F)", None))
        self.powerStatusSection_30.setTitle(QCoreApplication.translate("smartGrowGUI", u"Power", None))
        self.voltageLabel_30.setText(QCoreApplication.translate("smartGrowGUI", u"Voltage (mV)", None))
        self.ampsLabel_30.setText(QCoreApplication.translate("smartGrowGUI", u"Amps (mA)", None))
        self.pumpStatusSection_30.setTitle(QCoreApplication.translate("smartGrowGUI", u"Light and Pumps", None))
        self.airPumpLabel_30.setText(QCoreApplication.translate("smartGrowGUI", u"Air Pump", None))
        self.sourcePumpLabel_30.setText(QCoreApplication.translate("smartGrowGUI", u"Source Pump", None))
        self.drainPumpLabel_30.setText(QCoreApplication.translate("smartGrowGUI", u"Drain Pump", None))
        self.nutrientsPumpLabel_30.setText(QCoreApplication.translate("smartGrowGUI", u"Nutrients Pump", None))
        self.lightStatusLabel_30.setText(QCoreApplication.translate("smartGrowGUI", u"Light Status", None))
        self.growPodNotesSection_30.setTitle(QCoreApplication.translate("smartGrowGUI", u"Notes", None))
        self.saveInfoButton_30.setText(QCoreApplication.translate("smartGrowGUI", u"Save Info", None))
        self.saveInitializeLaterButton_30.setText(QCoreApplication.translate("smartGrowGUI", u"Save Info, Initialize Later", None))
        self.initializeGrowPodButton_30.setText(QCoreApplication.translate("smartGrowGUI", u"Initilize Grow Pod", None))
        self.editButton_30.setText(QCoreApplication.translate("smartGrowGUI", u"Edit", None))
        self.enableResetButton_30.setText(QCoreApplication.translate("smartGrowGUI", u"Enable Reset Button", None))
        self.resetGrowPodButton_30.setText(QCoreApplication.translate("smartGrowGUI", u"Reset Grow Pod", None))
        self.messageAreaLabel.setText(QCoreApplication.translate("smartGrowGUI", u"Messages", None))
        self.messageAreaClearButton.setText(QCoreApplication.translate("smartGrowGUI", u"Reset Messages", None))
    # retranslateUi

