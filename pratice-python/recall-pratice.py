numbers = [4, 7, 4, 9, 7, 10, 4]

seen = set()
duplicates = set()

for num in numbers:
  if num in seen:
    duplicates.add(num)
  else:
    seen.add(num)
print(duplicates)

tasks = [
    {"task": "study python", "done": False},
    {"task": "finish homework", "done": True}
]

tasks.append({
  "task":"go to gym",
  "done": False

})
print(tasks)

#3
for task in tasks:
  if not task["done"]:
    print(task["task"])
#4
contacts = {
    "alex": "111",
    "maya": "222"
}

contacts["sam"] =   "333"
contacts["alex"] = "999"

print(contacts)

#Contacts .items gives you the key and value of the contacts so name and number
#Contacts .values gives you the value it self so it will be numbers only 
#Contacts .Keys gives you the key so the name 

inventory = {
    "apple": {"price": 1.50, "stock": 10},
    "banana": {"price": 0.75, "stock": 4},
    "orange": {"price": 1.25, "stock": 8}
}

lowest_item = inventory["apple"]["stock"]

for name ,value in inventory.items():
  if value["stock"] < lowest_item:
    lowest_item = value["stock"]
    lowest_name = name
print(lowest_item)
print(lowest_name)
  

expenses = [
    {"name": "food", "amount": 25},
    {"name": "gas", "amount": 40},
    {"name": "coffee", "amount": 6}
]

highest_amount = expenses[0]["amount"]
lowest_amount = expenses[0]["amount"]
for item in expenses:
  if item["amount"] > highest_amount:
    highest_amount = item["amount"]
    highest_expense_name = item["name"]
  if item ["amount"] < lowest_amount:
    lowest_amount = item["amount"]
    lowest_expense_name = item["name"]
print(highest_expense_name, highest_amount)
print(lowest_expense_name, lowest_amount)
