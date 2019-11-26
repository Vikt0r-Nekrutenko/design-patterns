from State.States import *


class Order:
    def __init__(self, state):
        self.__state: OrderState = state

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state):
        self.__state = state

    def create(self):
        self.state.create(self)

    def consider(self):
        self.state.consider(self)

    def snooze(self):
        self.state.snooze(self)

    def reject(self):
        self.state.reject(self)

    def withdraw(self):
        self.state.withdraw(self)

    def approve(self):
        self.state.approve(self)


order = Order(CreateOrderState())
order.consider()
order.snooze()

order.consider()
order.reject()

print()

order = Order(CreateOrderState())
order.consider()
order.approve()

print()

order = Order(CreateOrderState())
order.consider()
order.withdraw()