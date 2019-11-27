from ChainOfResposibility.PaymentHandlers import *
from random import randint


class Payment:
    def __init__(self, type, amount):
        self.id = randint(1000, 9999)
        self.type = type
        self.amount = amount

    def __str__(self):
        return f"Payment: Id[{self.id}] Type[{self.type}] Amount[{format(self.amount, '.2f')}$]"


def bank(payment):
    regular = RegularPaymentHandler()               # lvl 1 prior
    preferential = PreferentialPaymentHandler()     # lvl 2 prior
    state = StatePaymentHandler()                   # lvl 3 prior
    interbank = InterbankPaymentHandler()           # lvl 4 prior

    regular.set_next(preferential).set_next(state).set_next(interbank)  # chain of handlers

    result = regular.handle(payment)

    if result:
        print(f"\t\tBank:\t{result} was made!\n")
    else:
        print(f"\t\tBank:\t{payment} was aborted\n")


common_person = Payment("Regular", randint(5, 5000))
print(f"Common person:\t{common_person}")
bank(common_person)

state_person = Payment("State", randint(9000, 100000))
print(f"State person:\t{state_person}")
bank(state_person)

common_person = Payment("Else", randint(5, 5000))   # nonexistent type of payment
print(f"Common person:\t{common_person}")
bank(common_person)

old_person = Payment("Preferential", randint(50, 800))
print(f"Old person:\t{old_person}")
bank(old_person)

bank_employee = Payment("Interbank", randint(200, 10000))
print(f"Bank employee:\t{bank_employee}")
bank(bank_employee)

old_person = Payment("Preferential", 5)     # too low amount
print(f"Old person:\t{old_person}")
bank(old_person)

""" 
.........................OUTPUT.................................
Common person:	Payment: Id[5654] Type[Regular] Amount[4603.00$]
.........Bank:	Payment: Id[5654] Type[Regular] Amount[4372.85$] was made!
..........................................................................
.State person:	Payment: Id[1389] Type[State] Amount[68340.00$]
.........Bank:	Payment: Id[1389] Type[State] Amount[67656.60$] was made!
.........................................................................
Common person:	Payment: Id[9986] Type[Else] Amount[768.00$]
.........Bank:	Payment: Id[9986] Type[Else] Amount[768.00$] was aborted
........................................................................
...Old person:  Payment: Id[5801] Type[Preferential] Amount[69.00$]
.........Bank:	Payment: Id[5801] Type[Preferential] Amount[67.62$] was made!
.............................................................................
Bank employee:	Payment: Id[5909] Type[Interbank] Amount[5042.00$]
.........Bank:	Payment: Id[5909] Type[Interbank] Amount[5042.00$] was made!
............................................................................
.Old person:	Payment: Id[6922] Type[Preferential] Amount[5.00$]
................Alarm!!!
................For Preferential:
................Percentage = 2.0%
................Minimal amount = 50$
................Your payment amount = 4.9$
.........Bank:	Payment: Id[6922] Type[Preferential] Amount[5.00$] was aborted
"""