class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"${amount} successfully deposited from {self.owner} Account.")
        else:
            print("Invalid Deposit amount!")

    def withdraw(self, amount):
        if self.__balance >= amount:
            if amount > 0:
                self.__balance -= amount
                print(f"${amount} successfully withdraw from {self.owner} Account.")
            else:
                print("Please enter Valid Number!")

        else:
            print("Not enough funds")

    def show_balance(self):
        print(f"{self.owner} your current balance: ${self.__balance}")

    @property
    def balance(self):
        return self.__balance

timmy = BankAccount("Timmy", 5000)
print(timmy.balance)
