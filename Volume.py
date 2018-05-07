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
    if (unit == "liter"):
        cups = vol / .236588
        seconds = round(cups / .125)
    if (unit == "cup"):
        seconds = round(vol / .125)
    if (unit == "milliliter"):
        cups = vol / (.236588 * 1000)
        seconds = round(cups / .125)
    if (unit == "fluidOz"):
        seconds = vol    
    return seconds
