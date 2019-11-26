from abc import ABC, abstractmethod


class Observable(ABC):
    @abstractmethod
    def add_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass


class Publisher(Observable):
    def __init__(self):
        self.__posts = []

    def add_observer(self, observer):
        self.__posts.append(observer)

    def notify_observers(self):
        print("Publisher send the production")
        for post in self.__posts:
            post.update()