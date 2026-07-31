


def view_expenses():
    if not expenses:
        print("No Expenses!")
    else:
        print("All Expenses:")
        for view_exp in expenses:
            for name, cost in view_exp.items():
                print(f"{name}: ${cost}")

def add_expenses():
        expense_name = input("Enter expense name: ")
        expense_amount = int(input("Enter expense amount: "))
        expenses.append({expense_name:expense_amount})
        print(f"{expense_name} Successfully Added With ${expense_amount}")

def search_expense():
    search_an_expense = input("Enter the expense you want to search: ")
    for view_exp in expenses:
       if view_exp.items() == search_an_expense:
           print("here")





expenses = [
    {"Food": 20},
    {"Uber": 15}
]

while True:
    user_option = input("1. View expenses\n2. Add expense\n3. Search expense\n4. Remove Expense\n5. View Total spent\n6. Exit\nChoose an Option: ")
    if user_option == "1":
        view_expenses()


    elif user_option == "2":
        add_expenses()
    elif user_option == "3":
        search_expense()
    elif user_option == "4":
        print("Remove Expense")
    elif user_option == "5":
        print("View Total Spent")
    elif user_option == "6":
        break

    else:
        print("Invalid Input!")

