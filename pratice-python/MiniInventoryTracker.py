inventory = {
    "apple": {"price": 1.50, "stock": 10},
    "banana": {"price": 0.75, "stock": 20},
    "orange": {"price": 1.25, "stock": 8}
}

def find_product(product_name):
    if product_name in inventory:
        return inventory[product_name]
    else:
        return None

def update_stock(product_name, amount):
    if product_name in inventory:
        if amount > 0:
            inventory[product_name]["stock"] += amount

        else:
            print("Please enter a valid amount number.")
    else:
        print("Product doesn't exists")
for product, info in inventory.items():
    print(f"{product} - Price: {info['price']} - Stock: {info['stock']}")

product_name = input("Enter product name: ").lower()
product = find_product(product_name)
if product == "Product not found":
    print("Product Not here")
else:
    print(f"Price: {product['price']}\nStock: {product['stock']}")


update_stock("apple", 10)
print(inventory["apple"])
