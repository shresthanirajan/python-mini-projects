#TODO pratice

products = [
    {"name": "Laptop", "price": 800},
    {"name": "Mouse", "price": 25},
    {"name": "Keyboard", "price": 70}
]

new_product = []

for product in products:
    product_var = product["price"]

    if product_var < 100:
        new_product.append(product["name"])

print(new_product)


