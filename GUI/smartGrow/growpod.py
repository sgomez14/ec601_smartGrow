import json

# list of available IP addresses for the grow pods
ipAddress1 = "192.168.0.1"
ipAddress2 = "192.168.0.2"
ipAddress3 = "192.168.0.3"

# if any of the setup fields are invalid then return 1
def invalidSetupInfo(growPod):
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

    with open('growPod.json', 'w') as outJSON:
        json.dump(growPodDictionary, outJSON, ensure_ascii=False, indent=4)


class GrowPod:
    def __init__(self):
        self.uniqueID = 0
        self.ipAddress = ""
        self.port = 80 # default port for UDP communication
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
        self.lightStatus = False
        self.airPump = False
        self.sourcePump = False
        self.drainPump = False
        self.nutrientsPump = False
        self.notes = ""

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
                                  'lightStatus': self.lightStatus,
                                  'airPump': self.airPump,
                                  'sourcePump': self.sourcePump,
                                  'drainPump': self.drainPump,
                                  'nutrientsPump': self.nutrientsPump,
                                  'notes': self.notes}
                             }

        return growPodDictionary

    def resetGrowPod(self):
        self.uniqueID = 0
        self.ipAddress = ""
        self.port = 80
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
        self.lightStatus = False
        self.airPump = False
        self.sourcePump = False
        self.drainPump = False
        self.nutrientsPump = False
        self.notes = ""
