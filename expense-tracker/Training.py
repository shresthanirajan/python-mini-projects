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


students = [
    {"name": "Jack", "score": 80},
    {"name": "Sarah", "score": 95},
    {"name": "Mike", "score": 70}
]

def get_top_score(student_list):
    top_student = student_list[0]

    for student in student_list:
        if student["score"] > top_student["score"]:
            top_student = student

    return top_student

print(get_top_score(students))