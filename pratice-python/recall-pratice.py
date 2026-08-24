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

contacts = ["sam"] = "333"
contacts["alex"] = 999