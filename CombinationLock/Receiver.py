from abc import ABC, abstractmethod


class Receiver(ABC):
    @abstractmethod
    def receive_signal(self, signal):
        pass