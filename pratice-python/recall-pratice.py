#1

words = ["cat", "dog", "cat", "bird", "dog", "cat", "dog"]
word_counts = {}
for word in words:
  if word in word_counts:
    word_counts[word] += 1
  else:
    word_counts[word] = 1
print(word_counts)

#2 and 3
highest_count = 0
for word, count in word_counts.items():
  if count > 1:
    print(f"{word} appears more that once")

  if count > highest_count:
    highest_count = count
    highest_word = word

print(highest_word, highest_count)

#4

def check_number(number):
  if number < 0:
    print("No Negative Numbers")
    return
  else:
    print("Valid number")

#5
students = [
    {"name": "Alex", "grades": [80, 90, 70]},
    {"name": "Maya", "grades": [95, 88, 92]}
]
print(students[1]["name"])
print(students[1]["grades"][0]) 
print(students[0]["grades"][2])

#6
numbers = [3, 5, 3, 8, 5, 9, 3]
seen = set()
dubplicates = set()

for num in numbers:
  if num in seen:
    dubplicates.add(num)
  else:
    seen.add(num)

print(dubplicates)
print(len(dubplicates))