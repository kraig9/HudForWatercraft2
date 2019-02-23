
#includes/imports
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.IN)

#inputs
def depthFinder():
    print('depthFinder subroutine started')
    #p = GPIO.PWM(12, 0.125)
    #p = GPIO.PWM(12, 5)
    #p.start(50)
    #input('Press return to stop:')
    #p.stop()
    #GPIO.cleanup()
    while True:
        if GPIO.input(12):
            print ("input is high")
        else:
            print ("input is low")
    return 0

def fuelGauge():
    print('fuelGauge subroutine started')
    return 0

def windSpeed():
    print('windSpeed subroutine started')
    return 0

def windDirection():
    print('windDirection subroutine started')
    return 0

def boatSpeed():
    print('boatSpeed subroutine started')
    return 0

#outputs
def displayOut():
    print('displayOut subroutine started')
    return 0

#main function
def main():
    print("Python main function started")
    depthFinder()
    fuelGuage()
    windSpeed()
    windDirection()
    boatSpeed()
    displayOut()

#program/module start    
if __name__ == '__main__':
    main()
