from abc import ABC, abstractmethod


class Receiver(ABC):
    @abstractmethod
    def receive_signal(self, signal):
        pass


class Sender:
    _receivers: Receiver = []

    def add_receiver(self, receiver):
        self._receivers.append(receiver)

    def send_signal(self, signal):
        for receiver in self._receivers:
            receiver.receive_signal(signal)
