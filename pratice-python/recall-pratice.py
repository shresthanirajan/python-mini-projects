contacts = {
    "alex": "817-555-1111",
    "maya": "682-555-2222"
}

inventory = {
    "apple": {"price": 1.50, "stock": 10},
    "banana": {"price": 0.75, "stock": 4},
    "orange": {"price": 1.25, "stock": 8}
}

def find_contact(name):
  if name in contacts:
    return contacts[name]
  else:
    return None

def delete_contact(name):
  if name in contacts:
    contacts.pop(name)
    print(f"{name} sucessfully removed!")
  else:
    print("No user Found")

def search_contacts(search_term):
    for name in contacts:
      if name in search_term:
        print("Found")
        return
    else:
      print("Not found")
       


contacts["sam"] = "469-555-3333"
contacts["alex"] = "817-556-1231"

for name, number in contacts.items():
  print(name, number)


lowest_stock = inventory["apple"]["stock"]
for name, number in inventory.items():
  if number["stock"] < lowest_stock:
    lowest_stock = number["stock"]
  
   
print(lowest_stock)


numbers = [4, 8, 2, 10, 7, 15]
is_duplicate = False
if len(numbers) != len(set(numbers)):
  is_duplicate = True
print(is_duplicate)

