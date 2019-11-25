from FactoryMethod.Blocks import *


class Creator(ABC):
    @abstractmethod
    def create(self):
        pass


class SquareCreator(Creator):
    def create(self):
        return Square()


class IBlockCreator(Creator):
    def create(self):
        return IBlock()


class LBlockCreator(Creator):
    def create(self):
        return LBlock()


class TBlockCreator(Creator):
    def create(self):
        return TBlock()