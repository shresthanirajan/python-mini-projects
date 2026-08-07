class Pets:
    def __init__(self, name, animal_type,age):
        self.name = name
        self.animal_type = animal_type
        self.age = age
        self.energy = 2
        self.hunger = 3

    def show_info(self):
        print(f"Animal is {self.animal_type}, Name is {self.name} and is {self.age} years old.")
        print(f"{self.name} Currently has {self.energy} energy Left.")
        print(f"{self.name} current hunger level: {self.hunger}")

    def birthday(self):
        self.age += 1
        print(f"{self.name} is now {self.age} Years old!")

    def rename(self, name):

        print(f"{self.name} Has been Renamed To {name}")
        self.name = name

    def change_animal_type(self, change_animal):
        print(f"{self.animal_type} has been changed to {change_animal}")
        self.animal_type = change_animal

    def is_older_than(self, other_pet):
        if self.age > other_pet.age:
            print(f"{self.name} is older.")

        elif other_pet.age > self.age:
            print(f"{other_pet.name} is older then {self.name}")
        else:
            print(f"{self.name} and {other_pet.name} Have the same Age ")


    def feed(self, food_name):
        if self.hunger <= 0:
            print(f"{self.name} is Full of Food, can't feed")
            return
        print(f"{self.name} ate {food_name}.")
        self.hunger -= 1

        if self.energy >= 5:
            print(f"Maximum Energy Reached")
        else:

            self.energy += 1
            print(f"{self.name} Energy Increased By 1")
            print(f"{self.name} Currently has {self.energy} energy Left.")
        print(f"{self.name} current hunger level: {self.hunger}")


    def play(self):

        if self.energy <= 0:
            print(f"{self.name} Has no energy to play")
        else:
            self.hunger += 1
            self.energy -= 1
            print(f"{self.name} is playing.")
            print(f"{self.name} Currently has {self.energy} Energy Left.")

    def sleep(self):
        if self.energy >= 5:
            print(f"{self.name} has to much energy, cannot sleep!")
        else:
            self.energy += 2
            print(f"{self.name} is currently Sleeping.")
            print(f"{self.name} Currently has {self.energy} Energy Left.")
            if self.energy > 5:
                self.energy = 5

    def status(self):

        if 0 >= self.energy and self.hunger >= 4:
            print(f"{self.name} is VERY TIRED!! And Very Hungry!!")

        elif (1 >= self.energy) and (2<= self.hunger <= 3):
            print(f"{self.name} has Low energy! AND Very hungry!")

        elif self.energy >= 2 and self.hunger <= 1:
            print(f"{self.name} has enough energy AND is not hungry")

        else:
            print(f"{self.name} is doing Good!")


class PetOwner:
    def __init__(self, name):
        self.name = name
        self.pets = []

    def add_pet(self, pet):
        print(f"{pet.name} has been Added.")
        self.pets.append(pet)



    def show_pets(self):
        if not self.pets:
            print("You have no Pets!")
        else:
            for pets in self.pets:
                pets.show_info()

    def remove_pet(self, pet):
        if not self.pets:
            print("No pets to Remove!")
        else:
            for pet_remove in self.pets:
                if pet.lower() == pet_remove.name.lower():
                    self.pets.remove(pet_remove)
                    print(f"{pet_remove.name} Successfully Removed!")
                    return
            else:
                print(f"Couldn't Find {pet} to remove!")


    def find_pet(self, pet):
        if not self.pets:
            print("No Pets to Find!")
        else:
            for pet_find in self.pets:
                if pet.lower() == pet_find.name.lower():
                    print(f"{pet_find.name} HAS BEEN FOUND!")
                    return
            else:
                print(f"Couldn't Find {pet}!")


owner = PetOwner("Nirajan")

pet1 = Pets("Max", "Dog", 2)
pet2 = Pets("Luna", "Cat", 3)


owner.add_pet(pet1)
owner.find_pet("maxx")