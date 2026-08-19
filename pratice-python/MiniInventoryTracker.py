#Current Inverntory
inventory = {
    "apple": {"price": 1.50, "stock": 10},
    "banana": {"price": 0.75, "stock": 20},
    "orange": {"price": 1.25, "stock": 8}
}

#Find Product
def find_product(product_name):
    if product_name in inventory:
        return inventory[product_name]
    else:
        return None
#Update Function
def update_stock(product_name, amount):
    if product_name in inventory:
        if amount > 0:
            inventory[product_name]["stock"] += amount

        else:
            print("Please enter a valid amount number.")
    else:
        print("Product doesn't exists")

def sell_product(product_name, amount):
    if product_name in inventory:
        if amount > 0:
            if inventory[product_name]["stock"] >= amount:
                inventory[product_name]["stock"] -= amount
                print("DONE")
            else:
                print("Please enter valid Amount to sell.")
        else:
            print("Please enter valid amount number.")
    else:
        print("Product doesn't exists")


#Prints inventory Values
for product, info in inventory.items():
    print(f"{product} - Price: {info['price']} - Stock: {info['stock']}")

#Finding Products
product_name = input("Enter product name: ").lower()
product = find_product(product_name)
if product == "Product not found":
    print("Product Not here")
else:
    print(f"Price: {product['price']}\nStock: {product['stock']}")


sell_product("apple", 100)
print(inventory["apple"])
