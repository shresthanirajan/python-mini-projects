# contacts = {
#     "alexander": "817-555-1111",
#     "maya": "682-555-2222"
# }

# inventory = {
#     "apple": {"price": 1.50, "stock": 10},
#     "banana": {"price": 0.75, "stock": 4},
#     "orange": {"price": 1.25, "stock": 8}
# }

# def find_contact(name):
#   if name.lower() in contacts:
#     return contacts[name.lower()]
#   else:
#     return None

# def delete_contact(name):
#   if name in contacts:
#     contacts.pop(name)
#     print(f"{name} sucessfully removed!")
#   else:
#     print("No user Found")

# def search_contacts(search_term):
#     for name in contacts:
#       if search_term in name:
#         print("Found")
#         return
#     else:
#       print("Not found")
       


# contacts["sam"] = "469-555-3333"
# contacts["alex"] = "817-556-1231"

# for name, number in contacts.items():
#   print(name, number)


# lowest_stock = inventory["apple"]["stock"]
# product_name = ""
# for name, number in inventory.items():
#   if number["stock"] < lowest_stock:
#     lowest_stock = number["stock"]
#     product_name = name
   
# print(product_name,lowest_stock)

# seen = []

# numbers = [4, 8, 2, 10, 7, 15, 4, 8]
# for x in numbers:
#     if x in seen:
#         print(x)
#     else:
#         seen.append(x)


# search_contacts("alex")




# words = ["cat", "dog", "bird", "cat", "dog"]

# seen = set()
# duplicates = set()

# for word in words:
#   if word in seen:
#     duplicates.add(word)
#   else:
#     seen.add(word)

# print(duplicates)


seen = set()
duplicate = set()
numbers = [2, 5, 7, 2, 9, 5]
for nums in numbers:
  if nums in seen:
    duplicate.add(nums)
  else:
    seen.add(nums)

print(seen)
print(duplicate)


seen = set()
duplicate = set()
letters = "banana"

for char in letters:
  if char in seen:
    duplicate.add(char)
  else:
    seen.add(char)

print(seen)
print(duplicate)