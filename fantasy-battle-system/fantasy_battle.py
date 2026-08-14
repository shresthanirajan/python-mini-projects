from Character import Character
from Character import Warrior
from Character import Mage
from Character import Archer
from team import Team

Ares = Warrior(name="Ares", health=100, level=30, strength=75)

Merlin = Mage(name="Merlin", health=100, level=25,mana=50)

Artemis = Archer(name="Artemis", health=85, level=50,)

Ares.show_team()
