import string
import random
letters = list(string.ascii_letters)
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['@','!','#','$','%','&','*']

print("Welcome to the password generator!\n")
number_letters = int(input(
  "How many letters do you want in your password?\n"  
))
number_numbers = int(input(
  "How many numbers do you want in your password?\n"
))
number_symbols = int(input(
  "How many symbols do you want in your password?\n"
))

password_list = []

for char in range(1, number_letters+1): 
  password_list.append(random.choice(letters))
for char in range(1, number_numbers+1):
  password_list.append(random.choice(numbers))
for char in range(1, number_symbols+1):
  password_list.append(random.choice(symbols))

random.shuffle(password_list)

password = ""

for char in password_list:
  password += char
  ##password = password + char

print(f"Your password is: {password}")