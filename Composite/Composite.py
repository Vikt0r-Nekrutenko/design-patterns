from Component import Component


class Composite(Component):
    def __init__(self, value):
        Component.__init__(self, value)
        self._subexpressions = []

    def add(self, component):
        self._subexpressions.append(component)

    def operation(self):
        for expression in self._subexpressions:
            self._value = expression.operation()
        return self.Value
