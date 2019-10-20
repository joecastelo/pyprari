import numpy as np
from datetime import datetime
from dateutil.parser import parse as dt_parse
import re

transformations = {
    "p" : 1e-12,
    "n" : 1e-9,
    "u" : 1e-6,
    "m" : 1e-3,
    "c" : 1e-2,
    "d" : 1e-1,
    "da" : 1e+1,
    "h" : 1e+2,
    "k" : 1e+3,
    "M" : 1e+6,
    "G" : 1e+9,
}

class BaseMeasure:
    def __init__(self,value:float ,unit : str):
        self.value = value
        self.unit = re.sub('[^A-Za-z0-9]+', '', unit)
    def __str__(self):
        print_value = "%.1e" % self.value
        return f"{print_value} {self.unit}"

class Measure(BaseMeasure):
    def __init__(self,value:float ,unit : str, transformed : bool = False):
        super().__init__(value,unit)
        self.transformed = transformed
        self.si_value,self.si_unit = self.decode_value()
    def decode_value(self):
        si_value,si_unit = self.value,self.unit
        if self.transformed:
            for transf in transformations.keys():
                if transf in self.unit[:len(transf)]: ## Always first cm
                    user_transform = transformations[self.unit[:len(transf)]]
                    si_value = self.value * user_transform
                    si_unit = self.unit[len(transf):]
        return si_value,si_unit
    def __str__(self):
        print_value = "%.1e" % self.si_value
        return super().__str__() if not self.transformed else f"{print_value} {self.si_unit}"



class TimeMixin:
    def __init__(self, time : datetime = datetime.now()):
        self.time = dt_parse(time)
    def __str__(self):
        return f"At time {self.time}"

class DistanceMixin:
    def __init__(self,distance:Measure):
        assert distance.unit == "m", "Distance must be in m"
        self.distance = distance
    def __srt__(self):
        return f"At distance {self.distance}"
