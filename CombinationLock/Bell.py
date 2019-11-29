import winsound
from Handler import *
from ComponentsTypes import Receiver


class BellSignalHandler(Handler):
    def handle(self, signal):
        if signal == "Bell":
            return signal
        return super().handle(signal)


class Bell(Receiver):
    __bell_handler = BellSignalHandler()

    def receive_signal(self, signal):
        if self.__bell_handler.handle(signal):
            for _ in range(5):
                winsound.Beep(2500, 500)
