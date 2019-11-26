from abc import ABC, abstractmethod


class Soundtrack(ABC):
    @abstractmethod
    def language(self):
        pass


class UaSoundtrack(Soundtrack):
    def language(self):
        return "ua"
        
        
class EnSoundtrack(Soundtrack):
    def language(self):
        return "en"
