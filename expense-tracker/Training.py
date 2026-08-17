class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def show_balance(self):
        print(f"{self.owner} has ${self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount} deposited successfully into {self.owner}'s account!")
            print(f"Remaining balance: ${self.balance}")
        else:
            print("invalid amount")


    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"${amount} was withdrawn from {self.owner}'s account!")
                print(f"Remaining balance: ${self.balance}")
            else:
                print("Not enough Money to Withdraw")
        else:
            print("Invalid Amount")

    def transfer(self, other_account, transfer_amount):
        if self == other_account:
            print("You cannot transfer money to the same account")
            return
        if transfer_amount > 0:
            if self.balance >= transfer_amount:
                self.balance -= transfer_amount
                other_account.balance += transfer_amount
                print(
                    f"${transfer_amount} has been transferred from {self.owner} to {other_account.owner} Account!")

                print(f"{self.owner}'s balance: ${self.balance}")
                print(f"{other_account.owner}'s balance: ${other_account.balance}")
            else:
                print("Not Enough Balance to transfer")
        else:
            print("Invalid Input")

account1 = BankAccount("Nirajan", 500)
account2 = BankAccount("Sarah", 1000)
account1.transfer(account1,500)







