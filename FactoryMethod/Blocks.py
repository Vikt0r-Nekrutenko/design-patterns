from abc import ABC, abstractmethod


class Block(ABC):
    def __init__(self):
        self._shape = None

    def print(self):
        print(self._shape)


class Square(Block):
    def __init__(self):
        Block.__init__(self)
        self._shape = "██\n██"


class IBlock(Block):
    def __init__(self):
        Block.__init__(self)
        self._shape = "█\n█\n█\n█"


class LBlock(Block):
    def __init__(self):
        Block.__init__(self)
        self._shape = "█\n███"


class TBlock(Block):
    def __init__(self):
        Block.__init__(self)
        self._shape = " █\n███"