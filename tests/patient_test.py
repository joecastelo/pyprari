import patient

person_instance = patient.Person(12,170,120,21,"male")

def test_person():
    assert isinstance(person_instance,patient.Person)

def test_person_str():
    assert isinstance(str(person_instance),str)
    print(person_instance)

patient_instance = patient.Patient(12,170,120,25,"male","1","SomeDisease")

def test_patient():
    assert isinstance(patient_instance,patient.Person)
    assert isinstance(patient_instance,patient.Patient)

def test_patient_str():
    assert isinstance(str(patient_instance),str)
    print(patient_instance)
