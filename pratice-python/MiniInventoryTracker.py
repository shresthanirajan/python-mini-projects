#Current inventory
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
#Sell Function
def sell_product(product_name, amount):
    if product_name in inventory:
        if amount > 0:
            if inventory[product_name]["stock"] >= amount:
                inventory[product_name]["stock"] -= amount
                print(f"SOLD: {amount} Amount of {product_name}")
            else:
                print("Not enough stock.")
        else:
            print("Please enter valid amount number.")
    else:
        print("Product doesn't exists")

#Total Inventory Value Function
def total_inventory_value():
    total = 0
    for value in inventory.values():
        total += value["price"] * value["stock"]
    return total

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

lowest_stock = inventory["apple"]["stock"]
lowest_stock_name = "apple"
for name, stock in inventory.items():
    print(stock["stock"])
    if stock["stock"] < lowest_stock:
        lowest_stock = stock["stock"]
        lowest_stock_name = name

print(f"{lowest_stock_name} has the lowest stock with: {lowest_stock}")
