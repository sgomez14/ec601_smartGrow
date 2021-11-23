import sys
from PySide6.QtWidgets import *  # QApplication, QMainWindow, QPushButton, QMessageBox
from ui_growMain import Ui_smartGrowGUI
from ui_addGrowPod import Ui_addGrowPodDialog
from Ui_growPodStatus import Ui_growPodStatus
from growpod import *

# TODO: function that will load previous growPod status
# TODO: need function that updates the GUI with new information

DEVELOPMENT = True

def confirmInitializeGrowPod(growPod):
    # code example for MessageBox from QT PySide6 documentation
    msgBox = QMessageBox()
    msgBox.setWindowTitle("GrowPod Initialization")
    msgBox.setIcon(QMessageBox.Question)
    msgBox.setText("Grow Pod Initialization Confirmation")
    msgBox.setInformativeText(f"Do you wish to initialize GrowPod{growPod.uniqueID}?")
    msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
    msgBox.setDefaultButton(QMessageBox.Cancel)
    ret = msgBox.exec()

    if ret == QMessageBox.Yes:
        return True
    else:
        False


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_smartGrowGUI()
        self.ui.setupUi(self)

        # set parameter for Grow Pod Status View Grid
        self.gridMaxColumns = 2
        self.gridCurrentCol = 1
        self.gridCurrentRow = 1

        self.growPod1 = GrowPod()
        self.growPod2 = GrowPod()
        self.growPod3 = GrowPod()

        # give unique IDs to each grow pod object
        self.growPod1.uniqueID = 1
        self.growPod2.uniqueID = 2
        self.growPod3.uniqueID = 3

        # set grow pod IP Addresses
        self.growPod1.ipAddress = ipAddress1
        self.growPod2.ipAddress = ipAddress2
        self.growPod3.ipAddress = ipAddress3

        self.growPodsList = [self.growPod1, self.growPod2, self.growPod3]

        # resetting the JSON file during development
        if DEVELOPMENT:
            saveGrowPodJSON(self.growPodsList)
        else:
            print("loading JSON file")
            # TODO: code for loading JSON and initializing the growPods

        # styling for when form is saved
        self.formFieldColorSaved = "background-color: Gainsboro"

        # styling for when form is being edited
        self.formFieldColorEditing = "background-color: white"

        # message for invalid field
        self.invalidFieldMessage = "Field invalid in Form"

        # hide the Edit and Save Info Buttons initially
        self.ui.editButton_1.setHidden(True)
        self.ui.editButton_20.setHidden(True)
        self.ui.editButton_30.setHidden(True)

        self.ui.saveInfoButton_1.setHidden(True)
        self.ui.saveInfoButton_20.setHidden(True)
        self.ui.saveInfoButton_30.setHidden(True)

        # hide the grow pod status sections until after user initializes a grow pod
        self.ui.environmentStatusSection_1.setHidden(True)
        self.ui.environmentStatusSection_20.setHidden(True)
        self.ui.environmentStatusSection_30.setHidden(True)

        self.ui.powerStatusSection_1.setHidden(True)
        self.ui.powerStatusSection_20.setHidden(True)
        self.ui.powerStatusSection_30.setHidden(True)

        self.ui.pumpStatusSection_1.setHidden(True)
        self.ui.pumpStatusSection_20.setHidden(True)
        self.ui.pumpStatusSection_30.setHidden(True)

        # connect initializeGrowPodButton signals to actions
        self.ui.initializeGrowPodButton_1.clicked.connect(self.initializeGrowPodButton_1_Clicked)
        self.ui.initializeGrowPodButton_20.clicked.connect(self.initializeGrowPodButton_20_Clicked)
        self.ui.initializeGrowPodButton_30.clicked.connect(self.initializeGrowPodButton_30_Clicked)

        # connect saveInitializeLater signals to actions
        self.ui.saveInitializeLaterButton_1.clicked.connect(self.saveInitializeLaterButton_1_Clicked)
        self.ui.saveInitializeLaterButton_20.clicked.connect(self.saveInitializeLaterButton_20_Clicked)
        self.ui.saveInitializeLaterButton_30.clicked.connect(self.saveInitializeLaterButton_30_Clicked)

        # connect editButton signals to actions
        self.ui.editButton_1.clicked.connect(self.editButton_1_Clicked)
        self.ui.editButton_20.clicked.connect(self.editButton_20_Clicked)
        self.ui.editButton_30.clicked.connect(self.editButton_30_Clicked)

        # connect saveInfo signals to actions
        self.ui.saveInfoButton_1.clicked.connect(self.saveInfoButton_1_Clicked)
        self.ui.saveInfoButton_20.clicked.connect(self.saveInfoButton_20_Clicked)
        self.ui.saveInfoButton_30.clicked.connect(self.saveInfoButton_30_Clicked)

    def initializeGrowPodButton_1_Clicked(self):
        print("initial grow pod button 1 clicked")

        # save information on form
        self.growPod1.plantName = self.ui.plantNameLineEdit_1.text()
        self.growPod1.plantType = self.ui.plantTypeLineEdit_1.text()
        self.growPod1.feedSchedule = self.ui.feedScheduleSpinBox_1.value()
        self.growPod1.feedDosage = self.ui.feedDosageDoubleSpinBox_1.value()
        self.growPod1.lightHoursOn = self.ui.hoursOnSpinBox_1.value()
        self.growPod1.lightHoursOff = self.ui.hoursOffSpinBox_1.value()
        self.growPod1.notes = self.ui.growPodNotesText_1.toPlainText()

        # logic for checking if fields are empty
        if invalidSetupInfo(self.growPod1):
            print(self.invalidFieldMessage + " 1")
            self.ui.messageAreaText.append(self.invalidFieldMessage + " 1")
        else:
            # logic to confirm that user wants to initialize grow pod
            if confirmInitializeGrowPod(self.growPod1):
                print("user wants to initialize growPod")

                # code section for updating the UI
                # show the grow pod status sections
                self.ui.environmentStatusSection_1.setHidden(False)
                self.ui.powerStatusSection_1.setHidden(False)
                self.ui.pumpStatusSection_1.setHidden(False)

                # show the edit and save info buttons
                self.ui.editButton_1.setHidden(False)
                self.ui.editButton_1.setEnabled(True)
                self.ui.saveInfoButton_1.setHidden(False)
                self.ui.saveInfoButton_1.setEnabled(False)

                # hide the initializeGrowPod and saveInitializeLater buttons
                self.ui.initializeGrowPodButton_1.setHidden(True)
                self.ui.saveInitializeLaterButton_1.setHidden(True)

                # set PlantName, Feeding Info, and Light Schedule sections to read only
                self.ui.plantNameLineEdit_1.setReadOnly(True)
                self.ui.plantTypeLineEdit_1.setReadOnly(True)

                self.ui.feedScheduleSpinBox_1.setReadOnly(True)
                self.ui.feedDosageDoubleSpinBox_1.setReadOnly(True)

                self.ui.hoursOnSpinBox_1.setReadOnly(True)
                self.ui.hoursOffSpinBox_1.setReadOnly(True)

                # notes section to read only
                self.ui.growPodNotesText_1.setReadOnly(True)

                # change the background color of fields to indicate they are read only
                self.ui.plantNameLineEdit_1.setStyleSheet(self.formFieldColorSaved)
                self.ui.plantTypeLineEdit_1.setStyleSheet(self.formFieldColorSaved)

                self.ui.feedScheduleSpinBox_1.setStyleSheet(self.formFieldColorSaved)
                self.ui.feedDosageDoubleSpinBox_1.setStyleSheet(self.formFieldColorSaved)

                self.ui.hoursOnSpinBox_1.setStyleSheet(self.formFieldColorSaved)
                self.ui.hoursOffSpinBox_1.setStyleSheet(self.formFieldColorSaved)

                self.ui.growPodNotesText_1.setStyleSheet(self.formFieldColorSaved)

                # rename the group box title with new plant name
                self.ui.growPodContainer_1.setTitle(self.growPod1.plantName + " Status View")

                # save the new information to JSON
                saveGrowPodJSON(self.growPodsList)

                # print setup info when button pressed
                self.growPod1.printSetupInfo()

                # TODO: here is the section for sending information over to microcontroller
                # sendPacketToGrowPod(growPod, command)

            else:
                print("user does not want to initialize growPod")



    def saveInitializeLaterButton_1_Clicked(self):
        print("save initialize Later button 1 clicked")

        # save information on form
        self.growPod1.plantName = self.ui.plantNameLineEdit_1.text()
        self.growPod1.plantType = self.ui.plantTypeLineEdit_1.text()
        self.growPod1.feedSchedule = self.ui.feedScheduleSpinBox_1.value()
        self.growPod1.feedDosage = self.ui.feedDosageDoubleSpinBox_1.value()
        self.growPod1.lightHoursOn = self.ui.hoursOnSpinBox_1.value()
        self.growPod1.lightHoursOff = self.ui.hoursOffSpinBox_1.value()
        self.growPod1.notes = self.ui.growPodNotesText_1.toPlainText()

        # logic for checking if fields are empty
        if invalidSetupInfo(self.growPod1):
            print(self.invalidFieldMessage + " 1")
            self.ui.messageAreaText.append(self.invalidFieldMessage + " 1")
        else:
            # code section for updating the UI

            # disable saveInitializeLater Button
            self.ui.saveInitializeLaterButton_1.setEnabled(False)

            # set PlantName, Feeding Info, and Light Schedule sections to read only
            self.ui.plantNameLineEdit_1.setReadOnly(True)
            self.ui.plantTypeLineEdit_1.setReadOnly(True)

            self.ui.feedScheduleSpinBox_1.setReadOnly(True)
            self.ui.feedDosageDoubleSpinBox_1.setReadOnly(True)

            self.ui.hoursOnSpinBox_1.setReadOnly(True)
            self.ui.hoursOffSpinBox_1.setReadOnly(True)

            # notes section to read only
            self.ui.growPodNotesText_1.setReadOnly(True)

            # change the background color of fields to indicate they are read only
            self.ui.plantNameLineEdit_1.setStyleSheet(self.formFieldColorSaved)
            self.ui.plantTypeLineEdit_1.setStyleSheet(self.formFieldColorSaved)

            self.ui.feedScheduleSpinBox_1.setStyleSheet(self.formFieldColorSaved)
            self.ui.feedDosageDoubleSpinBox_1.setStyleSheet(self.formFieldColorSaved)

            self.ui.hoursOnSpinBox_1.setStyleSheet(self.formFieldColorSaved)
            self.ui.hoursOffSpinBox_1.setStyleSheet(self.formFieldColorSaved)

            self.ui.growPodNotesText_1.setStyleSheet(self.formFieldColorSaved)

            # rename the group box title with new plant name
            self.ui.growPodContainer_1.setTitle(self.growPod1.plantName + " Status View")

            # show edit info button so that user can edit setup information later
            self.ui.editButton_1.setHidden(False)
            self.ui.editButton_1.setEnabled(True)

            # save the new information to JSON
            saveGrowPodJSON(self.growPodsList)

            # print setup info when button pressed
            self.growPod1.printSetupInfo()

    def editButton_1_Clicked(self):
        print("edit button 1 clicked")

        # disable edit button
        self.ui.editButton_1.setEnabled(False)

        # enable save info button
        self.ui.saveInitializeLaterButton_1.setEnabled(True)
        self.ui.saveInfoButton_1.setEnabled(True)

        # make PlantName, Feeding Info, and Light Schedule editable again
        self.ui.plantNameLineEdit_1.setReadOnly(False)
        self.ui.plantTypeLineEdit_1.setReadOnly(False)

        self.ui.feedScheduleSpinBox_1.setReadOnly(False)
        self.ui.feedDosageDoubleSpinBox_1.setReadOnly(False)

        self.ui.hoursOnSpinBox_1.setReadOnly(False)
        self.ui.hoursOffSpinBox_1.setReadOnly(False)

        # notes section editable
        self.ui.growPodNotesText_1.setReadOnly(False)

        # change the background color of fields to indicate they are editable again
        self.ui.plantNameLineEdit_1.setStyleSheet(self.formFieldColorEditing)
        self.ui.plantTypeLineEdit_1.setStyleSheet(self.formFieldColorEditing)

        self.ui.feedScheduleSpinBox_1.setStyleSheet(self.formFieldColorEditing)
        self.ui.feedDosageDoubleSpinBox_1.setStyleSheet(self.formFieldColorEditing)

        self.ui.hoursOnSpinBox_1.setStyleSheet(self.formFieldColorEditing)
        self.ui.hoursOffSpinBox_1.setStyleSheet(self.formFieldColorEditing)

        self.ui.growPodNotesText_1.setStyleSheet(self.formFieldColorEditing)


    def saveInfoButton_1_Clicked(self):
        print("save info button 1 clicked")

        # create temp growPod object to check if info has been updated
        tempGrowPod = GrowPod()

        # save information on form
        tempGrowPod.plantName = self.ui.plantNameLineEdit_1.text()
        tempGrowPod.plantType = self.ui.plantTypeLineEdit_1.text()
        tempGrowPod.feedSchedule = self.ui.feedScheduleSpinBox_1.value()
        tempGrowPod.feedDosage = self.ui.feedDosageDoubleSpinBox_1.value()
        tempGrowPod.lightHoursOn = self.ui.hoursOnSpinBox_1.value()
        tempGrowPod.lightHoursOff = self.ui.hoursOffSpinBox_1.value()
        tempGrowPod.notes = self.ui.growPodNotesText_1.toPlainText()

        # logic for checking if fields are empty
        if invalidSetupInfo(tempGrowPod):
            print(self.invalidFieldMessage + " 1")
            self.ui.messageAreaText.append(self.invalidFieldMessage + " 1")
        else:
            # code section for updating the UI
            # set PlantName, Feeding Info, and Light Schedule sections to read only
            self.ui.plantNameLineEdit_1.setReadOnly(True)
            self.ui.plantTypeLineEdit_1.setReadOnly(True)

            self.ui.feedScheduleSpinBox_1.setReadOnly(True)
            self.ui.feedDosageDoubleSpinBox_1.setReadOnly(True)

            self.ui.hoursOnSpinBox_1.setReadOnly(True)
            self.ui.hoursOffSpinBox_1.setReadOnly(True)

            # notes section to read only
            self.ui.growPodNotesText_1.setReadOnly(True)

            # change the background color of fields to indicate they are read only
            self.ui.plantNameLineEdit_1.setStyleSheet(self.formFieldColorSaved)
            self.ui.plantTypeLineEdit_1.setStyleSheet(self.formFieldColorSaved)

            self.ui.feedScheduleSpinBox_1.setStyleSheet(self.formFieldColorSaved)
            self.ui.feedDosageDoubleSpinBox_1.setStyleSheet(self.formFieldColorSaved)

            self.ui.hoursOnSpinBox_1.setStyleSheet(self.formFieldColorSaved)
            self.ui.hoursOffSpinBox_1.setStyleSheet(self.formFieldColorSaved)

            self.ui.growPodNotesText_1.setStyleSheet(self.formFieldColorSaved)

            # re-enable edit button
            self.ui.editButton_1.setEnabled(True)

            # re-disable save button
            self.ui.saveInfoButton_1.setEnabled(False)

            # logic to see if the setup values changed. if yes, then send update packet to microcontroller
            if growPodSetupInfoSame(tempGrowPod, self.growPod1):
                # nothing to change
                print("all setup info remained the same")
            else:
                # logic to update grow pod
                print("setup info changed")

                # TODO: section for sending packet to microcontroller
                # sendPacketToGrowPod(growPod, command)

        # save information on form
        self.growPod1.plantName = self.ui.plantNameLineEdit_1.text()
        self.growPod1.plantType = self.ui.plantTypeLineEdit_1.text()
        self.growPod1.feedSchedule = self.ui.feedScheduleSpinBox_1.value()
        self.growPod1.feedDosage = self.ui.feedDosageDoubleSpinBox_1.value()
        self.growPod1.lightHoursOn = self.ui.hoursOnSpinBox_1.value()
        self.growPod1.lightHoursOff = self.ui.hoursOffSpinBox_1.value()
        self.growPod1.notes = self.ui.growPodNotesText_1.toPlainText()

        # rename the group box title with new plant name
        self.ui.growPodContainer_1.setTitle(self.growPod1.plantName + " Status View")

        # save the new information to JSON
        saveGrowPodJSON(self.growPodsList)

        # printing for debugging
        self.growPod1.printSetupInfo()


    def initializeGrowPodButton_20_Clicked(self):
        print("initial grow pod button 2 clicked")

        # save information on form
        self.growPod2.plantName = self.ui.plantNameLineEdit_20.text()
        self.growPod2.plantType = self.ui.plantTypeLineEdit_20.text()
        self.growPod2.feedSchedule = self.ui.feedScheduleSpinBox_20.value()
        self.growPod2.feedDosage = self.ui.feedDosageDoubleSpinBox_20.value()
        self.growPod2.lightHoursOn = self.ui.hoursOnSpinBox_20.value()
        self.growPod2.lightHoursOff = self.ui.hoursOffSpinBox_20.value()
        self.growPod2.notes = self.ui.growPodNotesText_20.toPlainText()

        # logic for checking if fields are empty
        if invalidSetupInfo(self.growPod2):
            print(self.invalidFieldMessage + " 2")
            self.ui.messageAreaText.append(self.invalidFieldMessage + " 2")
        else:
            # logic to confirm that user wants to initialize grow pod
            if confirmInitializeGrowPod(self.growPod2):
                print("user wants to initialize growPod")

                # code section for updating the UI
                # show the grow pod status sections
                self.ui.environmentStatusSection_20.setHidden(False)
                self.ui.powerStatusSection_20.setHidden(False)
                self.ui.pumpStatusSection_20.setHidden(False)

                # show the edit and save info buttons
                self.ui.editButton_20.setHidden(False)
                self.ui.editButton_20.setEnabled(True)
                self.ui.saveInfoButton_20.setHidden(False)
                self.ui.saveInfoButton_20.setEnabled(False)

                # hide the initializeGrowPod and saveInitializeLater buttons
                self.ui.initializeGrowPodButton_20.setHidden(True)
                self.ui.saveInitializeLaterButton_20.setHidden(True)

                # set PlantName, Feeding Info, and Light Schedule sections to read only
                self.ui.plantNameLineEdit_20.setReadOnly(True)
                self.ui.plantTypeLineEdit_20.setReadOnly(True)

                self.ui.feedScheduleSpinBox_20.setReadOnly(True)
                self.ui.feedDosageDoubleSpinBox_20.setReadOnly(True)

                self.ui.hoursOnSpinBox_20.setReadOnly(True)
                self.ui.hoursOffSpinBox_20.setReadOnly(True)

                # notes section to read only
                self.ui.growPodNotesText_20.setReadOnly(True)

                # change the background color of fields to indicate they are read only
                self.ui.plantNameLineEdit_20.setStyleSheet(self.formFieldColorSaved)
                self.ui.plantTypeLineEdit_1.setStyleSheet(self.formFieldColorSaved)

                self.ui.feedScheduleSpinBox_20.setStyleSheet(self.formFieldColorSaved)
                self.ui.feedDosageDoubleSpinBox_20.setStyleSheet(self.formFieldColorSaved)

                self.ui.hoursOnSpinBox_20.setStyleSheet(self.formFieldColorSaved)
                self.ui.hoursOffSpinBox_20.setStyleSheet(self.formFieldColorSaved)

                self.ui.growPodNotesText_20.setStyleSheet(self.formFieldColorSaved)

                # rename the group box title with new plant name
                self.ui.growPodContainer_2.setTitle(self.growPod2.plantName + " Status View")

                # save the new information to JSON
                saveGrowPodJSON(self.growPodsList)

                # print setup info when button pressed
                self.growPod2.printSetupInfo()

                # TODO: here is the section for sending information over to microcontroller
                # sendPacketToGrowPod(growPod, command)

            else:
                print("user does not want to initialize growPod")


############ start here ##############


    def saveInitializeLaterButton_20_Clicked(self):
        print("save initialize Later button 20 clicked")

        # save information on form
        self.growPod2.plantName = self.ui.plantNameLineEdit_20.text()
        self.growPod2.plantType = self.ui.plantTypeLineEdit_20.text()
        self.growPod2.feedSchedule = self.ui.feedScheduleSpinBox_20.value()
        self.growPod2.feedDosage = self.ui.feedDosageDoubleSpinBox_20.value()
        self.growPod2.lightHoursOn = self.ui.hoursOnSpinBox_20.value()
        self.growPod2.lightHoursOff = self.ui.hoursOffSpinBox_20.value()
        self.growPod2.notes = self.ui.growPodNotesText_20.toPlainText()

        # logic for checking if fields are empty
        if invalidSetupInfo(self.growPod2):
            print(self.invalidFieldMessage + " 2")
            self.ui.messageAreaText.append(self.invalidFieldMessage + " 2")
        else:
            # code section for updating the UI

            # disable saveInitializeLater Button
            self.ui.saveInitializeLaterButton_20.setEnabled(False)

            # set PlantName, Feeding Info, and Light Schedule sections to read only
            self.ui.plantNameLineEdit_20.setReadOnly(True)
            self.ui.plantTypeLineEdit_20.setReadOnly(True)

            self.ui.feedScheduleSpinBox_20.setReadOnly(True)
            self.ui.feedDosageDoubleSpinBox_20.setReadOnly(True)

            self.ui.hoursOnSpinBox_20.setReadOnly(True)
            self.ui.hoursOffSpinBox_20.setReadOnly(True)

            # notes section to read only
            self.ui.growPodNotesText_20.setReadOnly(True)

            # change the background color of fields to indicate they are read only
            self.ui.plantNameLineEdit_20.setStyleSheet(self.formFieldColorSaved)
            self.ui.plantTypeLineEdit_20.setStyleSheet(self.formFieldColorSaved)

            self.ui.feedScheduleSpinBox_20.setStyleSheet(self.formFieldColorSaved)
            self.ui.feedDosageDoubleSpinBox_20.setStyleSheet(self.formFieldColorSaved)

            self.ui.hoursOnSpinBox_20.setStyleSheet(self.formFieldColorSaved)
            self.ui.hoursOffSpinBox_20.setStyleSheet(self.formFieldColorSaved)

            self.ui.growPodNotesText_20.setStyleSheet(self.formFieldColorSaved)

            # rename the group box title with new plant name
            self.ui.growPodContainer_2.setTitle(self.growPod2.plantName + " Status View")

            # show edit info button so that user can edit setup information later
            self.ui.editButton_20.setHidden(False)
            self.ui.editButton_20.setEnabled(True)

            # save the new information to JSON
            saveGrowPodJSON(self.growPodsList)

            # print setup info when button pressed
            self.growPod2.printSetupInfo()

    def editButton_20_Clicked(self):
        print("edit button 20 clicked")

        # disable edit button
        self.ui.editButton_20.setEnabled(False)

        # enable save info button
        self.ui.saveInitializeLaterButton_20.setEnabled(True)
        self.ui.saveInfoButton_20.setEnabled(True)

        # make PlantName, Feeding Info, and Light Schedule editable again
        self.ui.plantNameLineEdit_20.setReadOnly(False)
        self.ui.plantTypeLineEdit_20.setReadOnly(False)

        self.ui.feedScheduleSpinBox_20.setReadOnly(False)
        self.ui.feedDosageDoubleSpinBox_20.setReadOnly(False)

        self.ui.hoursOnSpinBox_20.setReadOnly(False)
        self.ui.hoursOffSpinBox_20.setReadOnly(False)

        # notes section editable
        self.ui.growPodNotesText_20.setReadOnly(False)

        # change the background color of fields to indicate they are editable again
        self.ui.plantNameLineEdit_20.setStyleSheet(self.formFieldColorEditing)
        self.ui.plantTypeLineEdit_20.setStyleSheet(self.formFieldColorEditing)

        self.ui.feedScheduleSpinBox_20.setStyleSheet(self.formFieldColorEditing)
        self.ui.feedDosageDoubleSpinBox_20.setStyleSheet(self.formFieldColorEditing)

        self.ui.hoursOnSpinBox_20.setStyleSheet(self.formFieldColorEditing)
        self.ui.hoursOffSpinBox_20.setStyleSheet(self.formFieldColorEditing)

        self.ui.growPodNotesText_20.setStyleSheet(self.formFieldColorEditing)


    def saveInfoButton_20_Clicked(self):
        print("save info button 20 clicked")

        # create temp growPod object to check if info has been updated
        tempGrowPod = GrowPod()

        # save information on form
        tempGrowPod.plantName = self.ui.plantNameLineEdit_20.text()
        tempGrowPod.plantType = self.ui.plantTypeLineEdit_20.text()
        tempGrowPod.feedSchedule = self.ui.feedScheduleSpinBox_20.value()
        tempGrowPod.feedDosage = self.ui.feedDosageDoubleSpinBox_20.value()
        tempGrowPod.lightHoursOn = self.ui.hoursOnSpinBox_20.value()
        tempGrowPod.lightHoursOff = self.ui.hoursOffSpinBox_20.value()
        tempGrowPod.notes = self.ui.growPodNotesText_20.toPlainText()

        # logic for checking if fields are empty
        if invalidSetupInfo(tempGrowPod):
            print(self.invalidFieldMessage + " 2")
            self.ui.messageAreaText.append(self.invalidFieldMessage + " 2")
        else:
            # code section for updating the UI
            # set PlantName, Feeding Info, and Light Schedule sections to read only
            self.ui.plantNameLineEdit_20.setReadOnly(True)
            self.ui.plantTypeLineEdit_20.setReadOnly(True)

            self.ui.feedScheduleSpinBox_20.setReadOnly(True)
            self.ui.feedDosageDoubleSpinBox_20.setReadOnly(True)

            self.ui.hoursOnSpinBox_20.setReadOnly(True)
            self.ui.hoursOffSpinBox_20.setReadOnly(True)

            # notes section to read only
            self.ui.growPodNotesText_20.setReadOnly(True)

            # change the background color of fields to indicate they are read only
            self.ui.plantNameLineEdit_20.setStyleSheet(self.formFieldColorSaved)
            self.ui.plantTypeLineEdit_20.setStyleSheet(self.formFieldColorSaved)

            self.ui.feedScheduleSpinBox_20.setStyleSheet(self.formFieldColorSaved)
            self.ui.feedDosageDoubleSpinBox_20.setStyleSheet(self.formFieldColorSaved)

            self.ui.hoursOnSpinBox_20.setStyleSheet(self.formFieldColorSaved)
            self.ui.hoursOffSpinBox_20.setStyleSheet(self.formFieldColorSaved)

            self.ui.growPodNotesText_20.setStyleSheet(self.formFieldColorSaved)

            # re-enable edit button
            self.ui.editButton_20.setEnabled(True)

            # re-disable save button
            self.ui.saveInfoButton_20.setEnabled(False)

            # logic to see if the setup values changed. if yes, then send update packet to microcontroller
            if growPodSetupInfoSame(tempGrowPod, self.growPod2):
                # nothing to change
                print("all setup info remained the same")
            else:
                # logic to update grow pod
                print("setup info changed")

                # TODO: section for sending packet to microcontroller
                # sendPacketToGrowPod(growPod, command)

        # save information on form
        self.growPod2.plantName = self.ui.plantNameLineEdit_20.text()
        self.growPod2.plantType = self.ui.plantTypeLineEdit_20.text()
        self.growPod2.feedSchedule = self.ui.feedScheduleSpinBox_20.value()
        self.growPod2.feedDosage = self.ui.feedDosageDoubleSpinBox_20.value()
        self.growPod2.lightHoursOn = self.ui.hoursOnSpinBox_20.value()
        self.growPod2.lightHoursOff = self.ui.hoursOffSpinBox_20.value()
        self.growPod2.notes = self.ui.growPodNotesText_20.toPlainText()

        # rename the group box title with new plant name
        self.ui.growPodContainer_2.setTitle(self.growPod2.plantName + " Status View")

        # save the new information to JSON
        saveGrowPodJSON(self.growPodsList)

        # printing for debugging
        self.growPod2.printSetupInfo()

############## stop here ########################

    def initializeGrowPodButton_30_Clicked(self):
        print("initial grow pod button 3 clicked")

        # save information on form
        self.growPod3.plantName = self.ui.plantNameLineEdit_30.text()
        self.growPod3.plantType = self.ui.plantTypeLineEdit_30.text()
        self.growPod3.feedSchedule = self.ui.feedScheduleSpinBox_30.value()
        self.growPod3.feedDosage = self.ui.feedDosageDoubleSpinBox_30.value()
        self.growPod3.lightHoursOn = self.ui.hoursOnSpinBox_30.value()
        self.growPod3.lightHoursOff = self.ui.hoursOffSpinBox_30.value()
        self.growPod3.notes = self.ui.growPodNotesText_30.toPlainText()

        # logic for checking if fields are empty
        if invalidSetupInfo(self.growPod3):
            print(self.invalidFieldMessage + " 3")
            self.ui.messageAreaText.append(self.invalidFieldMessage + " 3")
        else:
            # logic to confirm that user wants to initialize grow pod
            if confirmInitializeGrowPod(self.growPod3):
                print("user wants to initialize growPod")

                # code section for updating the UI
                # show the grow pod status sections
                self.ui.environmentStatusSection_30.setHidden(False)
                self.ui.powerStatusSection_30.setHidden(False)
                self.ui.pumpStatusSection_30.setHidden(False)

                # show the edit and save info buttons
                self.ui.editButton_30.setHidden(False)
                self.ui.editButton_30.setEnabled(True)
                self.ui.saveInfoButton_30.setHidden(False)
                self.ui.saveInfoButton_30.setEnabled(False)

                # hide the initializeGrowPod and saveInitializeLater buttons
                self.ui.initializeGrowPodButton_30.setHidden(True)
                self.ui.saveInitializeLaterButton_30.setHidden(True)

                # set PlantName, Feeding Info, and Light Schedule sections to read only
                self.ui.plantNameLineEdit_30.setReadOnly(True)
                self.ui.plantTypeLineEdit_30.setReadOnly(True)

                self.ui.feedScheduleSpinBox_30.setReadOnly(True)
                self.ui.feedDosageDoubleSpinBox_30.setReadOnly(True)

                self.ui.hoursOnSpinBox_30.setReadOnly(True)
                self.ui.hoursOffSpinBox_30.setReadOnly(True)

                # notes section to read only
                self.ui.growPodNotesText_30.setReadOnly(True)

                # change the background color of fields to indicate they are read only
                self.ui.plantNameLineEdit_30.setStyleSheet(self.formFieldColorSaved)
                self.ui.plantTypeLineEdit_30.setStyleSheet(self.formFieldColorSaved)

                self.ui.feedScheduleSpinBox_30.setStyleSheet(self.formFieldColorSaved)
                self.ui.feedDosageDoubleSpinBox_30.setStyleSheet(self.formFieldColorSaved)

                self.ui.hoursOnSpinBox_30.setStyleSheet(self.formFieldColorSaved)
                self.ui.hoursOffSpinBox_30.setStyleSheet(self.formFieldColorSaved)

                self.ui.growPodNotesText_30.setStyleSheet(self.formFieldColorSaved)

                # rename the group box title with new plant name
                self.ui.growPodContainer_3.setTitle(self.growPod2.plantName + " Status View")

                # save the new information to JSON
                saveGrowPodJSON(self.growPodsList)

                # print setup info when button pressed
                self.growPod3.printSetupInfo()

                # TODO: here is the section for sending information over to microcontroller
                # sendPacketToGrowPod(growPod, command)

            else:
                print("user does not want to initialize growPod")

    def saveInitializeLaterButton_30_Clicked(self):
        print("save initialize Later button 3 clicked")

        # save information on form
        self.growPod3.plantName = self.ui.plantNameLineEdit_30.text()
        self.growPod3.plantType = self.ui.plantTypeLineEdit_30.text()
        self.growPod3.feedSchedule = self.ui.feedScheduleSpinBox_30.value()
        self.growPod3.feedDosage = self.ui.feedDosageDoubleSpinBox_30.value()
        self.growPod3.lightHoursOn = self.ui.hoursOnSpinBox_30.value()
        self.growPod3.lightHoursOff = self.ui.hoursOffSpinBox_30.value()
        self.growPod3.notes = self.ui.growPodNotesText_30.toPlainText()

        # logic for checking if fields are empty
        if invalidSetupInfo(self.growPod3):
            print(self.invalidFieldMessage + " 3")
            self.ui.messageAreaText.append(self.invalidFieldMessage + " 3")
        else:
            # code section for updating the UI

            # disable saveInitializeLater Button
            self.ui.saveInitializeLaterButton_30.setEnabled(False)

            # set PlantName, Feeding Info, and Light Schedule sections to read only
            self.ui.plantNameLineEdit_30.setReadOnly(True)
            self.ui.plantTypeLineEdit_30.setReadOnly(True)

            self.ui.feedScheduleSpinBox_30.setReadOnly(True)
            self.ui.feedDosageDoubleSpinBox_30.setReadOnly(True)

            self.ui.hoursOnSpinBox_30.setReadOnly(True)
            self.ui.hoursOffSpinBox_30.setReadOnly(True)

            # notes section to read only
            self.ui.growPodNotesText_30.setReadOnly(True)

            # change the background color of fields to indicate they are read only
            self.ui.plantNameLineEdit_30.setStyleSheet(self.formFieldColorSaved)
            self.ui.plantTypeLineEdit_30.setStyleSheet(self.formFieldColorSaved)

            self.ui.feedScheduleSpinBox_30.setStyleSheet(self.formFieldColorSaved)
            self.ui.feedDosageDoubleSpinBox_30.setStyleSheet(self.formFieldColorSaved)

            self.ui.hoursOnSpinBox_30.setStyleSheet(self.formFieldColorSaved)
            self.ui.hoursOffSpinBox_30.setStyleSheet(self.formFieldColorSaved)

            self.ui.growPodNotesText_30.setStyleSheet(self.formFieldColorSaved)

            # rename the group box title with new plant name
            self.ui.growPodContainer_3.setTitle(self.growPod3.plantName + " Status View")

            # show edit info button so that user can edit setup information later
            self.ui.editButton_30.setHidden(False)
            self.ui.editButton_30.setEnabled(True)

            # save the new information to JSON
            saveGrowPodJSON(self.growPodsList)

            # print setup info when button pressed
            self.growPod3.printSetupInfo()

    def editButton_30_Clicked(self):
        print("edit button 30 clicked")

        # disable edit button
        self.ui.editButton_30.setEnabled(False)

        # enable save info button
        self.ui.saveInitializeLaterButton_30.setEnabled(True)
        self.ui.saveInfoButton_30.setEnabled(True)

        # make PlantName, Feeding Info, and Light Schedule editable again
        self.ui.plantNameLineEdit_30.setReadOnly(False)
        self.ui.plantTypeLineEdit_30.setReadOnly(False)

        self.ui.feedScheduleSpinBox_30.setReadOnly(False)
        self.ui.feedDosageDoubleSpinBox_30.setReadOnly(False)

        self.ui.hoursOnSpinBox_30.setReadOnly(False)
        self.ui.hoursOffSpinBox_30.setReadOnly(False)

        # notes section editable
        self.ui.growPodNotesText_30.setReadOnly(False)

        # change the background color of fields to indicate they are editable again
        self.ui.plantNameLineEdit_30.setStyleSheet(self.formFieldColorEditing)
        self.ui.plantTypeLineEdit_30.setStyleSheet(self.formFieldColorEditing)

        self.ui.feedScheduleSpinBox_30.setStyleSheet(self.formFieldColorEditing)
        self.ui.feedDosageDoubleSpinBox_30.setStyleSheet(self.formFieldColorEditing)

        self.ui.hoursOnSpinBox_30.setStyleSheet(self.formFieldColorEditing)
        self.ui.hoursOffSpinBox_30.setStyleSheet(self.formFieldColorEditing)

        self.ui.growPodNotesText_30.setStyleSheet(self.formFieldColorEditing)


    def saveInfoButton_30_Clicked(self):
        print("save info button 30 clicked")

        # create temp growPod object to check if info has been updated
        tempGrowPod = GrowPod()

        # save information on form
        tempGrowPod.plantName = self.ui.plantNameLineEdit_30.text()
        tempGrowPod.plantType = self.ui.plantTypeLineEdit_30.text()
        tempGrowPod.feedSchedule = self.ui.feedScheduleSpinBox_30.value()
        tempGrowPod.feedDosage = self.ui.feedDosageDoubleSpinBox_30.value()
        tempGrowPod.lightHoursOn = self.ui.hoursOnSpinBox_30.value()
        tempGrowPod.lightHoursOff = self.ui.hoursOffSpinBox_30.value()
        tempGrowPod.notes = self.ui.growPodNotesText_30.toPlainText()

        # logic for checking if fields are empty
        if invalidSetupInfo(tempGrowPod):
            print(self.invalidFieldMessage + " 3")
            self.ui.messageAreaText.append(self.invalidFieldMessage + " 3")
        else:
            # code section for updating the UI
            # set PlantName, Feeding Info, and Light Schedule sections to read only
            self.ui.plantNameLineEdit_30.setReadOnly(True)
            self.ui.plantTypeLineEdit_30.setReadOnly(True)

            self.ui.feedScheduleSpinBox_30.setReadOnly(True)
            self.ui.feedDosageDoubleSpinBox_30.setReadOnly(True)

            self.ui.hoursOnSpinBox_30.setReadOnly(True)
            self.ui.hoursOffSpinBox_30.setReadOnly(True)

            # notes section to read only
            self.ui.growPodNotesText_30.setReadOnly(True)

            # change the background color of fields to indicate they are read only
            self.ui.plantNameLineEdit_30.setStyleSheet(self.formFieldColorSaved)
            self.ui.plantTypeLineEdit_30.setStyleSheet(self.formFieldColorSaved)

            self.ui.feedScheduleSpinBox_30.setStyleSheet(self.formFieldColorSaved)
            self.ui.feedDosageDoubleSpinBox_30.setStyleSheet(self.formFieldColorSaved)

            self.ui.hoursOnSpinBox_30.setStyleSheet(self.formFieldColorSaved)
            self.ui.hoursOffSpinBox_30.setStyleSheet(self.formFieldColorSaved)

            self.ui.growPodNotesText_30.setStyleSheet(self.formFieldColorSaved)

            # re-enable edit button
            self.ui.editButton_30.setEnabled(True)

            # re-disable save button
            self.ui.saveInfoButton_30.setEnabled(False)

            # logic to see if the setup values changed. if yes, then send update packet to microcontroller
            if growPodSetupInfoSame(tempGrowPod, self.growPod3):
                # nothing to change
                print("all setup info remained the same")
            else:
                # logic to update grow pod
                print("setup info changed")

                # TODO: section for sending packet to microcontroller
                # sendPacketToGrowPod(growPod, command)

        # save information on form
        self.growPod3.plantName = self.ui.plantNameLineEdit_30.text()
        self.growPod3.plantType = self.ui.plantTypeLineEdit_30.text()
        self.growPod3.feedSchedule = self.ui.feedScheduleSpinBox_30.value()
        self.growPod3.feedDosage = self.ui.feedDosageDoubleSpinBox_30.value()
        self.growPod3.lightHoursOn = self.ui.hoursOnSpinBox_30.value()
        self.growPod3.lightHoursOff = self.ui.hoursOffSpinBox_30.value()
        self.growPod3.notes = self.ui.growPodNotesText_30.toPlainText()

        # rename the group box title with new plant name
        self.ui.growPodContainer_3.setTitle(self.growPod3.plantName + " Status View")

        # save the new information to JSON
        saveGrowPodJSON(self.growPodsList)

        # printing for debugging
        self.growPod3.printSetupInfo()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
