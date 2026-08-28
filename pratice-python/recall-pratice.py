#1
text = "banana"
text_dictinoary = {}
for char in text:
  if char in text_dictinoary:
    text_dictinoary[char] += 1
  else:
    text_dictinoary[char] = 1
print(text_dictinoary)

#2
text = "aabbcddee"
text_dictinoary = {}
for char in text:
  if char in text_dictinoary:
    text_dictinoary[char] += 1
  else:
    text_dictinoary[char] = 1

for char in text:
  if text_dictinoary[char] == 1:
    print(char)
    break

#3
text = "aabbccd"
text_dictinoary = {}
for char in text:
  if char in text_dictinoary:
    text_dictinoary[char] += 1
  else:
    text_dictinoary[char] = 1

for index, char in enumerate(text):
  if text_dictinoary[char] == 1:
    print(index)
    break 

#4
text = "level"

left = 0
right = len(text) -1
is_panedolium = True
while left < right:
  if text[left] == text[right]:
    left += 1
    right -= 1
  else:
     is_panedolium = False
     break
  
    
print(is_panedolium) 


#5 

#Text[left] means the variable text starting from the left index of 0 
#text[right] means the variable text starting all the way at the end of the text variable index
#left += 1 means moving forward in the text 
    

#6
def return_placement():
  for i, char in enumerate(text):
    if counts[char] == 1:
        return i
  else:
      return None

# 7. 
tasks = [
    {"task": "study python", "done": False}
]

tasks.append({
  "task": "go to gym",
  "done": False
})
print(tasks)

#8

def check_age(age):
   if age <= 0:
      print("Invalid age")
      return
   if age > 120:
      print("Invalid age")
      return
   print("Valid Age")

check_age(1)

def isPalindrome(s):
        s = s.lower()
        cleaned = ""
        for char in s:
            if char.isalnum():
                cleaned += char
        print(f"CLEANED HERE: {cleaned}")
        left = 0
        right = len(cleaned) -1
        is_palindorme = True
        while left < right:
            if cleaned[left] == cleaned[right]:
                left += 1
                right -= 1
            
            else:
                is_palindorme = False
                return is_palindorme
        return True

checkl = isPalindrome("level, level")
print(checkl)
