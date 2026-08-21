tasks = [
    {"task": "study python", "done": True},
    {"task": "finish homework", "done": True},
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
def add_task(task):
  tasks.append(task)

#Removes a task
def remove_task(task_number):
   index = task_number -1
   tasks.pop(index)

#Update Task
def update_task(task_number, new_task):
  index = task_number -1
  tasks[index] = new_task

#Search Function
def search_tasks(search_term):
  found = False
  for task in tasks:
    if search_term.lower() in task.lower():
      print(f"{task} is here!")
      found = True
  if not found:
    print("Not here")

def complete_task(task_number):
  pass

show_tasks()

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

print(f"Task completed: {completed}")
print(task_completed)
print(f"Task Not completed: {not_completed}")