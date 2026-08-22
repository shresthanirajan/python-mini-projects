tasks = [
    {"task": "study python", "done": True},
    {"task": "finish homework", "done": False},
    {"task": "go to gym", "done": True}
]
#Shows All the Tasks
def show_tasks():

  for i, task in enumerate(tasks):
    if not task["done"]:
      print(i+1,".",task["task"], "-" , "Not Done")
    else:
      print(i+1,".",task["task"], "-" , "Done")
    
#Complete Task
def complete_task(task_number):
  index = task_number - 1
  tasks[index]["done"] = True

#Uncomplete Task
def uncomplete_task(task_number):
  index = task_number -1
  tasks[index]["done"] = False

#Adds Task
def add_task(task_name):
  tasks.append({
    "task": task_name,
    "done": False
  })

#Removes a task
def remove_task(task_number):
   index = task_number -1
   tasks.pop(index)

#Update Task
def update_task(task_number, new_task):
  index = task_number -1
  tasks[index]["task"] = new_task

#Search Function
def search_tasks(search_term):
  found = False
  for task in tasks:
    if search_term.lower() in task["task"].lower():
      print(f"{task} is here!")
      found = True
  if not found:
    print("Not here")

#Show completed Task
def show_completed_tasks():
  for task in tasks:
    if task["done"]:
      print(task["task"])

#Show Incompleted Tasks
def show_incomplete_tasks():
  for task in tasks:
    if not task["done"]:
      print(task["task"])


completed = 0
not_completed = 0
task_completed = ""
task_not_completed = ""

for task in tasks:
  if task["done"]:
    completed += 1
    task_completed += task["task"]
  else:
    not_completed += 1

# print(f"Task completed: {completed}")
# print(task_completed)
# print(f"Task Not completed: {not_completed}")


# show_completed_tasks()

# show_incomplete_tasks()


remove_task(2)
print(tasks)