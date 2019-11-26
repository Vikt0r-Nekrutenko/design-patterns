from Observer.Observers import *


class Subscriber(Observer, ABC):
    def __init__(self, name):
        self._name = name


class JournalSubscriber(Subscriber):
    def update(self):
        print(self._name, "received the journal")


class NewspaperSubscriber(Subscriber):
    def update(self):
        print(self._name, "received the newspaper")