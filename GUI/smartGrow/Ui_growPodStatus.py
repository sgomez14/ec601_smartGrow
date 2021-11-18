# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'growPodStatus.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

class Ui_growPodStatus(object):
    def setupUi(self, growPodStatus):
        if not growPodStatus.objectName():
            growPodStatus.setObjectName(u"growPodStatus")
        growPodStatus.resize(480, 640)
        growPodStatus.setMinimumSize(QSize(480, 640))
        self.label = QLabel(growPodStatus)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 130, 47, 13))

        self.retranslateUi(growPodStatus)

        QMetaObject.connectSlotsByName(growPodStatus)
    # setupUi

    def retranslateUi(self, growPodStatus):
        growPodStatus.setWindowTitle(QCoreApplication.translate("growPodStatus", u"Form", None))
        self.label.setText(QCoreApplication.translate("growPodStatus", u"Info about growPod", None))
    # retranslateUi

