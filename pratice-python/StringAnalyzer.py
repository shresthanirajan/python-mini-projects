user_word = input("What is your Word: ")
original_word = user_word
reversed_word = user_word[::-1]
length_of_word =len(user_word)

word_tuple = (original_word, reversed_word, length_of_word)

print(f"First character: {user_word[0]}")
print(f"Last character: {user_word[-1]}")
print(f"First 3 characters: {user_word[:3]}")
print(f"Last 3 characters: {user_word[-3:]}")
print(f"Reversed: {reversed_word}")
print(f"Length: {length_of_word}")
print(word_tuple)

vowels = 0
consonants = 0
for char in user_word:
    if char in 'aeiou':
        vowels += 1
    else:
        consonants += 1

print(f"vowels: {vowels}")
print(f"consonants: {consonants}")

is_palindrome = False
clean_word = user_word.replace(" ", "").lower()
if clean_word[::-1] == clean_word:
    is_palindrome = True

print(f"Palindrome {is_palindrome}")

print("Characters: ")
for char in user_word:
    print(char)