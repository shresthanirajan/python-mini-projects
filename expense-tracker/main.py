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
    for search_exp in expenses:
        if search_an_expense in search_exp:

            return f"{search_an_expense} ${search_exp[search_an_expense]} in expenses"
    else:
        return f"{search_an_expense} NOT HERE"

def remove_expense():
    if not expenses:
        print("No Expenses to Remove!")
    else:
        remove_item = input("Enter the expense you wanna remove: ")
        for remove_exp in expenses:
            if remove_item in remove_exp:
                 expenses.remove(remove_exp)
                 print(f"{remove_item} has been removed from Expenses!")
                 return

        else:
            print(f"{remove_item}, Doesn't Exist")

def total_spent():
    if not expenses:
        print("No Expenses Spend!")
    else:
        total_amount = 0
        for spend in expenses:
            spend_amount = (list(spend.values())[0])
            total_amount += spend_amount
        print(F"Your total spend Amount is: ${total_amount}")

expenses = [

]

while True:
    user_option = input("1. View expenses\n2. Add expense\n3. Search expense\n4. Remove Expense\n5. View Total spent\n6. Exit\nChoose an Option: ")
    if user_option == "1":
        view_expenses()


    elif user_option == "2":
        add_expenses()
    elif user_option == "3":
        print(search_expense())
    elif user_option == "4":
         remove_expense()
    elif user_option == "5":
        total_spent()
    elif user_option == "6":
        break

    else:
        print("Invalid Input!")
