from abc import ABC, abstractmethod


class Movable(ABC):
    @abstractmethod
    def move(self):
        pass


class Walking(Movable):
    def move(self):
        print("walking", end=' ')


class Flying(Movable):
    def move(self):
        print("flying", end=' ')


class WalkingAndFlying(Walking, Flying):
    def move(self):
        Walking.move(self)
        print("and", end=' ')
        Flying.move(self)
