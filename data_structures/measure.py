import numpy as np
from datetime import datetime
 
transformations = {
    "p" : 1e-12,
    "n" : 1e-9,
    "micro" : 1e-6,
    "m" : 1e-3,
    "c" : 1e-2,
    "d" : 1e-1,
    "da" : 1e1,
    "h" : 1e2,
    "k" : 1e3,
    "M" : 1e6,
    "G" : 1e9,
}

class BaseMeasure:
    def __init__(self,measure:float ,unit : str):
        self.measure = measure
        self.unit = unit
    def __str__(self):
        return f"Value : {self.measure} {self.unit}"


class Measure(BaseMeasure):
    def __init__(self,measure:float ,unit : str, transformed : bool = False):
        super().__init__(self,measure,unit)
    def decode_measure(self):
        if self.transformed:
            for transf in transformations.keys():
                if transf in self.unit[:len(transf)]: ## Always first cm
                    self.user_transform = transformations[self.unit[:len(transf)]]
                    self.si_unit = self.unit.replace(self.unit[:len(transf)],"")    


class TimeMixin:
    def __init__(self, time : datetime = datetime.now()):
        self.time = time
    def __str__(self):
        return f"At time {self.time}"

class DistanceMixin:
    def __init__(self,distance:Measure)
        assert distance.unit == "m", "Distance must be in m"
        self.distance = distance
    def __srt__(self):
        return f"At distance {self.distance}"


        

