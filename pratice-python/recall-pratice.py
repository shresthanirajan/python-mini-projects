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


search_tasks("gym")