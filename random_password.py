#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

###Option 1###

# password = ""

# for char in range(0, nr_letters):
#     password += random.choice(letters)

# for char in range(0, nr_symbols):
#     password += random.choice(symbols)

# for char in range(0, nr_numbers):
#     password += random.choice(numbers)

# print(f"Your password is: {password}")

##Option 2###
#Random letters

#Declare empty string
ran_pass_letters = ""

for char in range(0, nr_letters):  #For every index within the input range
    random_letters = random.choice(
        letters)  #Grab a random letter from letter[]
    ran_pass_letters += random_letters  #Adds a letter until count requirement met

#Random symbols
ran_pass_symbols = ""

for char in range(0, nr_symbols):
    random_symbols = random.choice(symbols)
    ran_pass_symbols += random_symbols

#Random numbers
ran_pass_numbers = ""

for char in range(0, nr_numbers):
    random_numbers = random.choice(numbers)
    ran_pass_numbers += random_numbers

print("Here is your password: " + ran_pass_letters + ran_pass_symbols +
      ran_pass_numbers)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

###Option 1###
password_list = []

for char in range(0, nr_letters):
    password_list += random.choice(letters)

for char in range(0, nr_symbols):
    password_list += random.choice(symbols)

for char in range(0, nr_numbers):
    password_list += random.choice(numbers)

random.shuffle(password_list)

super_ran_password = ""

for char in password_list:
    super_ran_password += char

print(f"Your super password is: {super_ran_password}")
