from abc import ABC, abstractmethod


class LockState(ABC):
    info = None

    @abstractmethod
    def change(self):
        pass


class LockedState(LockState):
    def __init__(self):
        self.info = "locked"

    def change(self):
        return UnlockedState()


class UnlockedState(LockState):
    def __init__(self):
        self.info = "unlocked"

    def change(self):
        return LockedState()