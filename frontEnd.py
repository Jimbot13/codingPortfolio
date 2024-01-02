from tkinter import *
from backEnd import SmartHome, SmartHeater, SmartPlug

mainWin = Tk()
smartHome = SmartHome()

def setUpHome():
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
    
    plug1.toggleSwitch()
    plug2.toggleSwitch()
    plug3.toggleSwitch()
    cust1.toggleSwitch()
    cust2.toggleSwitch()


def setupMainWin():
    mainWin.title("Smart Home")
    mainWin.geometry("300x100")
    mainWin.resizable(False, False)
    mainWin.columnconfigure(index=0, weight=4)
    
    titleLable = Label(mainWin, text="Smart Home")
    titleLable.grid(row=0, column=0, padx=10, pady=10, sticky="n")
    titleLable.config(font=("TkDefaultFont", 12, "bold"))
    listOfPlugs()
    quitBtn = Button(mainWin, text="Quit", command=mainWin.destroy)
    quitBtn.grid(row=0, column=1, padx=15, pady=10, sticky="e")

    toggleOnBtn = Button(mainWin, text="Switch On All", command=smartHome.turnOnAll())
    toggleOnBtn.grid(row=1, column=0, padx=10, pady=2, sticky="w")

    toggleOffBtn = Button(mainWin, text="Switch Off All", command=smartHome.turnOffAll())
    toggleOffBtn.grid(row=2, column=0, padx=10, pady=2, sticky="w")

    
    updateBtn = Button(mainWin, text="Update", command=listOfPlugs)
    updateBtn.grid(row=2, column=1, padx=10, pady=2, sticky="w")

    mainWin.mainloop()

def listOfPlugs():
    height = 50 * ((len(smartHome.devices)) + 2)
    mainWin.geometry("400x{}".format(height))

    for plugIndex in range(len(smartHome.devices)):
        plugs = smartHome.getDeviceAt(plugIndex)

        plugTxt = Text(mainWin, height=2, width=50)
        plugTxt.insert("1.0", str(plugs))
        plugTxt.grid(row = plugIndex + 3, column=0, padx=10, pady=5)

        configBtn = Button(mainWin, text="Toggle this")
        configBtn.grid(row=plugIndex + 3, column=1, padx=10, pady=5)


def main():
    setUpHome()
    setupMainWin()

main()