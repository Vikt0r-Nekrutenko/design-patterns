import threading
import time
from Handler import *
from ComponentsTypes import Receiver


class LockState(ABC):
    @abstractmethod
    def change(self, lock):
        pass

    @abstractmethod
    def get(self):
        pass

class LockedState(LockState):
    def change(self, lock):
        lock.state = UnlockedState()

    def get(self):
        return "Locked"


class UnlockedState(LockState):
    def change(self, lock):
        lock.state = LockedState()

    def get(self):
        return "Unlocked"


class LockSignalHandler(Handler):
    def handle(self, signal):
        if signal == "Locked" or signal == "Unlocked":
            return signal
        return super().handle(signal)


class Lock(Receiver):
    def __init__(self, lock):
        self.__lock = lock
        self.__lock_handler = LockSignalHandler()
        self.state = LockedState()

    def receive_signal(self, signal):
        if self.__lock_handler.handle(signal) and self.state.get() == "Locked":
            threading.Timer(0, self.change_state).start()

    def change_state(self):
        self.state.change(self)
        for sec in range(5):
            self.__lock.setText(f"Door {self.state.get()}. Time to closing: {5 - sec} seconds.")
            time.sleep(1.0)
        self.state.change(self)
        self.__lock.setText(f"Door {self.state.get()}.")
