from abc import ABC, abstractmethod
import random


class Bacteria(ABC):
    _size = None

    @abstractmethod
    def create(self, time_before_division):
        pass


class KokkosBacteria(Bacteria):
    def __init__(self):
        self._size = 5

    def create(self, time_before_division):
        print(f"Form: kokkos. Size: {self._size}. Time before division: {format(time_before_division, '.2f')}")


class BacillusBacteria(Bacteria):
    def __init__(self):
        self._size = 10

    def create(self, time_before_division):
        print(f"Form: bacillus. Size: {self._size}. Time before division: {format(time_before_division, '.2f')}")


class BacteriaFactory:
    def __init__(self):
        self._bacteria_dict = {
            'Kokkos': KokkosBacteria(),
            'Bacillus': BacillusBacteria(),
        }

    def get_bacteria(self, type_of_bacteria):
        return self._bacteria_dict.get(type_of_bacteria)


init_time = 10
bacteria_factory = BacteriaFactory()

for _ in range(100):
    bacteria = bacteria_factory.get_bacteria(random.choice(['Kokkos', 'Bacillus']))
    if bacteria:
        bacteria.create(init_time)
    if init_time == 0:
        init_time = 10
    init_time -= 0.1
