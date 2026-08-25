numbers = [5, 8, 5, 2, 8, 8, 10, 2, 14, 14, 14]
seen = set()
duplicates = set()
for num in numbers:
  if num in seen:
    duplicates.add(num)
  else:
    seen.add(num)

print(f"Duplicates: {duplicates}")
print(f"Number of unique duplicates: {len(duplicates)}")

tasks = [
    {"task": "study python", "done": False},
    {"task": "finish calculus", "done": True}
]

# def add_task(task_name):
#   tasks({
#     "task": task_name

#   })


# add_task("go to gym")
# print(tasks)


tasks = [
    {"task": "study python", "done": False},
    {"task": "python leetcode practice", "done": False},
    {"task": "finish calculus homework", "done": True},
    {"task": "go to gym", "done": True}
]


def search_tasks(search_term):
  found = False
  for task in tasks:
    if search_term.lower() in task["task"].lower():
      found = True
      print(f"{task["task"]} was found") 
  if not found:
    print("Not Found!")


search_tasks("PYTHON")


expenses = [
    {"name": "food", "amount": 25},
    {"name": "gas", "amount": 40},
    {"name": "coffee", "amount": 6}
]

def remove_expense(expense_number):
  for index, expense in enumerate(expenses):
    index += 1
    expenses.pop(expense_number-1)
    return

def expenses_in_range(min_amount, max_amount):
  for expense in expenses:
    if min_amount >= 0 or max_amount <= 0:
      if min_amount > max_amount:
        print("Invalid range")
        return
      else:
        if min_amount <= expense["amount"] <= max_amount:
          print(expense)
    else:
      print("Amounts cannot be negative")
      return

# remove_expense(2)
# print(expenses)
expenses_in_range(7,25)


print(" ")
inventory = {
    "keyboard": {"price": 70, "stock": 12},
    "mouse": {"price": 30, "stock": 4},
    "monitor": {"price": 220, "stock": 7},
    "headphones": {"price": 90, "stock": 2}
}

lowest_stock = inventory["keyboard"]["price"]
lowest_stock_name = ''

for name, item in inventory.items():
  if item["stock"] < lowest_stock:
    lowest_stock = item["stock"]
    lowest_stock_name = name


print(f"Lowest stock product: {lowest_stock_name}")
print(f"Stock: {lowest_stock}")


expenses = [
    {"name": "rent", "amount": 900},
    {"name": "food", "amount": 200},
    {"name": "gas", "amount": 100}
]

higest_amount = expenses[0]["amount"]
higest_expense = expenses[0]["name"]


for amount in expenses:
  if higest_amount < amount["amount"]:
    higest_amount = amount["amount"]
    higest_expense = amount["name"]
    
    
                      

print(higest_amount) 
print(higest_expense)

#9 Should Print nothing 

expenses = [
    {"name": "food", "amount": 25},
    {"name": "gas", "amount": 40},
    {"name": "coffee", "amount": 6},
    {"name": "books", "amount": 40}
]

def find_expenses_over(limit):
  if limit > 0:
    found = False
    for expense in expenses:
      if expense["amount"] > limit:
        print(expense["amount"])
        found = True
      if not found:
        print("No expenses Found")
        return
  else:
    print("limit cannot be negative")

find_expenses_over(2)