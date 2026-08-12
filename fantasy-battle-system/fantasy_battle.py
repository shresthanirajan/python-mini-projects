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


class Warrior(Character):
    def __init__(self, name, health, level, strength):
        super().__init__(name, health, level)
        self.strength = strength

    def attack(self):
        print(f"Warrior: {self.name} Strength: {self.strength} attacking with a sword")


warrior = Warrior("Sigma", 100, 12, 50)
warrior.take_damage(99)
print(warrior.health)



