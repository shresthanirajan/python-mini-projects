#position, name, age, level salary

se1 = ["Software Engineer", "Max", 20, "Junior", 5000]
se2 = ["Software Engineer", "Lisa", 20, "Senior", 7000]
d1 = ["Designer", "Phillipp"]


#class
class SoftwareEngineer:


    #Class attribute
    alias = "Keyboard Magician"

    def __init__(self, name, age, level, salary):
        #Instance Attributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    #Instance method
    def code(self):
        print(f"{self.name} is writing code...")

    def code_in_language(self, language):
        print(f"{self.name} is writing code...{language}")

    #dunder method
    def __str__(self):
        information = f"name = {self.name}, age = {self.age}, level = {self.level}"
        return information

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def  entry_salary(age):
        if age < 25:
            return 5000
        if age < 30:
            return 7000
        return 9000


#Instance
se1 = SoftwareEngineer("Max", 20, "Junior", 5000)
se2 = SoftwareEngineer( "Lisa", 20, "Senior", 7000)
se3 = SoftwareEngineer( "Lisa", 27, "Senior", 7000)

se1.code()
se2.code()
se1.code_in_language("Python")
se2.code_in_language("C++")

print(se2 == se3)

SoftwareEngineer.entry_salary(24)


