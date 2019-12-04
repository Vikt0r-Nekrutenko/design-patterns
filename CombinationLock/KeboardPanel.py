import re
from Receiver import Receiver


class KeyboardPanel:
    out_0: Receiver = None

    def invoke(self):
        signal = input()
        if re.match(r"\d+|ctrl|call", signal):
            self.out_0.receive_signal(signal)
        else:
            exit(0)
