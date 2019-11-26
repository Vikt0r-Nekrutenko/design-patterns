from Observer.Observable import *


class Observer(ABC):
    @abstractmethod
    def update(self):
        pass


class Post(Observable, Observer):
    def __init__(self):
        self.__subscribers = []

    def add_observer(self, observer):
        self.__subscribers.append(observer)

    def notify_observers(self):
        print("Post send the production")
        for subscriber in self.__subscribers:
            subscriber.update()

    def update(self):
        print("Post received the production")
        self.notify_observers()