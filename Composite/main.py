from Composite import Composite
from Operand import Operand
from Add import Add
from Multiply import Multiply


#(10 + 25) * 4 + 52 * (3 + 6)
expression = Composite(0)

first_brackets = Add(Operand(10), Operand(25))
mul = Multiply(first_brackets, Operand(4))

second_brackets = Add(Operand(3), Operand(6))
mul2 = Multiply(second_brackets, Operand(52))

add = Add(mul, mul2)
expression.add(add)

print(expression.operation())
