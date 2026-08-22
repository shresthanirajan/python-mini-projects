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

def total_expenses():
  total = 0
  highest_amount = expenses[0]["amount"]
  lowest_amount = expenses[0]["amount"]

  highest_expenses_name = expenses[0]["name"]
  lowest_expenses_name = expenses[0]["name"]
  
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

print(highest_expenses_name, highest_amount)
print(lowest_expenses_name, lowest_amount)

