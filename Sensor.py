import RPi.GPIO as GPIO
from time import sleep
sensor = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN)

class Sensor(object):
    #MoistChk returns True if there is moisture in soil
    def MoistChk(self):
        #not GPIO.input(sensor) is used because sensor module naturally sends a True signal when it doesn't detect moisture
        return not GPIO.input(sensor)
