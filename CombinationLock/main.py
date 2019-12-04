import threading
from abc import ABC, abstractmethod
from LCD import LCD
from Lock import Lock
from Bell import Bell
from Receiver import Receiver
from KeboardPanel import KeyboardPanel


class State(ABC):
    info = None

    @abstractmethod
    def change(self):
        pass


class ReadState(State):
    def __init__(self):
        self.info = "read"

    def change(self):
        print(self.info)
        return WriteState()


class WriteState(State):
    def __init__(self):
        self.info = "write"

    def change(self):
        print(self.info)
        return ReadState()


class AbstractHandler:
    _password = None
    _next_handler = None
    state = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)

        return None


class PassHandler(AbstractHandler):
    def __init__(self):
        self._password = "1111"
        self.state = ReadState()

    def handle(self, request):
        if self.state.info == "read":
            if self._password == request:
                return True
            return False
        elif self.state.info == "write":
            if len(request) == 4:
                self._password = request
                print(f"Pass key changed: {self._password}")
                self.state = self.state.change()
                return True
            return False


class CtrlHandler(AbstractHandler):
    def __init__(self):
        self._password = "2222"
        self.state = ReadState()

    def handle(self, request):
        if self.state.info == "read":
            if self._password == request:
                return True
            return False
        elif self.state.info == "write":
            if len(request) == 4:
                self._password = request
                print(f"Ctrl key changed: {self._password}")
                self.state = self.state.change()
                return True
            return False


class Microprocessor(Receiver):
    out_0 = LCD()
    out_1 = Bell()
    out_2 = Lock()

    pkh = PassHandler()
    ckh = CtrlHandler()

    def receive_signal(self, signal):
        if self.pkh.handle(signal) == True:
            if self.out_2.state.info == "locked":
                self.procedure()
                th = threading.Timer(10, self.procedure)
                th.start()
        elif self.out_2.state.info == "unlocked":
            if signal == "call":
                if self.ckh.handle(signal) == True:
                    print("CALL!!!")
                    self.ckh.state = self.ckh.state.change()
            else:
                if self.out_2.state.info == "unlocked":
                    if self.ckh.handle(signal) == True:
                        self.pkh.state = self.pkh.state.change()
        self.out_0.receive_signal(signal)

    def procedure(self):
        self.out_2.receive_signal(None)
        print(f"Lock: {self.out_2.state.info}")


if __name__ == "__main__":
    kp = KeyboardPanel()
    mic = Microprocessor()
    kp.out_0 = mic
    while True:
        kp.invoke()
