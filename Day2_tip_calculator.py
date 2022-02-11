#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

# Laerning Data Types and String Manipulation

print("Welcome to the tip calculator!")
total_bill =float( input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?") )
people = int(input("How many people to split the bill? "))
each_pay = "{:.2f}".format((total_bill*(1+tip/100))/people)

print(f"Each person should pay ${each_pay}")

'''
Example:
If the bill was $150.00, split between 5 people, with 12% tip.

Each person should pay (150.00 / 5) * 1.12 = 33.6

Format the result to 2 decimal places = 33.60

Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.
'''