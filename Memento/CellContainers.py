from abc import ABC, abstractmethod


class CellContainer(ABC):
    def __init__(self):
        self._container = []

    def __setitem__(self, index, value):
        index *= 2
        self._container[index] = value

    def __getitem__(self, index):
        index *= 2
        return self._container[index]

    @abstractmethod
    def print(self):
        pass


class Row(CellContainer):
    def __init__(self, line):
        CellContainer.__init__(self)
        self._container = line

    def print(self):
        for i in self._container:
            print(i, end='')


class Matrix(CellContainer):
    def __init__(self):
        CellContainer.__init__(self)
        self._container = [
            Row([' ', '│', ' ', '│', ' ']),
            Row(['─', '┼', '─', '┼', '─']),
            Row([' ', '│', ' ', '│', ' ']),
            Row(['─', '┼', '─', '┼', '─']),
            Row([' ', '│', ' ', '│', ' ']),
        ]

    def print(self):
        for i in self._container:
            i.print()
            print()