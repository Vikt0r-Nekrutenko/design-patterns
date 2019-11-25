from abc import ABC, abstractmethod


class Component(ABC):
    def __init__(self, value):
        self._value = value

    @property
    def Value(self):
        return self._value

    def add(self, component):
        pass

    @abstractmethod
    def operation(self):
        pass
