numbers_input = input("Enter numbers: ").split()

numbers_list = []
for num in numbers_input:
    numbers_list.append(int(num))

max_number = 0
for num in numbers_list:
    if num > max_number:
        max_number = num
print(max_number)

min_number = numbers_list[0]
for num in numbers_list:
    if num < min_number:
        min_number = num
print(min_number)

even = 0
odd = 0
for num in numbers_list:
    if num % 2 ==0:
        even += 1
    else:
        odd += 1
print(even)
print(odd)

is_duplicates = False


print(is_duplicates)