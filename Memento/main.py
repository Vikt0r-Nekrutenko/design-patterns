from Memento.Game import Game
from Memento.GameMementoUtils import GameHistory


game = Game()
saves = GameHistory()
saves.add_saving(game.save_state())

while True:
    print("Enter 1 if you want restore the last saving: ", end='')
    n = input()
    if n == "q":
        break
    elif n == "1":
        game.restore_state(saves.last_saving())
    else:
        game.execute_move()
        saves.add_saving(game.save_state())
