import re
from Handler import *
from ComponentsTypes import Receiver

class DisplaySignalHandler(Handler):
    def handle(self, signal):
        if re.search(r"^\d+$", signal):
            return signal
        return super().handle(signal)


class DigitalDisplay(Receiver):
    def __init__(self, lcd_display):
        self.__lcd = lcd_display
        self.__lcd_handler = DisplaySignalHandler()

    def receive_signal(self, signal):
        if self.__lcd_handler.handle(signal):
            self.__lcd.display(signal)
