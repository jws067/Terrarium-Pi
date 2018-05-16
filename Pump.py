import RPi.GPIO as GPIO
from time import sleep
class Pump():
    def __init__(self, time):
        self.time = time
        print self.time
        self.pump = 27
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pump, GPIO.OUT)

    @property
    def time (self):
        return self._time
    @time.setter
    def time (self, val):
        self._time = float(val)

    @property
    def pump (self):
        return self._pump
    @pump.setter
    def pump(self, val):
        
        self._pump = int(val)

    def Run(self):
        GPIO.output(self.pump, 1)
        sleep(self.time)
        GPIO.output(self.pump, 0)
    
