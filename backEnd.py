class SmartHome:
    def __init__(self):
        self.devices = []

    def addDevice(self, device):
        self.devices.append(device)
    
    def getDevice(self):
        return self.devices
    
    def getDeviceAt(self, index):
        return self.devices[index]
    
    def toggleSwitch(self, index):
        self.devices[index].toggleSwitch()

    def turnOnAll(self):
        for device in self.devices:
            if not device.getSwitchedOn():
                device.toggleSwitch()
        
    def turnOffAll(self):
        for device in self.devices:
            if device.getSwitchedOn():
                device.toggleSwitch()
    
    def __str__(self):
        output = "Smart Home contains: \n"
        for i in range (len(self.devices)):
            output = output + "{}\n".format(self.devices[i])
        return output
    
def testSmartHome():
    smartHome = SmartHome()
    plug1 = SmartPlug()
    cust1 = SmartHeater()
    plug2 = SmartPlug()
    plug3 = SmartPlug()
    cust2 = SmartHeater()
    smartHome.addDevice(plug1)
    smartHome.addDevice(cust1)
    smartHome.addDevice(plug2)
    smartHome.addDevice(plug3)
    smartHome.addDevice(cust2)

    plug2.toggleSwitch()
    plug2.setConsumptionRate(45)
    cust1.setHeaterSetting(4)

    print(smartHome)
    smartHome.turnOnAll()
    print(smartHome)
    smartHome.turnOffAll()
    print(smartHome)


class SmartPlug:
    def __init__(self):
        self.switchedOn = False
        self.consumptionRate = 0

    def toggleSwitch(self):
        self.switchedOn = not self.switchedOn
       #if self.getSwitchedOn == True:
            #self.switchedOn = False
        #else:
            #self.switchedOn = True
        
    def getSwitchedOn(self):
        return self.switchedOn

    def setConsumptionRate(self, consumption):
        curConsumption = consumption + self.consumptionRate
        if 0 <= curConsumption <= 150:
            self.consumptionRate += consumption
        else:
            print("This is an invalid consumption rate")

    def getConsumptionRate(self):
        return self.consumptionRate
    
    def __str__(self):
        if self.switchedOn == True:
            return "Plug: {}, Consumption: {}".format("On", self.consumptionRate)
        else:
            return "Plug: {}, Consumption: {}".format("Off", self.consumptionRate)

    
def testSmartPlug():
    smartPlug = SmartPlug()
    smartPlug.toggleSwitch()
    print(smartPlug.getSwitchedOn())
    print(smartPlug.getConsumptionRate())
    #consumption = int(input("Please enter your consumption rate that should a number between 0 and 150: "))
    smartPlug.setConsumptionRate(45)
    print(smartPlug.getConsumptionRate())
    print(smartPlug)


class SmartHeater:
    def __init__(self):
        self.switchedOn = False
        self.heaterSetting = 0
    
    def getSwitchedOn(self):
        return self.switchedOn

    def toggleSwitch(self):
        self.switchedOn = not self.switchedOn
        #if self.getSwitchedOn == True:
            #self.switchedOn = False
        #else:
            #self.switchedOn = True

    def setHeaterSetting(self, setting):
        curSetting = setting + self.heaterSetting
        if 0 <= curSetting <= 5:
            self.heaterSetting += setting
        else:
            print("This is an invalid setting")
    
    def getHeaterSetting(self):
        return self.heaterSetting

    def __str__(self):
        if self.switchedOn == True:
            return "Heater: {}, Consumption: {}".format("On", self.heaterSetting)
        else:
            return "Heater: {}, Consumption: {}".format("Off", self.heaterSetting)
    
def testDevice():
    smartHeater = SmartHeater()
    smartHeater.toggleSwitch()
    print(smartHeater.getSwitchedOn())
    print(smartHeater.getHeaterSetting())
    #setting = int(input("Please enter your heater setting which is 0-5: ")
    smartHeater.setHeaterSetting(4)
    print(smartHeater.getHeaterSetting())
    print(smartHeater)
    

#testSmartPlug()
#testDevice()
testSmartHome()