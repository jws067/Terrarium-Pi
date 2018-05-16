from Tkinter import *
from ttk import *
import time, threading
from threading import *
from Sensor import *
from Volume import *
from Pump import *
import RPi.GPIO as GPIO



class Application(Frame):
    """A GUI application"""
    def __init__(self, parent):
        """Initialize the Frame"""
        Frame.__init__(self, parent)
        self.createWidgets()
        self.ThreadOnline = False
        self.x = 0
        self.Mminutes = 60000
        self.Sminutes = 60
        self.Hours = 24
        self.time=0.0
        self.Vol=0.0
        self.Unit=""
        self.Sense = Sensor()

    def createWidgets(self):
        """Create the window layout"""
        #toolbar setup
        menubar = Menu(root)
        filemenu = Menu(menubar,tearoff = 0)
        filemenu.add_command(label = "Standard")
        filemenu.add_command(label = "Demo")
        menubar.add_cascade(label = "Mode", menu = filemenu)
        root.config(menu = menubar)
        
        #Label
        self.display = Label(self, text = "units", anchor = W)
        self.display.grid(row = 0, column = 3,\
                          sticky = N+E+W+S)
        self.display = Label(self, text = "ones", anchor = W)
        self.display.grid(row = 0, column = 1,\
                          sticky = N+E+W+S)
        self.display = Label(self, text = "tenths", anchor = W)
        self.display.grid(row = 0, column = 2,\
                          sticky = N+E+W+S)
        self.display = Label(self, text = "Progress to Next Watering:")
        self.display.grid(row = 3, column = 0,columnspan = 4, sticky = N+E+W+S)
        #combo box
        self.pack(fill = BOTH, expand = 1)
        self.drop_down = Combobox(self,font = ("Comic Sans",12), width = 7, state = "readonly")
        self.drop_down['values']= ("Liters","FluidOz","milliliters","Cups")
        self.drop_down.current(0)
        self.drop_down.grid(row = 1, column =3 ,sticky = N+E+W+S)
        #enter button
        self.button1 = Button(self, text = "Enter", command = self.stopIt)
        self.button1.grid(row = 2, column = 3, sticky = W)
        #Progress bar
        self.progress = Progressbar(self,maximum = 60,orient = "horizontal", length = 200,mode = "determinate")
        self.progress.grid(row = 4, column = 0, columnspan = 4 ,sticky = N+E+W+S )
        #Spinner
        self.ones=Spinbox(self,width = 2, from_=1, to =9, state = "readonly")
        self.ones.grid(row = 1, column = 1, sticky = N)
        self.tenths=Spinbox(self,width = 2, from_=0, to =9, state = "readonly")
        self.tenths.grid(row = 1, column = 2, sticky = N)

    #Create timer thread
    def CreateThread(self):
        """creates a new thread"""
        self.stopFlag = Event()
        self.thread = MyThread(self.stopFlag)
        self.thread.start()
        self.ThreadOnline = True
    #Stop Timer and Start Timer
    def stopIt(self):
        """Starts and stops the timer"""
        if (self.ThreadOnline):
            #turn off thread
            self.stopFlag.set()
            self.ThreadOnline = False
            self.x=0
            self.progress.stop()
            self.Enable()
            self.thread.rst()
        elif (not self.ThreadOnline):
            #set self.vol and self.unit
            self.Vol, self.Unit = self.info()
            #turn on thread and progress bar
            self.time = Volume(self.Vol,self.Unit).time
            self.CreateThread()
            self.progress.start(self.Mminutes)
            self.Disable()

    #returns user input
    def info(self):
        """returns input from user"""
        flt = float(self.ones.get()) + (float(self.tenths.get())/10)
        return flt, self.drop_down.get()

    #disable variable editing
    def Disable(self):
        """disables variable editing"""
        self.tenths["state"] = "disabled"
        self.ones["state"] = "disabled"
        self.drop_down["state"] = "disabled"

    #Enable variable editing
    def Enable(self):
        """enables variable editing"""
        self.tenths["state"] = "readonly"
        self.ones["state"] = "readonly"
        self.drop_down["state"] = "readonly"

    #Standard mode
    def Standard(self):
        self.Mminutes = 60000
        self.Sminutes = 60
        self.Hours = 24

    #Demo mode
    def Demo(self):
        self.Mminutes = 1000
        self.Sminutes = 1
        self.Hours = 1

    #checks soil
    def Check(self):
        sen = self.Sense.MoistChk()
        if(sen == 1):
            pump = Pump(app.time)
            pump.Run()
            GPIO.cleanup(pump.pump)
        else:
            pass

class MyThread(Thread):
    def __init__(self, event):
        Thread.__init__(self)
        self.stopped = event
        self.x = 0
        self.hours = 0

    def run(self):
        while not self.stopped.wait(app.Sminutes):
            self.x +=1
            #hour counter
            if(self.x>=60 ):
                self.x = 0
                self.hours += 1
                #pump activator
                if(app.Sminutes == 1 and self.hours >=1):
                    self.hours = 0
                    app.progress.stop()

                    # call a function
                    app.Check()
                    app.progress.start(app.Mminutes)
                elif(app.Sminutes == 60 and self.hours >=24):
                    self.hours = 0
                    app.progress.stop()
                
                    #function here
                    app.Check()                                        
                    app.progress.start(app.Mminutes)
    def rst(self):
        self.x = 0
        self.hours = 0

############################ MAIN ############################


try:
    height = 200
    width = 200
    root = Tk()
    root.title("Terrarium Pi")
    
    
    
    app = Application(root)
    #taskbar setup
    menubar = Menu(root)
    filemenu = Menu(menubar,tearoff = 0)
    filemenu.add_command(label = "Standard", command = app.Standard)
    filemenu.add_command(label = "Demo", command = app.Demo)
    menubar.add_cascade(label = "Mode", menu = filemenu)
    root.config(menu = menubar)
    root.mainloop()
finally:
    GPIO.cleanup()
    if(app.ThreadOnline):
        try:
            app.stopIt()
        except TclError:
            pass
