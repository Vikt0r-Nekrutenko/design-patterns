from PyQt5 import QtWidgets
from Handler import *


class ControlKeyHandler(Handler):
    __ctrl_key = ['2', '2', '2', '2']

    def handle(self, password):
        if password == self.__ctrl_key:
            return "controled"
        else:
            return super().handle(password)


class PassKeyHandler(Handler):
    __pass_key = ['1', '1', '1', '1']

    def handle(self, password):
        if password == self.__pass_key:
            return "Unlocked"
        else:
            return super().handle(password)
