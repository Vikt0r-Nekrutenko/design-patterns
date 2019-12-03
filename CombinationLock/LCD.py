from CombinationLock.Receiver import Receiver


class LCD(Receiver):
    def receive_signal(self, signal):
        print(f"LCD: {signal}")