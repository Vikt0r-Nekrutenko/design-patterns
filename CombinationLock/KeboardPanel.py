import re
from Receiver import Receiver


class KeyboardPanel:
    def invoke(self) -> str:
        signal = input()
        if re.match(r"\d+|ctrl|call", signal):
            return signal
        else:
            exit(0)
