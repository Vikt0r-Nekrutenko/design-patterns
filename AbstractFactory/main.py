from AbstractFactory.MovieFactories import UaMovieFactory, EnMovieFactory, ABC


class Movie:
    def __init__(self, movie_factory, name):
        self.__name = name
        self.__subtitles = movie_factory.create_subtitles()
        self.__soundtrack = movie_factory.create_soundtrack()

    @property
    def subtitles(self):
        return self.__subtitles.language()

    @property
    def soundtrack(self):
        return self.__soundtrack.language()

    @subtitles.setter
    def subtitles(self, movie_factory):
        self.__subtitles = movie_factory.create_subtitles()
        self.__soundtrack = movie_factory.create_soundtrack()

    @soundtrack.setter
    def soundtrack(self, movie_factory):
        self.__subtitles = movie_factory.create_subtitles()
        self.__soundtrack = movie_factory.create_soundtrack()

    def info(self):
        print(f"Info about film {self.__name}:\n\tSoundtrack: {self.soundtrack}\n\tSubtitles : {self.subtitles}", end="\n\n")


movie1 = Movie(UaMovieFactory(), "Predator")
movie1.info()

movie2 = Movie(EnMovieFactory(), "Predator VS Alien")
movie2.info()

movie1.soundtrack = EnMovieFactory()
movie1.info()

