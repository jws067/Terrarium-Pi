import RPi.GPIO as GPIO
from time import sleep
class Pump():
    def __init__(self, time):
        self.time = time
        self.pump = 17
        Initialize(self.pump)

    @property
    def time (self):
        return self._time
    @time.setter
    def time (self, val):
        self._time = int(val)

    @property
    def pump (self):
        return self._pump
    @pump.setter
    def pump(self, val):
        
        self._pump = int(val)

    def Run():
        GPIO.output(pin, 1)
        sleep(self.time)
        GPIO.output(pin, 0)
def Initialize(pin):
    GPIO.setup(pin, GPIO.OUT)
    
