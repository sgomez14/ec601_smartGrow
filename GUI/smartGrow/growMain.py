import sys
from PySide6.QtWidgets import *  # QApplication, QMainWindow, QPushButton, QDialog
from ui_growMain import Ui_smartGrowGUI
from ui_addGrowPod import Ui_addGrowPodDialog
from Ui_growPodStatus import Ui_growPodStatus


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_smartGrowGUI()
        self.ui.setupUi(self)

        # set parameter for Grow Pod Status View Grid
        self.gridMaxColumns = 2
        self.gridCurrentCol = 0
        self.gridCurrentRow = 0

        self.growPodStatusList = []

        self.ui.addGrowPodButton.clicked.connect(self.addGrowPodButtonPushed)
        # self.ui.addGrowPodButton.pressed().connect(self.addGrowPodButtonPushed)

    def addGrowPodButtonPushed(self):
        print("addGrowPodButton Pushed!")
        growPod = GrowPodStatus()

        # adding new grow pod status views in a grid manner
        if self.gridCurrentCol < self.gridMaxColumns:
            self.ui.gridLayout.addWidget(growPod, self.gridCurrentRow, self.gridCurrentCol)
            self.gridCurrentCol += 1
            if self.gridCurrentCol >= self.gridMaxColumns:
                self.gridCurrentCol = 0
                self.gridCurrentRow += 1

    def addGrowPodStatusToCluster(self):
        self.growPodStatusWidget = GrowPodStatus()
        self.growPodStatusWidget.show()


class GrowPodDialog(QDialog):
    def __init__(self):
        super(GrowPodDialog, self).__init__()
        self.ui = Ui_addGrowPodDialog()
        self.ui.setupUi(self)

        self.addGrowPodFormClosed = False

        self.ui.addGrowStatusButton.clicked.connect(self.addGrowStatusButtonClicked)

    def addGrowStatusButtonClicked(self):
        print("addGrowStatusButton CLicked")
        self.addGrowPodFormClosed = True
        self.close()  # done(0)


class GrowPodStatus(QWidget):
    def __init__(self):
        super(GrowPodStatus, self).__init__()
        self.ui = Ui_growPodStatus()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    # window.ui.addGrowPodButton.connect(addGrowPodButtonPushed())
    sys.exit(app.exec())
