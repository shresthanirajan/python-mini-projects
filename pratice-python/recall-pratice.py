#1
text = "banana"
text_dic = {}
for char in text:
  if char in text_dic:
    text_dic[char] += 1
  else:
    text_dic[char] = 1
print(text_dic)