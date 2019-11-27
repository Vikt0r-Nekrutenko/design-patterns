from abc import ABC, abstractmethod


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, payment):
        pass


class PaymentHandler(Handler):
    _next_handler: Handler = None
    _min_amount = 0
    _percentage = 0

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, payment):
        if self._next_handler:
            return self._next_handler.handle(payment)

        return None


class UnknownPaymentHandler(PaymentHandler):
    _type = None

    def handle(self, payment):
        if payment.type == self._type:
            percentage = payment.amount - payment.amount * self._percentage

            if percentage < self._min_amount:
                print(f"Alarm!!!\n"
                      f"For {payment.type}:\n"
                      f"Percentage = {self._percentage * 100}%\n"
                      f"Minimal amount = {self._min_amount}$\n"
                      f"Your payment amount = {percentage}$\n")
                return None
            payment.amount = percentage
            return payment
        else:
            return super().handle(payment)


class RegularPaymentHandler(UnknownPaymentHandler):
    def __init__(self):
        self._type = "Regular"
        self._min_amount = 5
        self._percentage = 0.05


class StatePaymentHandler(UnknownPaymentHandler):
    def __init__(self):
        self._type = "State"
        self._min_amount = 9000
        self._percentage = 0.01


class PreferentialPaymentHandler(UnknownPaymentHandler):
    def __init__(self):
        self._type = "Preferential"
        self._min_amount = 50
        self._percentage = 0.02


class InterbankPaymentHandler(UnknownPaymentHandler):
    def __init__(self):
        self._type = "Interbank"
        self._min_amount = 200
        self._percentage = 0