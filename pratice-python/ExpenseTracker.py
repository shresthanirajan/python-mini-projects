expenses = [
    {"name": "food", "amount": 25},
    {"name": "gas", "amount": 40},
    {"name": "coffee", "amount": 6}
]


def show_expenses():
  for name in expenses:
    print(f"{name['name']} - ${name['amount']}")

def add_expense(name, amount):
  expenses.append({
    "name": name,
    "amount": amount
  })

def expensive_expenses(limit):
  for amount in expenses:
    if amount["amount"] > limit:
      print(f"{amount["name"]} - {amount["amount"]}")

def remove_expense(name):
  for i, expense_name in enumerate(expenses):
    if name.lower() in expense_name["name"].lower():
      print("removed")
      expenses.pop(i)
      return
  else:
    print("Not Found")

def update_expense(name, new_amount):
  for expense in expenses:
    if name.lower() in expense["name"].lower():
      expense["amount"] = new_amount
      print(f"{expense['name']} Amount Changed to ${expense['amount']}")
      return
  else:
    print("Not Found!")
    
  

def total_expenses():
  total = 0
  highest_amount = expenses[0]["amount"]
  lowest_amount = expenses[0]["amount"]

  highest_expenses_name = expenses[0]["name"]
  lowest_expenses_name = expenses[0]["name"]
  average = 0 
  for expense in expenses:
    total += expense['amount']
    if expense['amount'] > highest_amount:
      highest_amount = expense['amount']
      highest_expenses_name = expense['name']
    if expense['amount'] < lowest_amount:
      lowest_amount = expense['amount']
      lowest_expenses_name = expense['name']
  return total, highest_amount, highest_expenses_name, lowest_amount, lowest_expenses_name

total_spend, highest_amount, highest_expenses_name, lowest_amount, lowest_expenses_name = total_expenses()

# print(highest_expenses_name, highest_amount)
# print(lowest_expenses_name, lowest_amount)

total = 0
length_expense = 0
for expense in expenses:
  total += (expense["amount"])
  length_expense += 1


average = total/length_expense
print(round(average,2))

expensive_expenses(20)

remove_expense("food")

update_expense("coffee", 500)
show_expenses()