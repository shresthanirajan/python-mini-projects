expenses = [
    {"name": "food", "amount": 25},
    {"name": "gas", "amount": 40},
    {"name": "coffee", "amount": 6}
]

def expenses_in_range(min_amount, max_amount):
  if min_amount < 0 or 0 > max_amount:
    print("Amounts cannot be negative ")
    return
  if min_amount > max_amount:
    print("Invalid Range")
    return

  for expense in expenses:
    if max_amount >= expense["amount"] >= min_amount:
      print(expense["amount"])
expenses_in_range(39,40)

#2
tasks = [
    {"task": "study python", "done": False}
]

def add_task(task_name):
  tasks.append({
    "task": task_name,
    "done": False
  })
add_task("Working out")
print(tasks)
#3

tasks = [
    {"task": "Study Python", "done": False},
    {"task": "Python LeetCode", "done": True},
    {"task": "Calculus Homework", "done": False}
]

def search_tasks(search_term):
  found = False
  for task in tasks:
    if search_term.lower() in task["task"].lower():
      print(task["task"])
      found = True
  if not found:
    print("Not Found Task!")
    return

search_tasks("Homework")

#4
numbers = [2, 4, 7, 2, 9, 4, 4, 10, 7]
seen = set()
duplicates = set()
for num in numbers:
  if num in seen:
    duplicates.add(num)
  else:
    seen.add(num)
print(f"seen: {seen}")
print(f"duplicates: {duplicates}")
unique_duplicates = len(duplicates)
print(unique_duplicates)


#5
expenses = [
    {"name": "food", "amount": 25},
    {"name": "rent", "amount": 900},
    {"name": "gas", "amount": 40}
]

highest_amount = expenses[0]["amount"]
highest_name = expenses[0]["name"]
for expense in expenses:
  if highest_amount < expense["amount"]:
    highest_amount = expense["amount"]
    highest_name = expense["name"]
print(highest_name,highest_amount)

#6
inventory = {
    "keyboard": {"stock": 8},
    "mouse": {"stock": 3},
    "monitor": {"stock": 6}
}
lowest_stock = inventory["keyboard"]["stock"]
lowest_name = "keyboard"
for name, stock in inventory.items():
  if lowest_stock > stock["stock"]:
    lowest_stock = stock["stock"]
    lowest_name = name
print(lowest_name)
print(lowest_stock)

#7 GETs 10 as the output because We are returning that then we are storing that value into results


#8 It because first it finds the name alex for example then straighjt returns it without prining  the other alexander
def search_names(search_term):
    names = ["alex", "alexander", "maya"]
    for name in names:
        if search_term in name:
            print(name)
            

search_names("alex")

#9

students = [
    {"name": "Alex", "grades": [80, 90, 70]},
    {"name": "Maya", "grades": [95, 88, 92]}
]

print(students[1]["grades"][1])

#10
products = [
    {"name": "apple", "price": 2, "stock": 10},
    {"name": "banana", "price": 1, "stock": 0},
    {"name": "orange", "price": 3, "stock": 5}
]

def available_products(max_price):
  if max_price < 0:
    print("No Negative Values")
    return
  found = False
  for product in products:
    if product["stock"] > 0:
      if max_price >= product["price"]:
            print(f"{product['name']}: ${product['price']}")     
            found = True
    
  if not found:
    print("No Products Found")

available_products(3)

#Drill 2 #It will print Inside Function first since we are still caliing then what ever value that it returns here for example
#we return Alex is stored inside Result and that result will print Alex

#Second Casw will Return the print function and return Alex wont work and it will be stored inside result and it will print Inside Function
def get_name():
    return print("Inside function")
    return "Alex"

result = get_name()

print(result)
