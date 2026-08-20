contacts = {
    "alex": "817-555-1111",
    "maya": "682-555-2222"
}

def find_contact(name):
    if name.lower() in contacts:
        return contacts[name.lower()]
    else:
        return None

def delete_contact(name):
    if name in contacts:
        contacts.pop(name)
    else:
        print("Contact Not Found")

def search_contacts(search_term):
    for name in contacts:
        if search_term in name:
            print(f"{name} Found")
    else:
        print("Not Found")

contacts["sam"] = "469-555-3333"
contacts["alex"] = "817-556-1125"
for name, number in contacts.items():
    print(name, number)

phone_number = find_contact("alexander")
print(phone_number)


search_contacts("alexa")


