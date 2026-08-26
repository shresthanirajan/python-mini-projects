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