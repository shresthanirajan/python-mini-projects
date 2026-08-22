seen = set()
duplicates = set()

numbers = [3, 7, 3, 9, 7, 12, 3]

for nums in numbers:
  if nums in seen:
    duplicates.add(nums)
  else:
    seen.add(nums)




words = ["cat", "dog", "cat", "bird", "dog", "fish", "cat"]

seen = set()
duplicates = set()

for word in words:
  if word in seen:
    duplicates.add(word)
  else:
    seen.add(word)


contacts = {
    "alex": "111",
    "maya": "222"
}


contacts["sam"] = "333"
contacts["alex"] = 999

print(contacts)

# Items gives the Key and Value
# Values Gives the value itself
# keys Gives the key itself




tasks = [
    {"task": "study python", "done": False},
    {"task": "finish homework", "done": False},
    {"task": "go to gym", "done": True}
]

def complete_task(task_number):
  index = task_number - 1
  tasks[index]["done"] = True


not_completed = 0
task_done = ""
for task in tasks:
  if task["done"] == False:
    not_completed += 1
    task_done = (task["task"])
    

complete_task(2)


inventory = {
    "apple": {"price": 1.50, "stock": 10},
    "banana": {"price": 0.75, "stock": 4},
    "orange": {"price": 1.25, "stock": 8}
}


lowest_name = 0
lowest_stock = inventory["apple"]["stock"]

for name, stock in inventory.items():
  if stock["stock"] < lowest_stock:
    lowest_stock = stock["stock"]
    lowest_name = name
print(lowest_stock)
print(lowest_name)
  
