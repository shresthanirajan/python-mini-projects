def analyze_password(password):
  digit = 0
  uppercase = 0
  lowercase = 0
  special_character = 0
 
  missing = []
  for char in password:
    

    if char.isdigit():
      digit += 1
    if char.isupper():
      uppercase += 1
    if char.islower():
      lowercase += 1
    if not char.isalnum():
      special_character +=1

  if uppercase <1:
        missing.append("Need more UpperCase")
  if len(password) < 8:
        missing.append("Not enough characters")
  if digit < 1:
        missing.append("Not enough digits")
  if lowercase < 1:
        missing.append("Not enough lowercase")
  if special_character < 1:
        missing.append("Not enough special character")  
  if not missing:
       password_decider = "Strong"
  else:
        password_decider = "Weak"
  
  
  return digit, uppercase, lowercase, special_character, password_decider, missing
    
    
digit, uppercase, lowercase, special_character, password_decider, missing = analyze_password("aawAAAd1231ad12.com@aaaaaaaaabcd11")

print(f"uppercase: {uppercase}")
print(f"Digits: {digit}")
print(f"Lowercase: {lowercase}")
print(f"Special Characters: {special_character}")
print(password_decider)
print(missing)
