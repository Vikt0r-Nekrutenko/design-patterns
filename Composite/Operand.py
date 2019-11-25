from Component import Component


class Operand(Component):
    def __init__(self, value):
        Component.__init__(self, value)

    def operation(self):
        if type(self._value) == Component:
            return self._value.Value
        else:
            return self._value
