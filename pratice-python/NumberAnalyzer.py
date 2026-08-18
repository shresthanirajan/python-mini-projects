user_number = (input("What is your number: ").split())
print(user_number)

#Looping Though Numbers and Converting to int()
numbers = []
for num in user_number:
    numbers.append(int(num))
print(numbers)

#Largest Number
largest = numbers[0]
for nums in numbers:
    if nums > largest:
        largest = nums
print(f"largest: {largest}")

#Smallest Number
smallest = numbers[0]
for nums in numbers:
    if nums < smallest:
        smallest = nums
print(f"smallest: {smallest}")


#Total Value and Average Value
numbers_amount = len(numbers)
total = 0
for nums in numbers:
    total += nums
average = total/numbers_amount
print(f"Total: {total}")
print(f"Average: {round(average,2)}")

even = 0
odd = 0


#Even and ODDS
for nums in numbers:
    if nums % 2 == 0:
        even += 1
    else:
        odd += 1

print(f"Even: {even}")
print(f"Odd: {odd}")

#Check Duplicates
duplicates = False

if len(set(numbers)) != len(numbers):
    duplicates = True

print(f"duplicates: {duplicates}")

#Finding The duplicated numbers
seen = set()
duplicates_found = set()

for nums in numbers:
    if nums not in seen:
        seen.add(nums)
    else:
        duplicates_found.add(nums)

if duplicates_found:
    print(f"Duplicates found: {duplicates_found}")
else:
    print("No duplicates found")
