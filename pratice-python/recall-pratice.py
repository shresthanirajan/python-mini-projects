user_input = input("What is your numbers:").split()

number_list = []

for nums in user_input:
    number_list.append(int(nums))

print(number_list)

maximum = number_list[0]
for nums in number_list:
    if nums > maximum:
        maximum = nums
print(maximum)

minium = number_list[0]
for nums in number_list:
    if nums < minium:
        minium = nums
print(minium)

even = 0
odd = 0
for nums in number_list:
    if nums % 2 ==0:
        even += 1
    else:
        odd += 1
print(f"Even: {even}")
print(f"Odd: {odd}")

is_duplicate = False
if len(number_list) != (len(set(number_list))):
    is_duplicate = True
print(f"Duplicate: {is_duplicate}")
highest_count = 0
highest_char = ""
user_dic = {"a": 3, "b": 1, "c": 2}
for char, num in user_dic.items():
    if num > highest_count:
        highest_count =num
        highest_char = char

print(highest_count)
print(highest_char)
