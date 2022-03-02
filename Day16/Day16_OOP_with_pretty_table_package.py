#!usr/bin/env python3

# Package PrettyTable document: https://code.google.com/archive/p/prettytable/wikis/Tutorial.wiki

# import class PrettyTable from package Prettytable
from prettytable import PrettyTable

# creating an object
table = PrettyTable()

# Making columns
table.add_column('Serial Number',["1","2","3"])
table.add_column('Pokemon Name',["Pikachu","Squirtle","Charmander"])
table.add_column('Type',["Electric","Water","Fire"])

# Aligning data in column in the center
table.align["Serial Number"] = "c"

# Aligning data in column to the left side
table.align["Pokemon Name"] = "l"

# Aligning data in column to the right side
table.align["Type"] = "r"

print(table)
