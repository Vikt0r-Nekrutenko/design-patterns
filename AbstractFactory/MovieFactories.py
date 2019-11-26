from AbstractFactory.Soundtracks import *
from AbstractFactory.Subtitles import *


class MovieFactory(ABC):
    @abstractmethod
    def create_subtitles(self):
        pass

    @abstractmethod
    def create_soundtrack(self):
        pass


class UaMovieFactory(MovieFactory):
    def create_soundtrack(self):
        return UaSoundtrack()

    def create_subtitles(self):
        return UaSubtitles()


class EnMovieFactory(MovieFactory):
    def create_soundtrack(self):
        return EnSoundtrack()

    def create_subtitles(self):
        return EnSubtitles()
