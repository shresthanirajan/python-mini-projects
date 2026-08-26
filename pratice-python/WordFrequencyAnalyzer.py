sentence = "Python is fun, and python is powerful!"

def count_words(sentence):
  words = sentence.lower().split()
  word_counts = {}
  highest_count = 0
  highest_word = ""
  
  for word in words:
    word = word.strip(",.!")
    if word in word_counts:
      word_counts[word] +=1
    else:
      word_counts[word] = 1
  for word, count in word_counts.items():
    
    if count > highest_count:
      highest_count = count
      highest_word = word
    if count > 1:
      print(word)
  return word_counts, highest_count, highest_word 
word_counts, highest_count, highest_word  = count_words(sentence)
print(word_counts)
print(f"Highest Word: {highest_word} | Highest count: {highest_count}")
