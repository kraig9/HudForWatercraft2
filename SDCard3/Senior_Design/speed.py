import RPi.GPIO as GPIO
import time

speedPin = 3
counter = 0
previous = 0
deltaT = 0
prevT = 0
cycles = 0
speed = 0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(speedPin, GPIO.IN)

print("Speed module started")
try:
    prevT=time.time()
    while 1:
        deltaT=time.time()-prevT
        #print(deltaT)
        if deltaT >= 1:
            cycles = counter
            speed = (cycles/10000)-.0005
            counter = 0
            prevT = time.time()
        print (speed)
        if GPIO.input(speedPin):
            #print("high")
            if previous == 0:
                counter = counter + 1
            previous = 1
        else:
            #print("low")
            previous = 0
       
    
except KeyboardInterrupt:
    GPIO.cleanup()
