import sys
from PySide6.QtWidgets import *  # QApplication, QMainWindow, QPushButton, QMessageBox
from PySide6 import QtCore
from ui_growMain import Ui_smartGrowGUI
from growpod import *
from UDPreceiver_1st_version import UDP_RequestInfoFromGrowPod, UDP_TransferUpdateToGrowPod
import datetime

# app logo source
# https://www.iconfinder.com/icons/5190724/farming_gardening_hydroponic_irrigation_organic_watering_icon

# stylesheets from https://qss-stock.devsecstudio.com/
styles = ["Toolery.qss", "Remover.qss", "SyNet.qss", "Irrorater.qss"]

stylesheetFilePath = f"resources/stylesheets/{styles[0]}"

# one minute in milliseconds
minute_ms = 60000

# this variable is for controlling the length for the timer that requests information from the growPods
timerTimeoutInterval = minute_ms*5 # request every 5 minutes


DEVELOPMENT = False
ReleaseFirstBootUp = False  

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
        return False

def confirmResetGrowPod(growPod):
    # code example for MessageBox from QT PySide6 documentation
    msgBox = QMessageBox()
    msgBox.setWindowTitle("GrowPod Reset")
    msgBox.setIcon(QMessageBox.Warning)
    msgBox.setText("Grow Pod Resetting Confirmation")
    msgBox.setInformativeText(f"Are you sure you wish to reset GrowPod {growPod.plantName}?")
    msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
    msgBox.setDefaultButton(QMessageBox.Cancel)
    ret = msgBox.exec()

    if ret == QMessageBox.Yes:
        return True
    else:
        return False


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_smartGrowGUI()
        self.ui.setupUi(self)

        # set parameter for Grow Pod Status View Grid
        self.gridMaxColumns = 2
        self.gridCurrentCol = 1
        self.gridCurrentRow = 1

        # create grow pod objects
        self.growPod1 = GrowPod()
        self.growPod2 = GrowPod()
        self.growPod3 = GrowPod()

        # give unique IDs to each grow pod object
        self.assignUniqueIDsToGrowPods()

        # set grow pod IP Addresses
        self.assignIpAddressesToGrowPods()

        # add grow pods to list
        self.growPodsList = [self.growPod1, self.growPod2, self.growPod3]

        # styling for when form is saved
        self.formFieldColorSaved = "background-color: Gainsboro"

        # styling for when form is being edited
        self.formFieldColorEditing = "background-color: white"

        # message for invalid field
        self.invalidFieldMessage = "Field invalid in Form"

        # hide addGrowPodButton
        self.ui.addGrowPodButton.setHidden(True)

        # connect buttons to actions
        self.connectButtonsToActions()

        # loading UI depending on the initialized states of the grow pods
        if DEVELOPMENT:
            # resetting the JSON file during development
            # growPod objects will be saved in their uninitialized state
            saveGrowPodJSON(self.growPodsList)

            # set the UI for the three grow pods in the notInitializedState
            self.setGrowPod_UI_notInitializedState(1)
            self.setGrowPod_UI_notInitializedState(2)
            self.setGrowPod_UI_notInitializedState(3)

        else:
            # code for loading JSON and initializing the growPods
            print("loading JSON file")
            if ReleaseFirstBootUp:
                saveGrowPodJSON(self.growPodsList)
                self.initGrowPodsWithJSON(self.growPodsList)
                self.loadGrowPodInfoForDisplay(self.growPodsList)

                # set the UI for the three grow pods in the notInitializedState
                self.setGrowPod_UI_notInitializedState(1)
                self.setGrowPod_UI_notInitializedState(2)
                self.setGrowPod_UI_notInitializedState(3)

            else:
                # read JSON file and populate growPod object variables with stored data
                self.initGrowPodsWithJSON(self.growPodsList)

                # display the info in the GUI
                self.loadGrowPodInfoForDisplay(self.growPodsList)

                # determine which UI state to display
                for growPod in self.growPodsList:
                    print(f"growPod{growPod.uniqueID} state = {growPod.initializedState}, IP is {growPod.ipAddress}")
                    growPod.printSetupInfo()
                    if growPod.initializedState == GROWPOD_NOT_INITIALIZED:
                        self.setGrowPod_UI_notInitializedState(growPod.uniqueID)
                        print(f"growPod{growPod.uniqueID}" + GROWPOD_NOT_INITIALIZED)

                    elif growPod.initializedState == GROWPOD_SAVED_INIT_LATER:
                        self.setGrowPod_UI_AfterSavedInitLater(growPod.uniqueID)
                        print(f"growPod{growPod.uniqueID}" + GROWPOD_SAVED_INIT_LATER)

                    elif growPod.initializedState == GROWPOD_INITIALIZED:
                        self.setGrowPod_UI_AfterInitialized(growPod.uniqueID)
                        print(f"growPod{growPod.uniqueID}" + GROWPOD_INITIALIZED)

                        # create grow pod timer
                        self.createGrowPodTimer(growPod.uniqueID, timerTimeoutInterval)

                        # start timer
                        self.startGrowPodTimer(growPod.uniqueID)

                    else:
                        print(f"did not recognize growPod{growPod.uniqueID}'s initialized state")

    def assignUniqueIDsToGrowPods(self):
        self.growPod1.uniqueID = 1
        self.growPod2.uniqueID = 2
        self.growPod3.uniqueID = 3

    def assignIpAddressesToGrowPods(self):
        self.growPod1.ipAddress = ipAddress1
        self.growPod2.ipAddress = ipAddress2
        self.growPod3.ipAddress = ipAddress3

    def connectButtonsToActions(self):
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

        # connect enableResetButton to actions
        self.ui.enableResetButton_1.clicked.connect(self.enableResetButton_1_Clicked)
        self.ui.enableResetButton_20.clicked.connect(self.enableResetButton_20_Clicked)
        self.ui.enableResetButton_30.clicked.connect(self.enableResetButton_30_Clicked)

        # connect resetGrowPodButton to actions
        self.ui.resetGrowPodButton_1.clicked.connect(self.resetGrowPodButton_1_Clicked)
        self.ui.resetGrowPodButton_20.clicked.connect(self.resetGrowPodButton_20_Clicked)
        self.ui.resetGrowPodButton_30.clicked.connect(self.resetGrowPodButton_30_Clicked)

        # connect message reset button to action
        self.ui.messageAreaClearButton.clicked.connect(self.messagesResetButtonClicked)

        # connect refresh button to action
        self.ui.refreshGrowPodInfoButton.clicked.connect(self.refreshInfoButtonClicked)

    def setGrowPod_UI_notInitializedState(self, growPodNumber):

        if growPodNumber == 1:
            # show initialize button and saveInfoInitializeLater button
            self.ui.initializeGrowPodButton_1.setHidden(False)
            self.ui.saveInitializeLaterButton_1.setHidden(False)

            # hide the Edit and Save Info Buttons initially
            self.ui.editButton_1.setHidden(True)
            self.ui.saveInfoButton_1.setHidden(True)

            # hide the reset button initially
            self.ui.enableResetButton_1.setHidden(True)
            self.ui.resetGrowPodButton_1.setHidden(True)
            self.ui.resetGrowPodButton_1.setEnabled(False)

            # hide the grow pod status sections until after user initializes a grow pod
            self.ui.environmentStatusSection_1.setHidden(True)
            self.ui.powerStatusSection_1.setHidden(True)
            self.ui.pumpStatusSection_1.setHidden(True)

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

            # reset the group box title
            self.ui.growPodContainer_1.setTitle("Grow Pod 1 Status View")

        elif growPodNumber == 2:
            # show initialize button and saveInfoInitializeLater button
            self.ui.initializeGrowPodButton_20.setHidden(False)
            self.ui.saveInitializeLaterButton_20.setHidden(False)

            # hide the Edit and Save Info Buttons initially
            self.ui.editButton_20.setHidden(True)
            self.ui.saveInfoButton_20.setHidden(True)

            # hide the reset button initially
            self.ui.enableResetButton_20.setHidden(True)
            self.ui.resetGrowPodButton_20.setHidden(True)
            self.ui.resetGrowPodButton_20.setEnabled(False)

            # hide the grow pod status sections until after user initializes a grow pod
            self.ui.environmentStatusSection_20.setHidden(True)
            self.ui.powerStatusSection_20.setHidden(True)
            self.ui.pumpStatusSection_20.setHidden(True)

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

            # reset the group box title
            self.ui.growPodContainer_2.setTitle("Grow Pod 2 Status View")

        elif growPodNumber == 3:
            # show initialize button and saveInfoInitializeLater button
            self.ui.initializeGrowPodButton_30.setHidden(False)
            self.ui.saveInitializeLaterButton_30.setHidden(False)

            # hide the Edit and Save Info Buttons initially
            self.ui.editButton_30.setHidden(True)
            self.ui.saveInfoButton_30.setHidden(True)

            # hide the reset button initially
            self.ui.enableResetButton_30.setHidden(True)
            self.ui.resetGrowPodButton_30.setHidden(True)
            self.ui.resetGrowPodButton_30.setEnabled(False)

            # hide the grow pod status sections until after user initializes a grow pod
            self.ui.environmentStatusSection_30.setHidden(True)
            self.ui.powerStatusSection_30.setHidden(True)
            self.ui.pumpStatusSection_30.setHidden(True)

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

            # reset the group box title
            self.ui.growPodContainer_3.setTitle("Grow Pod 3 Status View")

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
            self.ui.messageAreaText.append(self.getTimeStamp() + self.invalidFieldMessage + " 1")
        else:
            # logic to confirm that user wants to initialize grow pod
            if confirmInitializeGrowPod(self.growPod1):
                print("user wants to initialize growPod")

                # set initialized variable in grow pod object to "initialized"
                self.growPod1.initializedState = GROWPOD_INITIALIZED
                self.setGrowPod_UI_AfterInitialized(1)

                # save the new information to JSON
                saveGrowPodJSON(self.growPodsList)

                # sending information over to microcontroller
                self.sendPacketToGrowPod(self.growPod1, "init")

                # create grow pod timer
                self.createGrowPodTimer(1, timerTimeoutInterval)

                # start timer
                self.startGrowPodTimer(1)

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
            self.ui.messageAreaText.append(self.getTimeStamp() + self.invalidFieldMessage + " 1")
        else:
            # set initialized status
            self.growPod1.initializedState = GROWPOD_SAVED_INIT_LATER

            # code section for updating the UI
            self.setGrowPod_UI_AfterSavedInitLater(1)

            # save the new information to JSON
            saveGrowPodJSON(self.growPodsList)

    def editButton_1_Clicked(self):
        print("edit button 1 clicked")

        self.setGrowPod_UI_EditClicked(1)

        # stop timer for getting updates
        if self.growPod1.initializedState == GROWPOD_INITIALIZED:
            self.stopGrowPodTimer(1)


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
            self.ui.messageAreaText.append(self.getTimeStamp() + self.invalidFieldMessage + " 1")
        else:
            # code section for updating the UI
            self.setGrowPod_UI_SavedInfoClicked(1)

            # save the new information to JSON
            saveGrowPodJSON(self.growPodsList)

            # logic to see if the setup values changed. if yes, then send update packet to microcontroller
            if growPodSetupInfoSame(tempGrowPod, self.growPod1):
                # nothing to change
                print("all setup info remained the same")
            else:
                # logic to update grow pod
                print("setup info changed")

                # sending packet to microcontroller
                self.sendPacketToGrowPod(self.growPod1, "update")

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

        # restart timer for getting updating info from mcu
        self.createGrowPodTimer(1, timerTimeoutInterval)
        self.startGrowPodTimer(1)

        # printing for debugging
        # self.growPod1.printSetupInfo()

    def enableResetButton_1_Clicked(self):
        print("enable reset button 1 clicked")

        self.ui.resetGrowPodButton_1.setHidden(False)
        self.ui.resetGrowPodButton_1.setEnabled(True)

    def resetGrowPodButton_1_Clicked(self):
        print("reset grow pod button 1 clicked")

        if confirmResetGrowPod(self.growPod1):
            print("user wants to reset grow pod")

            # set message in Messages
            self.ui.messageAreaText.append(self.getTimeStamp() + f"Reset of Grow Pod {self.growPod1.plantName} Confirmed")

            self.growPod1.resetGrowPod(1, ipAddress1)

            # send reset command to grow pod
            self.sendPacketToGrowPod(self.growPod1, "reset")

            # save the current status of all grow pods
            saveGrowPodJSON(self.growPodsList)

            # load form fields with reset values
            self.loadGrowPodInfoForDisplay([self.growPod1])

            # set UI to not initialized state
            self.setGrowPod_UI_notInitializedState(1)

            # kill grow pod timer
            self.stopGrowPodTimer(1)

        else:
            print("user does not want to reset grow pod")

            # hide and disable reset button
            self.ui.resetGrowPodButton_1.setHidden(True)
            self.ui.resetGrowPodButton_1.setEnabled(False)

            # set message in Messages
            self.ui.messageAreaText.append(self.getTimeStamp() + f"Reset of Grow Pod {self.growPod1.plantName} Cancelled")



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
            self.ui.messageAreaText.append(self.getTimeStamp() + self.invalidFieldMessage + " 2")
        else:
            # logic to confirm that user wants to initialize grow pod
            if confirmInitializeGrowPod(self.growPod2):
                print("user wants to initialize growPod")

                # set initialized variable in grow pod object to "initialized"
                self.growPod2.initializedState = GROWPOD_INITIALIZED

                # set UI
                self.setGrowPod_UI_AfterInitialized(2)

                # save the new information to JSON
                saveGrowPodJSON(self.growPodsList)

                # sending information over to microcontroller
                self.sendPacketToGrowPod(self.growPod2, "init")

                # create grow pod timer
                self.createGrowPodTimer(2, timerTimeoutInterval)

                # start timer
                self.startGrowPodTimer(2)

            else:
                print("user does not want to initialize growPod")

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
            self.ui.messageAreaText.append(self.getTimeStamp() + self.invalidFieldMessage + " 2")
        else:
            # set initialized Status
            self.growPod2.initializedState = GROWPOD_SAVED_INIT_LATER

            # code section for updating the UI
            self.setGrowPod_UI_AfterSavedInitLater(2)

            # save the new information to JSON
            saveGrowPodJSON(self.growPodsList)


    def editButton_20_Clicked(self):
        print("edit button 20 clicked")

        self.setGrowPod_UI_EditClicked(2)

        # stop timer for getting updates
        if self.growPod2.initializedState == GROWPOD_INITIALIZED:
            self.stopGrowPodTimer(2)


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
            self.ui.messageAreaText.append(self.getTimeStamp() + self.invalidFieldMessage + " 2")
        else:
            # code section for updating the UI
            self.setGrowPod_UI_SavedInfoClicked(2)

            # save the new information to JSON
            saveGrowPodJSON(self.growPodsList)

            # logic to see if the setup values changed. if yes, then send update packet to microcontroller
            if growPodSetupInfoSame(tempGrowPod, self.growPod2):
                # nothing to change
                print("all setup info remained the same")
            else:
                # logic to update grow pod
                print("setup info changed")

                # sending packet to microcontroller
                self.sendPacketToGrowPod(self.growPod2, "update")

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

        # restart timer for getting updating info from mcu
        self.createGrowPodTimer(2, timerTimeoutInterval)
        self.startGrowPodTimer(2)

        # printing for debugging
        # self.growPod2.printSetupInfo()

    def enableResetButton_20_Clicked(self):
        print("enable reset button 20 clicked")

        self.ui.resetGrowPodButton_20.setHidden(False)
        self.ui.resetGrowPodButton_20.setEnabled(True)

    def resetGrowPodButton_20_Clicked(self):
        print("reset grow pod button 20 clicked")

        if confirmResetGrowPod(self.growPod2):
            print("user wants to reset grow pod")

            # set message in Messages
            self.ui.messageAreaText.append(self.getTimeStamp() + f"Reset of Grow Pod {self.growPod2.plantName} Confirmed")

            self.growPod2.resetGrowPod(2, ipAddress2)

            # send reset command to grow pod
            self.sendPacketToGrowPod(self.growPod2, "reset")

            # save the current status of all grow pods
            saveGrowPodJSON(self.growPodsList)

            # load form fields with reset values
            self.loadGrowPodInfoForDisplay([self.growPod2])

            # set UI to not initialized state
            self.setGrowPod_UI_notInitializedState(2)

            # stop grow pod timer
            self.stopGrowPodTimer(2)

        else:
            print("user does not want to reset grow pod")

            # hide and disable reset button
            self.ui.resetGrowPodButton_20.setHidden(True)
            self.ui.resetGrowPodButton_20.setEnabled(False)

            # set message in Messages
            self.ui.messageAreaText.append(self.getTimeStamp() + f"Reset of Grow Pod {self.growPod2.plantName} Cancelled")

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
            self.ui.messageAreaText.append(self.getTimeStamp() + self.invalidFieldMessage + " 3")
        else:
            # logic to confirm that user wants to initialize grow pod
            if confirmInitializeGrowPod(self.growPod3):
                print("user wants to initialize growPod")

                # set initialized variable in grow pod object to "initialized"
                self.growPod3.initializedState = GROWPOD_INITIALIZED

                # set UI
                self.setGrowPod_UI_AfterInitialized(3)

                # save the new information to JSON
                saveGrowPodJSON(self.growPodsList)

                # sending information over to microcontroller
                self.sendPacketToGrowPod(self.growPod3, "init")

                # create grow pod timer
                self.createGrowPodTimer(3, timerTimeoutInterval)

                # start timer
                self.startGrowPodTimer(3)

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
            self.ui.messageAreaText.append(self.getTimeStamp() + self.invalidFieldMessage + " 3")
        else:
            # set initialized status
            self.growPod3.initializedState = GROWPOD_SAVED_INIT_LATER

            # code section for updating the UI
            self.setGrowPod_UI_AfterSavedInitLater(3)

            # save the new information to JSON
            saveGrowPodJSON(self.growPodsList)

    def editButton_30_Clicked(self):
        print("edit button 30 clicked")

        self.setGrowPod_UI_EditClicked(3)

        # stop timer for getting updates
        if self.growPod3.initializedState == GROWPOD_INITIALIZED:
            self.stopGrowPodTimer(3)


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
            self.ui.messageAreaText.append(self.getTimeStamp() + self.invalidFieldMessage + " 3")
        else:
            # code section for updating the UI
            self.setGrowPod_UI_SavedInfoClicked(3)

            # save the new information to JSON
            saveGrowPodJSON(self.growPodsList)

            # logic to see if the setup values changed. if yes, then send update packet to microcontroller
            if growPodSetupInfoSame(tempGrowPod, self.growPod3):
                # nothing to change
                print("all setup info remained the same")
            else:
                # logic to update grow pod
                print("setup info changed")

                # sending packet to microcontroller
                self.sendPacketToGrowPod(self.growPod3, "update")

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

        # restart timer for getting updating info from mcu
        self.createGrowPodTimer(3, timerTimeoutInterval)
        self.startGrowPodTimer(3)

        # printing for debugging
        # self.growPod3.printSetupInfo()

    def enableResetButton_30_Clicked(self):
        print("enable reset button 30 clicked")

        self.ui.resetGrowPodButton_30.setHidden(False)
        self.ui.resetGrowPodButton_30.setEnabled(True)

    def resetGrowPodButton_30_Clicked(self):
        print("reset grow pod button 30 clicked")

        if confirmResetGrowPod(self.growPod3):
            print("user wants to reset grow pod")

            # set message in Messages
            self.ui.messageAreaText.append(self.getTimeStamp() + f"Reset of Grow Pod {self.growPod3.plantName} Confirmed")

            # reset grow pod object
            self.growPod3.resetGrowPod(3, ipAddress3)

            # send reset command to grow pod
            self.sendPacketToGrowPod(self.growPod3, "reset")

            # save the current status of all grow pods
            saveGrowPodJSON(self.growPodsList)

            # load form fields with reset values
            self.loadGrowPodInfoForDisplay([self.growPod3])

            # set UI to not initialized state
            self.setGrowPod_UI_notInitializedState(3)

            # stop grow pod timer
            self.stopGrowPodTimer(3)

        else:
            print("user does not want to reset grow pod")

            # hide and disable reset button
            self.ui.resetGrowPodButton_30.setHidden(True)
            self.ui.resetGrowPodButton_30.setEnabled(False)

            # set message in Messages
            self.ui.messageAreaText.append(self.getTimeStamp() + f"Reset of Grow Pod {self.growPod3.plantName} Cancelled")

    def messagesResetButtonClicked(self):
        print("Messages Rest button clicked")
        self.ui.messageAreaText.clear()

    def loadGrowPodInfoForDisplay(self, listOfGrowPods):

        for growPod in listOfGrowPods:
            if growPod.uniqueID == 1:
                # set form fields for growPod1
                self.ui.plantNameLineEdit_1.setText(self.growPod1.plantName)
                self.ui.plantTypeLineEdit_1.setText(self.growPod1.plantType)
                self.ui.feedScheduleSpinBox_1.setValue(self.growPod1.feedSchedule)
                self.ui.feedDosageDoubleSpinBox_1.setValue(self.growPod1.feedDosage)
                self.ui.hoursOnSpinBox_1.setValue(self.growPod1.lightHoursOn)
                self.ui.hoursOffSpinBox_1.setValue(self.growPod1.lightHoursOff)
                self.ui.luminositySpinBox_1.setValue(self.growPod1.luminosity)
                self.ui.temperatureDoubleSpinBox_1.setValue(self.growPod1.temperature)
                self.ui.humidityDoubleSpinBox_1.setValue(self.growPod1.humidity)
                self.ui.voltageDoubleSpinBox_1.setValue(self.growPod1.voltage)
                self.ui.ampsDoubleSpinBox_1.setValue(self.growPod1.amps)
                self.ui.lightStatusLineEdit_1.setText(self.growPod1.lightStatus)
                self.ui.airPumpLineEdit_1.setText(self.growPod1.airPump)
                self.ui.sourcePumpLineEdit_1.setText(self.growPod1.sourcePump)
                self.ui.drainPumpLineEdit_1.setText(self.growPod1.drainPump)
                self.ui.nutrientsPumpLineEdit_1.setText(self.growPod1.nutrientsPump)
                self.ui.growPodNotesText_1.setPlainText(self.growPod1.notes)

            elif growPod.uniqueID == 2:
                # set form fields for growPod2
                self.ui.plantNameLineEdit_20.setText(self.growPod2.plantName)
                self.ui.plantTypeLineEdit_20.setText(self.growPod2.plantType)
                self.ui.feedScheduleSpinBox_20.setValue(self.growPod2.feedSchedule)
                self.ui.feedDosageDoubleSpinBox_20.setValue(self.growPod2.feedDosage)
                self.ui.hoursOnSpinBox_20.setValue(self.growPod2.lightHoursOn)
                self.ui.hoursOffSpinBox_20.setValue(self.growPod2.lightHoursOff)
                self.ui.luminositySpinBox_20.setValue(self.growPod2.luminosity)
                self.ui.temperatureDoubleSpinBox_20.setValue(self.growPod2.temperature)
                self.ui.humidityDoubleSpinBox_20.setValue(self.growPod2.humidity)
                self.ui.voltageDoubleSpinBox_20.setValue(self.growPod2.voltage)
                self.ui.ampsDoubleSpinBox_20.setValue(self.growPod2.amps)
                self.ui.lightStatusLineEdit_20.setText(self.growPod2.lightStatus)
                self.ui.airPumpLineEdit_20.setText(self.growPod2.airPump)
                self.ui.sourcePumpLineEdit_20.setText(self.growPod2.sourcePump)
                self.ui.drainPumpLineEdit_20.setText(self.growPod2.drainPump)
                self.ui.nutrientsPumpLineEdit_20.setText(self.growPod2.nutrientsPump)
                self.ui.growPodNotesText_20.setPlainText(self.growPod2.notes)

            elif growPod.uniqueID == 3:
                # set form fields for growPod3
                self.ui.plantNameLineEdit_30.setText(self.growPod3.plantName)
                self.ui.plantTypeLineEdit_30.setText(self.growPod3.plantType)
                self.ui.feedScheduleSpinBox_30.setValue(self.growPod3.feedSchedule)
                self.ui.feedDosageDoubleSpinBox_30.setValue(self.growPod3.feedDosage)
                self.ui.hoursOnSpinBox_30.setValue(self.growPod3.lightHoursOn)
                self.ui.hoursOffSpinBox_30.setValue(self.growPod3.lightHoursOff)
                self.ui.luminositySpinBox_30.setValue(self.growPod3.luminosity)
                self.ui.temperatureDoubleSpinBox_30.setValue(self.growPod3.temperature)
                self.ui.humidityDoubleSpinBox_30.setValue(self.growPod3.humidity)
                self.ui.voltageDoubleSpinBox_30.setValue(self.growPod3.voltage)
                self.ui.ampsDoubleSpinBox_30.setValue(self.growPod3.amps)
                self.ui.lightStatusLineEdit_30.setText(self.growPod3.lightStatus)
                self.ui.airPumpLineEdit_30.setText(self.growPod3.airPump)
                self.ui.sourcePumpLineEdit_30.setText(self.growPod3.sourcePump)
                self.ui.drainPumpLineEdit_30.setText(self.growPod3.drainPump)
                self.ui.nutrientsPumpLineEdit_30.setText(self.growPod3.nutrientsPump)
                self.ui.growPodNotesText_30.setPlainText(self.growPod3.notes)

            else:
                print("growPod is unknown")

    def initGrowPodsWithJSON(self, listOfGrowPods):
        growPodDictionary = {}

        with open(filePathJSON, 'r') as inputJSON:
            growPodDictionary = json.load(inputJSON)

        growPodIndex = [1, 2, 3]

        for number in growPodIndex:
            key = f"growPod{number}"
            listOfGrowPods[number - 1].initializedState = growPodDictionary[key]['initializedState']
            listOfGrowPods[number - 1].plantName = growPodDictionary[key]['plantName']
            listOfGrowPods[number - 1].plantType = growPodDictionary[key]['plantType']
            listOfGrowPods[number - 1].feedSchedule = growPodDictionary[key]['feedSchedule']
            listOfGrowPods[number - 1].feedDosage = growPodDictionary[key]['feedDosage']
            listOfGrowPods[number - 1].lightHoursOn = growPodDictionary[key]['lightHoursOn']
            listOfGrowPods[number - 1].lightHoursOff = growPodDictionary[key]['lightHoursOff']
            listOfGrowPods[number - 1].luminosity = growPodDictionary[key]['luminosity']
            listOfGrowPods[number - 1].temperature = growPodDictionary[key]['temperature']
            listOfGrowPods[number - 1].humidity = growPodDictionary[key]['humidity']
            listOfGrowPods[number - 1].voltage = growPodDictionary[key]['voltage']
            listOfGrowPods[number - 1].amps = growPodDictionary[key]['amps']
            listOfGrowPods[number - 1].lightStatus = growPodDictionary[key]['lightStatus']
            listOfGrowPods[number - 1].airPump = growPodDictionary[key]['airPump']
            listOfGrowPods[number - 1].sourcePump = growPodDictionary[key]['sourcePump']
            listOfGrowPods[number - 1].drainPump = growPodDictionary[key]['drainPump']
            listOfGrowPods[number - 1].nutrientsPump = growPodDictionary[key]['nutrientsPump']
            listOfGrowPods[number - 1].notes = growPodDictionary[key]['notes']
            listOfGrowPods[number - 1].rememberGUIAtStartUp = growPodDictionary[key]['rememberGUIAtStartUp']


    def setGrowPod_UI_AfterInitialized(self, growPodNumber):
        # code section for updating the UI
        # the initialize and saveInitializeLater buttons are hidden
        # the edit, save, and enable reset buttons are displayed
        # the save button is set to not enabled

        if growPodNumber == 1:
            # show the grow pod status sections
            self.ui.environmentStatusSection_1.setHidden(False)
            self.ui.powerStatusSection_1.setHidden(False)
            self.ui.pumpStatusSection_1.setHidden(False)

            # show the edit and save info buttons
            self.ui.editButton_1.setHidden(False)
            self.ui.editButton_1.setEnabled(True)
            self.ui.saveInfoButton_1.setHidden(False)
            self.ui.saveInfoButton_1.setEnabled(False)

            # show enable reset button
            self.ui.enableResetButton_1.setHidden(False)

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

            # buttons to hide in initialized state
            self.hideButtonsInitializedState(1)

            # print setup info when button pressed
            # self.growPod1.printSetupInfo()

        elif growPodNumber == 2:
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

            # show enable reset button
            self.ui.enableResetButton_20.setHidden(False)

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
            self.ui.plantTypeLineEdit_20.setStyleSheet(self.formFieldColorSaved)

            self.ui.feedScheduleSpinBox_20.setStyleSheet(self.formFieldColorSaved)
            self.ui.feedDosageDoubleSpinBox_20.setStyleSheet(self.formFieldColorSaved)

            self.ui.hoursOnSpinBox_20.setStyleSheet(self.formFieldColorSaved)
            self.ui.hoursOffSpinBox_20.setStyleSheet(self.formFieldColorSaved)

            self.ui.growPodNotesText_20.setStyleSheet(self.formFieldColorSaved)

            # rename the group box title with new plant name
            self.ui.growPodContainer_2.setTitle(self.growPod2.plantName + " Status View")

            # buttons to hide in initialized state
            self.hideButtonsInitializedState(2)

            # print setup info when button pressed
            # self.growPod2.printSetupInfo()

        elif growPodNumber == 3:
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

            # show enable reset button
            self.ui.enableResetButton_30.setHidden(False)

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
            self.ui.growPodContainer_3.setTitle(self.growPod3.plantName + " Status View")

            # buttons to hide in initialized state
            self.hideButtonsInitializedState(3)

            # print setup info when button pressed
            # self.growPod3.printSetupInfo()

    def setGrowPod_UI_AfterSavedInitLater(self, growPodNumber):

        if growPodNumber == 1:
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

            # print setup info when button pressed
            # self.growPod1.printSetupInfo()

            # buttons to hide in savedInitializeLater state
            self.hideButtonsInSavedInitLaterState(1)

        elif growPodNumber == 2:
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

            # buttons to hide in savedInitializeLater state
            self.hideButtonsInSavedInitLaterState(2)

            # print setup info when button pressed
            # self.growPod2.printSetupInfo()

        elif growPodNumber == 3:
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

            # buttons to hide in savedInitializeLater state
            self.hideButtonsInSavedInitLaterState(3)

            # print setup info when button pressed
            # self.growPod3.printSetupInfo()

    def setGrowPod_UI_EditClicked(self, growPodNumber):

        if growPodNumber == 1:
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

        elif growPodNumber == 2:
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

        elif growPodNumber == 3:
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

    def setGrowPod_UI_SavedInfoClicked(self, growPodNumber):

        if growPodNumber == 1:
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

        elif growPodNumber == 2:
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

        elif growPodNumber == 3:
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

    def hideButtonsInSavedInitLaterState(self, growPodNumber):
        # buttons to hide in savedInitializeLater state
        if growPodNumber == 1:

            self.ui.saveInfoButton_1.setHidden(True)
            self.ui.enableResetButton_1.setHidden(True)
            self.ui.resetGrowPodButton_1.setHidden(True)

        elif growPodNumber == 2:
            self.ui.saveInfoButton_20.setHidden(True)
            self.ui.enableResetButton_20.setHidden(True)
            self.ui.resetGrowPodButton_20.setHidden(True)

        elif growPodNumber == 3:
            self.ui.saveInfoButton_30.setHidden(True)
            self.ui.enableResetButton_30.setHidden(True)
            self.ui.resetGrowPodButton_30.setHidden(True)

    def hideButtonsInitializedState(self, growPodNumber):
        # buttons to hide in initialized state
        if growPodNumber == 1:
            self.ui.initializeGrowPodButton_1.setHidden(True)
            self.ui.saveInitializeLaterButton_1.setHidden(True)
            self.ui.resetGrowPodButton_1.setHidden(True)

        elif growPodNumber == 2:
            self.ui.initializeGrowPodButton_20.setHidden(True)
            self.ui.saveInitializeLaterButton_20.setHidden(True)
            self.ui.resetGrowPodButton_20.setHidden(True)

        elif growPodNumber == 3:
            self.ui.initializeGrowPodButton_30.setHidden(True)
            self.ui.saveInitializeLaterButton_30.setHidden(True)
            self.ui.resetGrowPodButton_30.setHidden(True)

    def createGrowPodTimer(self, growPodNumber, timeOutInterval):

        if growPodNumber == 1:
            # create timer for requesting data from grow pod
            self.growPodTimer1 = QtCore.QTimer()

            # connect timer to timeout functions
            self.growPodTimer1.timeout.connect(self.requestInfoFromGrowPod1)

            # set timeout interval
            self.growPodTimer1.setInterval(timeOutInterval)

        elif growPodNumber == 2:
            # create timer for requesting data from grow pod
            self.growPodTimer2 = QtCore.QTimer()

            # connect timer to timeout functions
            self.growPodTimer2.timeout.connect(self.requestInfoFromGrowPod2)

            # set timeout interval
            self.growPodTimer2.setInterval(timeOutInterval)

        elif growPodNumber == 3:
            # create timer for requesting data from grow pod
            self.growPodTimer3 = QtCore.QTimer()

            # connect timer to timeout functions
            self.growPodTimer3.timeout.connect(self.requestInfoFromGrowPod3)

            # set timeout interval
            self.growPodTimer3.setInterval(timeOutInterval)

        else:
            print("did not recognize grow pod number for setting up timer")

    def startGrowPodTimer(self, growPodNumber):

        if growPodNumber == 1:
            self.growPodTimer1.start()

        elif growPodNumber == 2:
            self.growPodTimer2.start()

        elif growPodNumber == 3:
            self.growPodTimer3.start()

        else:
            print("did not recognize grow pod number for starting timer")

    def stopGrowPodTimer(self, growPodNumber):

        if growPodNumber == 1:
            self.growPodTimer1.stop()

        elif growPodNumber == 2:
            self.growPodTimer2.stop()

        elif growPodNumber == 3:
            self.growPodTimer3.stop()

        else:
            print("did not recognize grow pod number for killing timer")

    def requestInfoFromGrowPod1(self):
        growPodNumber = 1
        message = f"Requesting UDP info from GrowPod{growPodNumber}"
        print(message)

        # update messages indicating that UPD packet requested
        self.ui.messageAreaText.append(self.getTimeStamp() + message)

        # get info from the grow pod MCU
        # format of the packet the growPod will send to GUI
        # luminosity;temperature;humidity;voltage;amps;lightStatus;airPump;sourcePump;drainPump;nutrientsPump
        mcuInfo = UDP_RequestInfoFromGrowPod(self.growPod1.ipAddress) # test data "100;100.5;100.5;200.3;400.6;ON;ON;ON;ON;ON"

        print(f"packet received for GrowPod{growPodNumber}: " + mcuInfo)

        if (mcuInfo == "fail"):
            # update messages with failed UPD packet
            self.ui.messageAreaText.append(
                self.getTimeStamp() + f"UDP packet from GrowPod{growPodNumber} failed")

        else:
            # update grow pod object with info from the grow pod MCU
            self.growPod1.updateWithMCUInfo(mcuInfo)

            # also post to messages that UDP packet was successful
            self.ui.messageAreaText.append(
                self.getTimeStamp() + f"UDP packet from GrowPod{growPodNumber} successful")

            # save the new info the JSON
            saveGrowPodJSON(self.growPodsList)

            # load that info on the GUI
            self.loadGrowPodInfoForDisplay([self.growPod1])

    def requestInfoFromGrowPod2(self):
        growPodNumber = 2
        message = f"requesting info from GrowPod{growPodNumber}"
        print(message)

        # update messages indicating that UPD packet requested
        self.ui.messageAreaText.append(self.getTimeStamp() + message)

        # get info from the grow pod MCU
        # format of the packet the growPod will send to GUI
        # luminosity;temperature;humidity;voltage;amps;lightStatus;airPump;sourcePump;drainPump;nutrientsPump
        mcuInfo = UDP_RequestInfoFromGrowPod(self.growPod2.ipAddress)  # test data "2000;100.5;100.5;200.3;400.6;ON;ON;ON;ON;ON"

        print(f"packet received for GrowPod{growPodNumber}: " + mcuInfo)

        if (mcuInfo == "fail"):
            # update messages with failed UPD packet
            self.ui.messageAreaText.append(
                self.getTimeStamp() + f"UDP packet from GrowPod{growPodNumber} failed")

        else:
            # update grow pod object with info from the grow pod MCU
            self.growPod2.updateWithMCUInfo(mcuInfo)

            # also post to messages that UDP packet was successful
            self.ui.messageAreaText.append(
                self.getTimeStamp() + f"UDP packet from GrowPod{growPodNumber} successful")

            # save the new info the JSON
            saveGrowPodJSON(self.growPodsList)

            # load that info on the GUI
            self.loadGrowPodInfoForDisplay([self.growPod2])

    def requestInfoFromGrowPod3(self):
        growPodNumber = 3
        message = f"requesting info from GrowPod{growPodNumber}"
        print(message)

        # update messages indicating that UPD packet requested
        self.ui.messageAreaText.append(self.getTimeStamp() + message)

        # get info from the grow pod MCU
        # format of the packet the growPod will send to GUI
        # luminosity;temperature;humidity;voltage;amps;lightStatus;airPump;sourcePump;drainPump;nutrientsPump
        mcuInfo = UDP_RequestInfoFromGrowPod(self.growPod3.ipAddress)  # test data "3000;100.5;100.5;200.3;400.6;ON;ON;ON;ON;ON"

        print(f"packet received for GrowPod{growPodNumber}: " + mcuInfo)

        if (mcuInfo == "fail"):
            # update messages with failed UPD packet
            self.ui.messageAreaText.append(
                self.getTimeStamp() + f"UDP packet from GrowPod{growPodNumber} failed")

        else:
            # update grow pod object with info from the grow pod MCU
            self.growPod3.updateWithMCUInfo(mcuInfo)

            # also post to messages that UDP packet was successful
            self.ui.messageAreaText.append(
                self.getTimeStamp() + f"UDP packet from GrowPod{growPodNumber} successful")

            # save the new info the JSON
            saveGrowPodJSON(self.growPodsList)

            # load that info on the GUI
            self.loadGrowPodInfoForDisplay([self.growPod3])

    def refreshInfoButtonClicked(self):

        if self.growPod1.initializedState == GROWPOD_INITIALIZED and self.growPodTimer1.isActive():
            # stop timer
            self.stopGrowPodTimer(1)

            # refresh grow pod UI
            self.requestInfoFromGrowPod1()

            # restart timer
            self.createGrowPodTimer(1, timerTimeoutInterval)
            self.startGrowPodTimer(1)

        else:
            print("GrowPod1 cannot be refreshed at this moment")
            self.ui.messageAreaText.append(self.getTimeStamp() + "GrowPod1 cannot be refreshed at this moment")

            if self.growPod1.initializedState == GROWPOD_INITIALIZED:
                # stop timer
                self.stopGrowPodTimer(1)

                # restart timer
                self.createGrowPodTimer(1, timerTimeoutInterval)
                self.startGrowPodTimer(1)

        if self.growPod2.initializedState == GROWPOD_INITIALIZED and self.growPodTimer2.isActive():
            # stop timer
            self.stopGrowPodTimer(2)

            # refresh grow pod UI
            self.requestInfoFromGrowPod2()

            # restart timer
            self.createGrowPodTimer(2, timerTimeoutInterval)
            self.startGrowPodTimer(2)

        else:
            print("GrowPod2 cannot be refreshed at this moment")
            self.ui.messageAreaText.append(self.getTimeStamp() + "GrowPod2 cannot be refreshed at this moment")

            if self.growPod2.initializedState == GROWPOD_INITIALIZED:
                # stop timer
                self.stopGrowPodTimer(2)

                # restart timer
                self.createGrowPodTimer(2, timerTimeoutInterval)
                self.startGrowPodTimer(2)

        if self.growPod3.initializedState == GROWPOD_INITIALIZED and self.growPodTimer3.isActive():
            # stop timer
            self.stopGrowPodTimer(3)

            # refresh grow pod UI
            self.requestInfoFromGrowPod3()

            # restart timer
            self.createGrowPodTimer(3, timerTimeoutInterval)
            self.startGrowPodTimer(3)

        else:
            print("GrowPod3 cannot be refreshed at this moment")
            self.ui.messageAreaText.append(self.getTimeStamp() + "GrowPod3 cannot be refreshed at this moment")

            if self.growPod3.initializedState == GROWPOD_INITIALIZED:
                # stop timer
                self.stopGrowPodTimer(3)

                # restart timer
                self.createGrowPodTimer(3, timerTimeoutInterval)
                self.startGrowPodTimer(3)

    def sendPacketToGrowPod(self, growPod, command):

        if growPod.uniqueID == 1:
            print(f"Sending update packet to GrowPod{growPod.uniqueID} with command: {command}")
            self.ui.messageAreaText.append(self.getTimeStamp() + f"Sending update packet to GrowPod{growPod.uniqueID} with command: {command}")

            # UPD data transfer here
            updatePacket = self.growPod1.createUpdatePacket(command)
            UDP_TransferUpdateToGrowPod(self.growPod1.ipAddress, updatePacket)

        elif growPod.uniqueID == 2:
            print(f"Sending update packet to GrowPod{growPod.uniqueID} with command: {command}")
            self.ui.messageAreaText.append(self.getTimeStamp() +
                f"Sending update packet to GrowPod{growPod.uniqueID} with command: {command}")

            # UPD data transfer here
            updatePacket = self.growPod2.createUpdatePacket(command)
            UDP_TransferUpdateToGrowPod(self.growPod2.ipAddress, updatePacket)

        elif growPod.uniqueID == 3:
            print(f"Sending update packet to GrowPod{growPod.uniqueID} with command: {command}")
            self.ui.messageAreaText.append(self.getTimeStamp() +
                f"Sending update packet to GrowPod{growPod.uniqueID} with command: {command}")

            # UPD data transfer here
            updatePacket = self.growPod3.createUpdatePacket(command)
            UDP_TransferUpdateToGrowPod(self.growPod3.ipAddress, updatePacket)

    def getTimeStamp(self):

        return f"{datetime.datetime.now():%Y-%b-%d %H:%M:%S}    "


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    # open qss file
    File = QtCore.QFile(stylesheetFilePath)
    if not File.open( QtCore.QFile.ReadOnly | QtCore.QFile.Text):
        print("could not load stylesheet")

    qss = QtCore.QTextStream(File)

    # setup stylesheet
    app.setStyleSheet(qss.readAll())

    window.show()
    sys.exit(app.exec())
