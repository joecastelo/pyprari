from data_structures.measure import *

def test_base_measure():
    b_measure = BaseMeasure(10,"W")
    assert str(b_measure) == "1.0e+01 W"
def test_measure():
    measure = Measure(5500,"Mmph",True)
    assert str(measure) == "5.5e+09 mph"
    measure_no_trans = Measure(100,"Mton",False)
    assert str(measure_no_trans) == "1.0e+02 Mton"
