import random
print("Welcome to the password generator")
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['1','2','3','4','5','6','7','8','9']
symbols = ['!', '@', '$', '%', '&', '*', '.' ,',' ,'']
no_of_letters = int(input("how many letters would you like in your password?\n"))
no_of_symbols = int(input("how many symbols would you like? \n"))
no_of_numbers = int(input("how many numbers would you like? \n"))

password = ""
for i in range(1, no_of_letters +1):
    random_letter = random.choice(letters)
    password += random_letter
for x in range(1, no_of_symbols+1):
    random_symbol = random.choice(symbols)
    password += random_symbol
for z in range(1, no_of_numbers+1):
    random_number = random.choice(numbers)
    password += random_number
print("your generated password is" + password)
