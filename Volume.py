class Volume (object):
    def __init__(self, vol, unit):
        self.vol= vol
        self.unit = unit
        self.time = timeRun(self.vol, self.unit)

    @property
    def vol (self):
        return self._vol
    @vol.setter
    def vol (self, val):
        self._vol = float(val)

    @property
    def unit (self):
        return self._unit

    @unit.setter
    def unit (self, val):
        self._unit = str(val)

def timeRun(vol, unit):
    if (unit == "Liters"):
        cups = vol / .236588
        seconds = float(cups / .125)
    if (unit == "Cups"):
        seconds = float(vol / .125)
    if (unit == "milliliters"):
        cups = vol / (.236588 * 1000)
        seconds = float(cups / .125)
    if (unit == "FluidOz"):
        seconds = float(vol)    
    return seconds
