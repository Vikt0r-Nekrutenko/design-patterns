from Composite import Composite


class Multiply(Composite):
    def __init__(self, *args):
        Composite.__init__(self, 1)
        for arg in args:
            self.add(arg)

    def operation(self):
        for expression in self._subexpressions:
            self._value *= expression.operation()

        return self._value