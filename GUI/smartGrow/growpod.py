import json

# list of available IP addresses for the grow pods
ipAddress1 = "192.168.0.101"
# ipAddress2 = "192.168.0.2"
# ipAddress3 = "192.168.0.3"
ipAddress4 = "192.168.0.100"

# ipAddress1 = "10.0.0.1"
ipAddress2 = "10.0.0.2"
ipAddress3 = "10.0.0.3"

# file path for JSON contains grow pod data
filePathJSON = "growPod.json"

# enumerate total grow pods for GUI
totalGrowPods = 3

GROWPOD_NOT_INITIALIZED = "notInitialized"
GROWPOD_SAVED_INIT_LATER = "savedInitLater"
GROWPOD_INITIALIZED = "initialized"

growPodInitStates = [GROWPOD_NOT_INITIALIZED, GROWPOD_SAVED_INIT_LATER, GROWPOD_INITIALIZED]

class GrowPod:
    def __init__(self):
        self.uniqueID = 0
        self.ipAddress = ""
        self.port = 80 # default port for UDP communication
        self.initializedState = growPodInitStates[0]
        self.plantName = ""
        self.plantType = ""
        self.feedSchedule = 0
        self.feedDosage = 0
        self.lightHoursOn = 0
        self.lightHoursOff = 0
        self.luminosity = 0
        self.temperature = 0
        self.humidity = 0
        self.voltage = 0
        self.amps = 0
        self.lightStatus = "OFF"
        self.airPump = "OFF"
        self.sourcePump = "OFF"
        self.drainPump = "OFF"
        self.nutrientsPump = "OFF"
        self.notes = ""
        self.rememberGUIAtStartUp = False

    def printSetupInfo(self):
        print(f"plantName: {self.plantName}")
        print(f"plantType: {self.plantType}")
        print(f"feedSchedule: {self.feedSchedule}")
        print(f"feedDosage: {self.feedDosage}")
        print(f"lightHoursOn: {self.lightHoursOn}")
        print(f"lightHoursOff: {self.lightHoursOff}")
        print(f"notes: {self.notes}")

    def getGrowPodDictionary(self):
        key = f"growPod{self.uniqueID}"
        growPodDictionary = {key:
                                 {'uniqueID': self.uniqueID,
                                  'ipAddress': self.ipAddress,
                                  'port': self.port,
                                  'initializedState': self.initializedState,
                                  'plantName': self.plantName,
                                  'plantType': self.plantType,
                                  'feedSchedule': self.feedSchedule,
                                  'feedDosage': self.feedDosage,
                                  'lightHoursOn': self.lightHoursOn,
                                  'lightHoursOff': self.lightHoursOff,
                                  'luminosity': self.luminosity,
                                  'temperature': self.temperature,
                                  'humidity': self.humidity,
                                  'voltage': self.voltage,
                                  'amps': self.amps,
                                  'lightStatus': self.lightStatus,
                                  'airPump': self.airPump,
                                  'sourcePump': self.sourcePump,
                                  'drainPump': self.drainPump,
                                  'nutrientsPump': self.nutrientsPump,
                                  'notes': self.notes,
                                  'rememberGUIAtStartUp': self.rememberGUIAtStartUp}
                             }

        return growPodDictionary

    def resetGrowPod(self, ID, ipAddress):
        self.uniqueID = ID
        self.ipAddress = ipAddress
        self.port = 80
        self.initializedState = growPodInitStates[0]
        self.plantName = ""
        self.plantType = ""
        self.feedSchedule = 0
        self.feedDosage = 0
        self.lightHoursOn = 0
        self.lightHoursOff = 0
        self.luminosity = 0
        self.temperature = 0
        self.humidity = 0
        self.voltage = 0
        self.amps = 0
        self.lightStatus = "OFF"
        self.airPump = "OFF"
        self.sourcePump = "OFF"
        self.drainPump = "OFF"
        self.nutrientsPump = "OFF"
        self.notes = ""
        self.rememberGUIAtStartUp = False

    def createUpdatePacket(self, command):
        # packet that will be sent to grow pod mcu
        updatePacket = ""

        # construct setup info string
        setupInfo = f" {self.feedSchedule} {self.feedDosage} {self.lightHoursOn} {self.lightHoursOff}"

        if command == "init":
            updatePacket = "init" + setupInfo

            return updatePacket

        elif command == "update":
            updatePacket = "update" + setupInfo

            return updatePacket

        elif command == "reset":
            updatePacket = "reset" + setupInfo

            return updatePacket

        else:
            print("did not recognize command for updating grow pod mcu")

    def updateWithMCUInfo(self, stringfromGrowPod):

        # incoming string will have the following structure
        # luminosity;temperature;humidity;voltage;amps;lightStatus;airPump;sourcePump;drainPump;nutrientsPump

        values = stringfromGrowPod.split(";")

        self.luminosity    = int(values[0])
        self.temperature   = float(values[1])
        self.humidity      = float(values[2])
        self.voltage       = float(values[3])
        self.amps          = float(values[4])
        self.lightStatus   = values[5]
        self.airPump       = values[6]
        self.sourcePump    = values[7]
        self.drainPump     = values[8]
        self.nutrientsPump = values[9]


############## Section for Functions ##############


def invalidSetupInfo(growPod):
    # if any of the setup fields are invalid then return 1
    invalidFormLogic = growPod.plantName == "" or \
                       growPod.plantType == "" or \
                       growPod.feedSchedule == 0 or \
                       growPod.feedDosage == 0 or \
                       growPod.lightHoursOn == 0 or \
                       growPod.lightHoursOff == 0

    return invalidFormLogic


def growPodSetupInfoSame(tempGrowPod, currGrowPod):
    sameFeedSchedule = tempGrowPod.feedSchedule == currGrowPod.feedSchedule
    sameFeedDosage = tempGrowPod.feedDosage == currGrowPod.feedDosage
    sameLightHoursOn = tempGrowPod.lightHoursOn == currGrowPod.lightHoursOn
    sameLightHoursOff = tempGrowPod.lightHoursOff == currGrowPod.lightHoursOff

    # if nothing change this return true
    setupInfoSame = sameFeedSchedule and sameFeedDosage and sameLightHoursOn and sameLightHoursOff

    return setupInfoSame


def saveGrowPodJSON(listOfGrowPods):
    growPodDictionary = {}

    for growPod in listOfGrowPods:
        growPodDictionary.update(growPod.getGrowPodDictionary())

    with open(filePathJSON, 'w') as outJSON:
        json.dump(growPodDictionary, outJSON, ensure_ascii=False, indent=4)



