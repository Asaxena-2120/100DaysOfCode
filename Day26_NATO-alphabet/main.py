import pandas

alpha = pandas.read_csv('nato_phonetic_alphabet.csv')
name = input("Enter a word: ")
name_list = list(name)
result = [row.code for letter in name_list for index,row in alpha.iterrows() if letter.lower() == row.letter.lower()]
print(result)
