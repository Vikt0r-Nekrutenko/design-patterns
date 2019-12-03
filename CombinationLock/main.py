import threading
from CombinationLock.LCD import LCD
from CombinationLock.Lock import Lock
from CombinationLock.Bell import Bell
from CombinationLock.Receiver import Receiver
from CombinationLock.KeboardPanel import KeyboardPanel


class Microprocessor(Receiver):
    out_0 = LCD()
    out_1 = Bell()
    out_2 = Lock()

    pass_key = "1111"
    ctrl_key = "2222"

    def receive_signal(self, signal):
        if signal == "call":
            self.out_1.receive_signal(signal)
        else:
            if self.out_2.state.info == "locked":
                if signal == self.pass_key:
                    self.procedure()
                    th = threading.Timer(5, self.procedure)
                    th.start()
            elif self.out_2.state.info == "unlocked":
                if signal == self.ctrl_key:
                    if len(signal) == 4:
                        print("Pass key changed: ", self.pass_key)
                        self.pass_key = signal
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
