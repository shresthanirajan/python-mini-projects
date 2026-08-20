contacts = {
    "alex": "817-555-1111",
    "maya": "682-555-2222",
    "sam": "469-555-3333"
}
#Finding Contact
def find_contact(name):
    if name.lower() in contacts:
        return contacts[name.lower()]
    else:
        return None

#Adding Contacts
def add_contact(name,phone):
    if name.lower() not in contacts:
        contacts[name.lower()] = phone
        print(f"{name} successfully added to contacts")
    else:
        print("Contact already exists")

#Updating Contact
def update_contact(name, new_phone):
    if name.lower() in contacts:
        contacts[name.lower()] = new_phone
        print("Number Changed")
    else:
        print("Contact not found")

#Deleting Contact
def delete_contact(name):
    if name.lower() in contacts:
        contacts.pop(name.lower())
        print(f"{name} has been deleted.")
    else:
        print("Contact not Found!")

#Shows All Contact
def show_contact():
    print("Contacts")
    for name, number in contacts.items():
        print(f"Name: {name}, Phone Number: {number}")

#Searching Contacts
def search_contacts(search_term):
    found = False
    for name, number in contacts.items():
        if search_term.lower() in name.lower():
            print(f"{name} has been found")
            found = True
    if not found:
        print("Not Found!")


result = find_contact("alex")
add_contact("Ron", 213123131133)

delete_contact("ron")
print(contacts)

search_contacts("sam")
