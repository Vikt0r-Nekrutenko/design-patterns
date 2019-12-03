from CombinationLock.Receiver import Receiver
from CombinationLock.LockStates import *


class Lock(Receiver):
    state = LockedState()

    def receive_signal(self, signal):
        self.state = self.state.change()