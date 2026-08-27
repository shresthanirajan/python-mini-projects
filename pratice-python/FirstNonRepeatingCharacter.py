# def first_unique_char(text):
#   text = text.lower()
#   counts = {}
#   for char in text:
#     if char in counts:
#       counts[char] += 1
#     else:
#       counts[char] = 1

#   for i, char in enumerate(text):
#     if counts[char] == 1:
#       return i
  
#   return None
  

# result = first_unique_char("aabbccd")
# print(result)

for x in (1,2,3):
  for y in (1,2):
    print(x,y)
  