# #1
# text = "banana"
# text_dic = {}
# for char in text:
#   if char in text_dic:
#     text_dic[char] += 1
#   else:
#     text_dic[char] = 1
# print(text_dic)

#2
def unique_character():
  text = "aabbcddee"
  text_dic = {}
  for char in text:
    if char in text_dic:
     text_dic[char] += 1
    else:
      text_dic[char] = 1
  for char in text_dic.values():
    if char <= 1:
      return char
  

test = unique_character()
print(test)
print(unique_character)
print(unique_character)


