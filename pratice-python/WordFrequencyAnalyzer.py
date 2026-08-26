sentence = "Python is fun, and python is powerful!"

def count_words(sentence):
  if not sentence.strip():
      print("Please Enter a Sentence")
      return
  words = sentence.lower().split()
  word_counts = {}
  highest_count = 0
  highest_word = ""
  repeated_words = [] 
  unique_words = []
  
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
      repeated_words.append(word)
    else:
      unique_words.append(word)
  return word_counts, highest_count, highest_word, repeated_words, unique_words

result = count_words(sentence)
if result:
    word_counts, highest_count, highest_word, repeated_words, unique_words = result
    print(f"Highest Word: {highest_word} | Highest count: {highest_count}")
    print(f"Repeated words: {repeated_words}")
    print(f"Unique words: {unique_words}")
