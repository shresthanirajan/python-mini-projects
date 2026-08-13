from abc import ABC,abstractmethod

class Character(ABC):
    def __init__(self, name, health, level):
        self.name = name
        self.__health = health
        self.level = level

    @abstractmethod
    def attack(self):
        pass

    @property
    def health(self):
        return self.__health

    def take_damage(self, amount):
        if amount > 0:
            if self.__health >= amount:
                    self.__health -= amount

            else:
                self.__health = 0
        else:
            print("damage must be greater than 0")

    def show_info(self):
        print(f"name: {self.name}, Level: {self.level}, Health: {self.__health}")

class Warrior(Character):
    def __init__(self, name, health, level, strength):
        super().__init__(name, health, level)
        self.strength = strength

    def attack(self):
        print(f"Warrior: {self.name} Strength: {self.strength} attacking with a sword")

class Mage(Character):
    def __init__(self, name, health, level, mana):
        super().__init__(name, health, level)
        self.mana = mana

    def attack(self):
        print(f"{self.name} attacks with magic using {self.mana} mana")

class Archer(Character):
    def __init__(self, name, health, level):
        super().__init__(name, health, level)
        self.arrow = "arrow"

    def attack(self):
        print(f"{self.name} attacks with an arrow")

warrior = Warrior("Sigma", 100, 12, 50)


mage = Mage("Mythical", 100, 30, 75)

queen = Archer("Queen", 85, 75)



characters = [warrior, mage, queen]

for character in characters:
    character.attack()
queen.attack()
mage.attack()
warrior.attack()
