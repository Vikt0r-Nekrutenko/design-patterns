import threading
from abc import ABC, abstractmethod
from LCD import LCD
from Lock import Lock
from Bell import Bell
from Receiver import Receiver
from KeboardPanel import KeyboardPanel


class PasswordHandler:
    def __init__(self, password):
        self._tmp = None
        self._password = password

    def read(self, password) -> bool:
        if self._password == password:
            return True
        return False

    def write(self, password) -> bool:
        if len(password) == 4:
            self._tmp = password
            print(f"\t{self._password} will be changed to {password}")
            return True
        return False

    def accept(self):
        if self._tmp:
            print(f"\t{self._password} was changed to {self._tmp}")
            self._password = self._tmp
            self._tmp = None
            return True
        return False

    @property
    def password(self):
        return self._password


class Handler(ABC):
    def __init__(self, mic):
        self._mic = mic
        self._next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


class OpenLockHandler(Handler):
    def handle(self, request):
        if self._mic.out_2.state.info == "unlocked":
            return super().handle(request)
        return None


class ClosedLockHandler(Handler):
    def handle(self, request):
        if self._mic.out_2.state.info == "locked":
            return super().handle(request)
        return None


class PassKeyHandler(Handler):
    pass_key = "1111"

    def handle(self, request):
        if request == self.pass_key:
            self._mic.procedure()
            th = threading.Timer(10, self._mic.procedure)
            th.start()
            return super().handle(request)
        return None


class CtrlKeyHandler(Handler):
    ctrl_key = "2222"

    def handle(self, request):
        inp = self._mic.in_0.invoke()
        if inp == self.ctrl_key:
            return super().handle(request)
        return None


class CallButtonHandler(Handler):
    def __init__(self, mic):
        Handler.__init__(self, mic)
        self.ctrl_flag = False

    def handle(self, request):
        if request == "call":
            self.ctrl_flag = True
            self._mic.out_1.receive_signal(None)
        return super().handle(request)


class PassKeyChangeHandler(Handler):
    def handle(self, request):
        inp = self._mic.in_0.invoke()
        if len(inp) == 4:
            print(f"\t{inp} will be next pass key")
            if self._mic.cbh.ctrl_flag:
                self.set_next(self._mic.ckah)
            else:
                self.set_next(self._mic.pkah)
            return super().handle(inp)
        return None


class PassKeyAcceptHandler(Handler):
    def __init__(self, pass_key_handler, mic):
        Handler.__init__(self, mic)
        self._pkh = pass_key_handler

    def handle(self, request):
        inp = self._mic.in_0.invoke()

        if inp == "ctrl":
            self._pkh.pass_key = request
            print(f"\t{request} is next pass key")
            return super().handle(request)
        return None


class Microprocessor(Receiver):
    in_0 = KeyboardPanel()
    out_0 = LCD()
    out_1 = Bell()
    out_2 = Lock()

    def __init__(self):
        self.olh = OpenLockHandler(self)
        self.clh = ClosedLockHandler(self)

        self.pkh = PassKeyHandler(self)
        self.ckh = CtrlKeyHandler(self)

        self.pkch = PassKeyChangeHandler(self)

        self.cbh = CallButtonHandler(self)
        self.pkah = PassKeyAcceptHandler(self.pkh, self)
        self.ckah = PassKeyAcceptHandler(self.ckh, self)

        self.cbh.set_next(self.clh).set_next(self.pkh).set_next(self.olh).set_next(self.ckh).set_next(self.ckh).set_next(self.pkch)

    def receive_signal(self, signal):
        signal = self.in_0.invoke()
        self.cbh.handle(signal)
        self.out_0.receive_signal(signal)

    def procedure(self):
        self.out_2.receive_signal(None)
        print(f"Lock: {self.out_2.state.info}")


if __name__ == "__main__":
    kp = KeyboardPanel()
    mic = Microprocessor()
    while True:
        mic.receive_signal(None)
