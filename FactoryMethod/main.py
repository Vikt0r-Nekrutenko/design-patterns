from FactoryMethod.Creators import *
import random

blocks = [
    SquareCreator(),
    IBlockCreator(),
    LBlockCreator(),
    TBlockCreator()
]

for _ in range(5):
    creator = random.choice(blocks)
    block = creator.create()
    block.print()
    print()
