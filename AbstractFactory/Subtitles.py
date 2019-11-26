from abc import ABC, abstractmethod


class Subtitles(ABC):
    @abstractmethod
    def language(self):
        pass


class UaSubtitles(Subtitles):
    def language(self):
        return "ua"


class EnSubtitles(Subtitles):
    def language(self):
        return "en"
