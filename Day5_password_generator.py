#!usr/bin/env python3
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

import random
result = ''
letters_length = len(letters)
numbers_length = len(numbers)
symbols_length = len(symbols)

# Selecing a letter from all the letters
for i in range(nr_letters):
  letter_index = random.randint(0, letters_length-1)
  result += letters[letter_index]

# Selecing a symbol from all the symbols
for i in range(nr_symbols):
  symbol_index = random.randint(0, symbols_length-1)
  result += symbols[symbol_index]

# Selecing a number from all the numbers
for i in range(nr_numbers):
  number_index = random.randint(0, numbers_length-1)
  result += numbers[number_index]


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
result2=''
new_string = list(result)

for i in range(len(new_string)):
    #select an index randomly
    j = random.randint(0, len(new_string)-1)
    #delete the element at that index.
    element=new_string.pop(j)
    #now append that deleted element to the list
    result2+=(element)
print("Your password is ",result2)