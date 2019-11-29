# This Python file uses the following encoding: utf-8
import sys

from window import *
from PyQt5 import QtWidgets, QtCore
from PasswordHandlers import *
from DigitalDisplay import DigitalDisplay
from Bell import Bell
from ComponentsTypes import Receiver, Sender
from Lock import Lock


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.one_btn.clicked.connect(lambda: self.send_signal(self.ui.one_btn))
        self.ui.two_btn.clicked.connect(lambda: self.send_signal(self.ui.two_btn))
        self.ui.three_btn.clicked.connect(lambda: self.send_signal(self.ui.three_btn))
        self.ui.four_btn.clicked.connect(lambda: self.send_signal(self.ui.four_btn))
        self.ui.five_btn.clicked.connect(lambda: self.send_signal(self.ui.five_btn))
        self.ui.six_btn.clicked.connect(lambda: self.send_signal(self.ui.six_btn))
        self.ui.seven_btn.clicked.connect(lambda: self.send_signal(self.ui.seven_btn))
        self.ui.eight_btn.clicked.connect(lambda: self.send_signal(self.ui.eight_btn))
        self.ui.nine_btn.clicked.connect(lambda: self.send_signal(self.ui.nine_btn))
        self.ui.zero_btn.clicked.connect(lambda: self.send_signal(self.ui.zero_btn))

        self.ui.control_btn.clicked.connect(lambda: self.send_signal(self.ui.control_btn))
        self.ui.bell_btn.clicked.connect(lambda: self.send_signal(self.ui.bell_btn))

        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def send_signal(self, key):
        for component in self.components:
            component.receive_signal(key.text())


class Microprocessor(Receiver, Sender):
    def __init__(self):
        self.__pass_key = PassKeyHandler()
        self.__ctrl_key = ControlKeyHandler()

        self.__input = []

        self.__pass_key.set_next(self.__ctrl_key)

        self.pass_key = ['1', '1', '1', '1']
        self.ctrl_key = ['2', '2', '2', '2']
        self.cp = False

    def receive_signal(self, signal):
        self.__input.append(signal)
        self.send_signal("".join(self.__input))

        if len(self.__input) == 4:
            result = self.__pass_key.handle(self.__input)

            if result:
                self.send_signal(result)
            self.__input.clear()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()

    mic = Microprocessor()
    lcd = DigitalDisplay(window.ui.lcdNumber)
    bell = Bell()
    lock = Lock(window.ui.label)

    mic.add_receiver(lock)
    mic.add_receiver(lcd)

    window.add_component(mic)
    window.add_component(bell)

    window.show()
    sys.exit(app.exec_())

"""
            container = []
            self.ui.one_btn.clicked.connect(lambda: container.append(self.ui.one_btn.text()))
            self.ui.one_btn.clicked.connect(lambda: self.ui.lcdNumber.display("".join(container)))

            self.ui.two_btn.clicked.connect(lambda: container.append(self.ui.two_btn.text()))
            self.ui.two_btn.clicked.connect(lambda: self.ui.lcdNumber.display("".join(container)))

            self.ui.three_btn.clicked.connect(lambda: container.append(self.ui.three_btn.text()))
            self.ui.three_btn.clicked.connect(lambda: self.ui.lcdNumber.display("".join(container)))

            self.ui.four_btn.clicked.connect(lambda: container.append(self.ui.four_btn.text()))
            self.ui.four_btn.clicked.connect(lambda: self.ui.lcdNumber.display("".join(container)))

            self.ui.five_btn.clicked.connect(lambda: container.append(self.ui.five_btn.text()))
            self.ui.five_btn.clicked.connect(lambda: self.ui.lcdNumber.display("".join(container)))

            self.ui.six_btn.clicked.connect(lambda: container.append(self.ui.six_btn.text()))
            self.ui.six_btn.clicked.connect(lambda: self.ui.lcdNumber.display("".join(container)))

            self.ui.seven_btn.clicked.connect(lambda: container.append(self.ui.seven_btn.text()))
            self.ui.seven_btn.clicked.connect(lambda: self.ui.lcdNumber.display("".join(container)))

            self.ui.eight_btn.clicked.connect(lambda: container.append(self.ui.eight_btn.text()))
            self.ui.eight_btn.clicked.connect(lambda: self.ui.lcdNumber.display("".join(container)))

            self.ui.nine_btn.clicked.connect(lambda: container.append(self.ui.nine_btn.text()))
            self.ui.nine_btn.clicked.connect(lambda: self.ui.lcdNumber.display("".join(container)))

            self.ui.zero_btn.clicked.connect(lambda: container.append(self.ui.zero_btn.text()))
            self.ui.zero_btn.clicked.connect(lambda: self.ui.lcdNumber.display("".join(container)))

            self.ui.control_btn.clicked.connect(lambda: container.clear())
            self.ui.control_btn.clicked.connect(lambda: self.ui.lcdNumber.display(""))

            self.ui.bell_btn.clicked.connect(lambda: container.clear())
            self.ui.bell_btn_btn.clicked.connect(lambda: self.ui.lcdNumber.display(""))
"""
