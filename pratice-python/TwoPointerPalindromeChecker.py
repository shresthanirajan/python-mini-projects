def is_palindrome(text):
  clean_text = text.lower().replace(" ", "")
  left = 0
  right = len(clean_text) -1
  print(left)
  print(right)
  while left < right:
    if clean_text[left] == clean_text[right]:
      left += 1
      right -= 1
    else:
      return False
  return True
is_palindrome("racecar")

text = "abcdefg"

left = 0 #0
right = len(text) -1 #6

while left < right:
  print(text[left], text[right])
  
  left += 1
  right -=1

text = "level"

left = 0
right = len(text)-1
is_palindrome = True
while left < right:
  if text[left] == text[right]:
    print(text[left], text[right], "True")
    
    left += 1
    right -= 1
  else:
    is_palindrome = False 
    break
print(is_palindrome)

