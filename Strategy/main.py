from Strategy.Characters import *
from Strategy.MovableTypes import *


orc = Orc(Walking())
orc.move()

pixie = Pixie(Flying())
pixie.move()

pegas = Pegas(WalkingAndFlying())
pegas.move()

group = MagicGroup(Flying())
group.add(orc, pixie, pegas)
group.move()
