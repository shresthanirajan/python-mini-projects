from ctypes import c_char

user_word = input("What is your word: ").lower().replace(" ","")

user_dic = {}
value = 1
for char in user_word:
    if char in user_dic:
       user_dic[char] +=1
    else:
        user_dic[char] = value

print(user_dic)
#Most frequent character.
most_char = ""
highest_count = 0
for char, count in user_dic.items():
    if count > highest_count:
        highest_count = count
        most_char = char


print(f"Most frequent character: {most_char}")
print(f"Count: {highest_count}")

#Least frequent Character
least_char = ""
lowest_count = next(iter(user_dic.values()))
for char, count in user_dic.items():
    if lowest_count is None or count < lowest_count:
        lowest_count = count
        least_char = char
print(f"Lowest: {lowest_count}")

#characters that appear more than once.
for char, count in user_dic.items():
    if count > 1:
        print(f"{char}: {count}")



#unique characters
unique_characters = len(user_dic)
print(unique_characters)