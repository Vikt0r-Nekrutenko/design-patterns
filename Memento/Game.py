from Memento.CellContainers import Matrix
from Memento.GameMementoUtils import GameMemento, GameHistory


class Game:
    def __init__(self):
        self.__current_player = "X"
        self.__game_place = Matrix()

    def change_player(self):
        if self.__current_player == "X":
            self.__current_player = "O"
        elif self.__current_player == "O":
            self.__current_player = "X"

    def execute_move(self):
        print(f"Player {self.__current_player}, input the x: ", end='')
        x = input()
        print(f"Player {self.__current_player}, input the y: ", end='')
        y = input()

        self.__game_place[int(y)][int(x)] = self.__current_player

        self.change_player()

        self.__game_place.print()

    def save_state(self):
        print("Game saved!")
        return GameMemento(self.__game_place, self.__current_player)

    def restore_state(self, gameMemento):
        self.__game_place = gameMemento.place
        self.__current_player = gameMemento.player
        print("Game restored!")
        self.__game_place.print()