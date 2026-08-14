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
    def __init__(self, name, health, level, strength, damage):
        super().__init__(name, health, level)
        self.strength = strength
        self.damage = damage

    def attack(self):
        print(f"Warrior: {self.name} Strength: {self.strength} attacking with a sword")

class Mage(Character):
    def __init__(self, name, health, level, mana, damage):
        super().__init__(name, health, level)
        self.mana = mana
        self.damage = damage

    def attack(self):
        print(f"{self.name} attacks with magic using {self.mana} mana")

class Archer(Character):
    def __init__(self, name, health, level, damage):
        super().__init__(name, health, level)
        self.arrow = "arrow"
        self.damage = damage

    def attack(self):
        print(f"{self.name} attacks with an arrow")







