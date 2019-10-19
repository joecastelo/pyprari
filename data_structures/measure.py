import numpy as np
from datetime import datetime
 
class BaseMeasure:
    def __init__(self,measure:float ,unit : str, time : datetime = datetime.now()):
        self.time = time
        self.measure = measure
        self.unit = unit
    def __str__(self):
        return f"Measure made at {str(self.time)}, value: {self.measure} {self.unit}"

    def convert(self,*args,*kwargs):
        pass

