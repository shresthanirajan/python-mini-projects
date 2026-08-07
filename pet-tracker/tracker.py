class Pets:
    def __init__(self, name, animal_type,age):
        self.name = name
        self.animal_type = animal_type
        self.age = age

    def show_info(self):
        print(f"Your Animal is a {self.animal_type}, Name is {self.name} and is {self.age} years old.")

    def birthday(self):
        self.age += 1
        print(f"{self.name} is now {self.age} Years old!")

    def rename(self, name):

        print(f"{self.name} Has been Renamed To {name}")
        self.name = name

    def change_animal_type(self, change_animal):
        print(f"{self.animal_type} has been changed to {change_animal}")
        self.animal_type = change_animal



pet1 = Pets("Max", "Dog", 4)
pet2 = Pets("Luna", "Cat", 2)


pet1.change_animal_type("Cat")
pet1.show_info()

