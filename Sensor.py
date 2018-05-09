import RPi.GPIO as GPIO
from time import sleep
sensor = 5
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN)

class Sensor(object):
    def MoistChk(self):
        print not GPIO.input(sensor)
        return not GPIO.input(sensor)
