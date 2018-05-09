import RPi.GPIO as GPIO
from time import sleep
sensor = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN)

class Sensor(object):
    def MoistChk(self):
        return not GPIO.input(sensor)
