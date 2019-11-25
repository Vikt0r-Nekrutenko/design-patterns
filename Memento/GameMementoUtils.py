import copy


class GameMemento:
    def __init__(self, place, player):
        self.__place = place
        self.__player = player

    @property
    def place(self):
        return self.place

    @property
    def player(self):
        return self.player


class GameHistory:
    def __init__(self):
        self.__history = []

    def add_saving(self, state):
        self.__history.append(copy.deepcopy(state))

    def last_saving(self):
        if len(self.__history) != 1:
            self.__history.pop()
        return self.__history[-1]
