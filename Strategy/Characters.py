from abc import ABC


class Character(ABC):
    def __init__(self, move_type):
        self._type = None
        self._move_type = move_type

    def move(self):
        print(self._type, end=": ")
        self._move_type.move()
        print()

    @property
    def move_type(self):
        return self._move_type

    @move_type.setter
    def move_type(self, move_type):
        self._move_type = move_type


class Orc(Character):
    def __init__(self, move_type):
        Character.__init__(self, move_type)
        self._type = "Orc"


class Pixie(Character):
    def __init__(self, move_type):
        Character.__init__(self, move_type)
        self._type = "Pixie"


class Pegas(Character):
    def __init__(self, move_type):
        Character.__init__(self, move_type)
        self._type = "Pegas"


class MagicGroup(Character):
    def __init__(self, move_type):
        Character.__init__(self, move_type)
        self._group = []
        self._type = "Magic group"

    def move(self):
        Character.move(self)

        for character in self._group:
            character.move()

    def add(self, *characters):
        self._group.extend(characters)
        for character in characters:
            character.move_type = self._move_type
