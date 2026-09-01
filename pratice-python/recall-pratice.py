#1
text = "mississippi"
text_dictinoary = {}
for char in text:
  if char in text_dictinoary:
    text_dictinoary[char] += 1
  else:
    text_dictinoary[char] = 1
print(text_dictinoary)

#2
text = "aabbcdd"
text_dictinoary = {}
for char in text:
  if char in text_dictinoary:
    text_dictinoary[char] += 1
  else:
    text_dictinoary[char] = 1


for char, value in text_dictinoary.items():
  if value <= 1:
    print(char)
    break

3
text = "aabccd"
text_dictinoary = {}
for char in text:
  if char in text_dictinoary:
    text_dictinoary[char] += 1
  else:
    text_dictinoary[char] = 1
print(text_dictinoary)

for index, char in enumerate(text_dictinoary):
  if text_dictinoary[char] <= 1:
    print(index)
    break

4
text = "racecar"
left = 0
right = len(text) - 1
print(right)
is_palindrome = True

while left < right:
  if text[left] == text[right]:
    left += 1
    right -= 1
  else:
    is_palindrome = False
    break


print(is_palindrome)

#5
tasks = [
    {"task": "study", "done": False},
    {"task": "gym", "done": True}
]

print(tasks[1]["task"])
tasks[1]["done"] = False
print(tasks)

#6
def check_score(score):
  if score < 0:
    return "Invalid"
  if score > 100:
    return "Invalid"
  return "Valid"

check = check_score(101)
print(check)

#7 6 is the complement

#8 that seen is a dictionary and holds the value and the index, seen[8] means the number returns the index


  

  
  
  
  
