from abc import ABC, abstractmethod
from datetime import date


class Prescription(ABC):
    def __init__(self, appointment, validity):
        self._appointment = appointment
        self._validity = validity

    @property
    def appointment(self):
        return self._appointment

    @property
    def validity(self):
        return self._validity

    @abstractmethod
    def clone(self, new_validity):
        pass


class DoctorsPrescription(Prescription):
    def __init__(self, appointment, validity):
        Prescription.__init__(self, appointment, validity)

    def clone(self, new_validity):
        return DoctorsPrescription(self.appointment, new_validity)


prescription = DoctorsPrescription("xxx", date.today())

elongated_prescription = prescription.clone(date(date.today().year, 12, 31))

print(f"ORIGINAL: {prescription.appointment}. Validity to {prescription.validity}", end='\n\n')

print(f"ELONGATED: {elongated_prescription.appointment}. Validity to {elongated_prescription.validity}", end='\n\n')
