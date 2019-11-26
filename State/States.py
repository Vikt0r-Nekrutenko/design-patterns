from abc import ABC, abstractmethod


class OrderState(ABC):
    @abstractmethod
    def create(self, order):
        pass

    @abstractmethod
    def consider(self, order):
        pass

    @abstractmethod
    def snooze(self, order):
        pass

    @abstractmethod
    def reject(self, order):
        pass

    @abstractmethod
    def withdraw(self, order):
        pass

    @abstractmethod
    def approve(self, order):
        pass


class CreateOrderState(OrderState):
    def create(self, order):
        pass

    def consider(self, order):
        print("Order created and considered")
        order.state = ConsiderOrderState()

    def snooze(self, order):
        print("Order created and snoozed")
        order.state = SnoozeOrderState()

    def reject(self, order):
        pass

    def withdraw(self, order):
        pass

    def approve(self, order):
        pass


class ConsiderOrderState(OrderState):
    def create(self, order):
        pass

    def consider(self, order):
        pass

    def snooze(self, order):
        print("Order considered and snoozed")
        order.state = SnoozeOrderState()

    def reject(self, order):
        print("Order considered and rejected")
        order.state = RejectOrderState()

    def withdraw(self, order):
        print("Order considered but withdrawn")
        order.state = WithdrawOrderState()

    def approve(self, order):
        print("Order considered and approved")
        order.state = ApproveOrderState()


class SnoozeOrderState(OrderState):
    def create(self, order):
        pass

    def consider(self, order):
        print("Order was snoozed but now considered")
        order.state = ConsiderOrderState()

    def snooze(self, order):
        pass

    def reject(self, order):
        pass

    def withdraw(self, order):
        pass

    def approve(self, order):
        pass


class RejectOrderState(OrderState):
    def create(self, order):
        pass

    def consider(self, order):
        pass

    def snooze(self, order):
        pass

    def reject(self, order):
        pass

    def withdraw(self, order):
        pass

    def approve(self, order):
        pass


class WithdrawOrderState(OrderState):
    def create(self, order):
        pass

    def consider(self, order):
        pass

    def snooze(self, order):
        pass

    def reject(self, order):
        pass

    def withdraw(self, order):
        pass

    def approve(self, order):
        pass


class ApproveOrderState(OrderState):
    def create(self, order):
        pass

    def consider(self, order):
        pass

    def snooze(self, order):
        pass

    def reject(self, order):
        pass

    def withdraw(self, order):
        print("Order approved but withdrawn")
        order.state = WithdrawOrderState()

    def approve(self, order):
        pass