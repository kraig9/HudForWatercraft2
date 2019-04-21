try:
    # for Python2
    import Tkinter as tk   ## notice capitalized T in Tkinter
except ImportError:
    # for Python3
    import tkinter as tk  ## notice lowercase 't' in tkinter here
import time
import serial
from threading import Thread
from time import sleep

# global variables
global gwindSpeed
global gfuel
global gwindDirection
global gdepth
global gboatSpeed


class GUI:
    windSpeed = 0
    fuel = 0
    windDirection = 0
    depth = 0
    boatSpeed = 0

    # Constructor
    def __init__(self, windSpeed, fuel, windDirection, depth, boatSpeed):
        self.windSpeed = windSpeed
        self.fuel = fuel
        self.windDirection = windDirection
        self.depth = depth
        self.boatSpeed = boatSpeed

    def guiRoutine(self):
        # This block makes the base window and makes it fullscreen.
        # Credit from https://gist.github.com/TravisJoe/5576258
        root = tk.Tk()
        root.attributes('-fullscreen', True)
        root.bind('<Escape>', lambda e: root.destroy())
        root.configure(background='black')

        w = tk.Label(root, text="Wind Speed", fg='yellow', bg='black', font=("", 100))
        w.grid(row=0, column=0, sticky=tk.NW)

        textDispw = tk.Text(root, height=2, width=8, fg='yellow', bg='black', font=("", 100))
        textDispw.grid(row=1, column=0, sticky=tk.NW)
        textDispw.insert(tk.END, self.windSpeed)

        x = tk.Label(root, text="Fuel", fg='yellow', bg='black', font=("", 100))
        x.place(rely=0, relx=1, x=0, y=0, anchor=tk.NE)

        textDispx = tk.Text(root, height=2, width=8, fg='yellow', bg='black', font=("", 100))
        textDispx.place(rely=0, relx=1, x=0, y=150, anchor=tk.NE)
        textDispx.insert(tk.END, self.fuel)

        #mid = tk.Label(root, text="Boat Speed", fg='yellow', bg='black', font=("", 100))
        #mid.place(rely=0, relx=.5, x=0, y=0, anchor=tk.N)

        #textDispMid = tk.Text(root, height=2, width=8, fg='yellow', bg='black', font=("", 100))
        #textDispMid.place(rely=0, relx=.5, x=0, y=150, anchor=tk.N)
        #textDispMid.insert(tk.END, self.boatSpeed)

        y = tk.Label(root, text="Boat Speed", fg='yellow', bg='black', font=("", 100))
        y.place(rely=1, relx=0, x=0, y=0, anchor=tk.SW)

        textDispy = tk.Text(root, height=2, width=8, fg='yellow', bg='black', font=("", 100))
        textDispy.place(rely=1, relx=0, x=0, y=-150, anchor=tk.SW)
        textDispy.insert(tk.END, self.boatSpeed)

        z = tk.Label(root, text="Depth", fg='yellow', bg='black', font=("", 100))
        z.place(rely=1, relx=1, x=0, y=0, anchor=tk.SE)

        textDispz = tk.Text(root, height=2, width=8, fg='yellow', bg='black', font=("", 100))
        textDispz.place(rely=1, relx=1, x=0, y=-150, anchor=tk.SE)
        textDispz.insert(tk.END, self.boatSpeed)

        root.attributes("-alpha", 0.5)

        while True:
            self.windSpeed = format(gwindSpeed, '.2f') + " M/s"
            self.fuel = format(gfuel, '.2f') + "%"
            #self.windDirection = format(gwindSp, '.2f') + " M/s"
            self.depth = format(gdepth, '.2f') + " M"
            self.boatSpeed = format(gboatSpeed, '.2f') + " M/s"

            # self.windSpeed += 1
            # self.fuel += 1
            # self.windDirection += 1
            # self.depth += 1
            # self.boatSpeed += 1

            textDispw.delete('1.0', tk.END)
            textDispw.insert(tk.END, self.windSpeed)
            textDispw.update_idletasks()

            textDispx.delete('1.0', tk.END)
            textDispx.insert(tk.END, self.fuel)
            textDispx.update_idletasks()

            #textDispMid.delete('1.0', tk.END)
            #textDispMid.insert(tk.END, self.boatSpeed)
            #textDispMid.update_idletasks()

            textDispy.delete('1.0', tk.END)
            textDispy.insert(tk.END, self.boatSpeed)
            textDispy.update_idletasks()

            textDispz.delete('1.0', tk.END)
            textDispz.insert(tk.END, self.depth)
            textDispz.update_idletasks()

        root.mainloop()


class ADC:
    def __init__(self, windSpeed, fuel, windDirection, depth, boatSpeed):
        print("inside ADC constructor")
        self.windSpeed = windSpeed
        self.fuel = fuel
        self.windDirection = windDirection
        self.depth = depth
        self.boatSpeed = boatSpeed

    def channelSwitcher(self, arg):
        if b'CH0' in arg:
            print("Channel 0")
        elif b'CH1' in arg:
            print("Channel 1")
        elif b'CH2' in arg:
            print("Channel 2")
        elif b'CH3' in arg:
            print("Channel 3")
            #print("arg is: " + arg)
            mphByte = arg[9:14]
            mphByte = mphByte.decode("utf-8")
            print("mphByte is: " + mphByte)
            #if (mphByte.isdigit()):
            mph = float(mphByte)
            print("mph is: " + str(mph))
            mph = ((mph * 150) / 3.3) - 17.727272727272727764
            print("mph is: " + str(mph))
            global gboatSpeed
            gboatSpeed = mph
        elif b'CH4' in arg:
            print("Channel 4")
        elif b'CH5' in arg:
            print("Channel 5")
            #print("arg is: " + arg)
            mphByte = arg[9:14]
            mphByte = mphByte.decode("utf-8")
            print("mphByte is: " + mphByte)
            #if (mphByte.isdigit()):
            mph = float(mphByte)
            print("mph is: " + str(mph))
            mph = ((mph * 150) / 3.3) - 17.727272727272727764
            print("mph is: " + str(mph))
            global gdepth
            gdepth = mph
        elif b'CH6' in arg:
            print("Channel 6")
        elif b'CH7' in arg:
            print("Channel 7")
            #print("arg is: " + arg)
            mphByte = arg[9:14]
            mphByte = mphByte.decode("utf-8")
            print("mphByte is: " + mphByte)
            #if (mphByte.isdigit()):
            mph = float(mphByte)
            print("mph is: " + str(mph))
            mph = ((mph * 150) / 3.3) - 17.727272727272727764
            print("mph is: " + str(mph))
            global gfuel
            gfuel = mph
        elif b'CH8' in arg:
            print("Channel 8")
        elif b'CH9' in arg:
            print("Channel 9")
            #print("arg is: " + arg)
            mphByte = arg[9:14]
            mphByte = mphByte.decode("utf-8")
            print("mphByte is: " + mphByte)
            #if (mphByte.isdigit()):
            mph = float(mphByte)
            print("mph is: " + str(mph))
            mph = ((mph * 150) / 3.3) - 17.727272727272727764
            print("mph is: " + str(mph))
            global gwindSpeed
            gwindSpeed = mph
        #else:
            #print("not a channel")

    def adcRoutine(self):
        print("inside adcRoutine")
        ser = serial.Serial('/dev/ttyUSB0', 115200)

        printVar = ""

        while True:
            bytesToRead = ser.inWaiting()
            incomingData = ser.readline(bytesToRead)
            #print("bytesToRead is: " + str(bytesToRead))
            # collect_incoming_data(printVar, incomingData)
            str(incomingData)
            self.channelSwitcher(incomingData)
            time.sleep(.01)
            # print(incomingData)


#########Main function#####################################
print("it's here")
gwindSpeed = 0
gfuel = 0
gwindDirection = 0
gdepth = 0
gboatSpeed = 0

adc = ADC(0, 0, 0, 0, 0)
gui = GUI(0, 0, 0, 0, 0)
print("it's here")

# adc.adcRoutine()

adcThread = Thread(target=adc.adcRoutine, args=())
adcThread.start()
print("past adcRouting")
print("gwindSpeed is:" + str(gwindSpeed))

guiThread = Thread(target=gui.guiRoutine, args=())
guiThread.start()
# gui.guiRoutine
print("past guiRoutine")

adcThread.join()
guiThread.join()

