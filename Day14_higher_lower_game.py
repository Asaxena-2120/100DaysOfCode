#!usr/bin/env python3
'''
Inspired from the game higherlower http://www.higherlowergame.com/
The program checks who has higher Instagram followers
'''
# importing libraries
from Resources.higher_lower_art import logo, vs
from Resources.higher_lower_game_data import data
import os
import random


# To clear screen for next turn
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Creating first option
obj1 = random.choice(data)
print(logo)

# Setting a global variable score as 0
score = 0


# Function compare() takes input as player's answer and both data objects for comparison. Returns True if user guessed correct.
def compare(user_input, ob1, ob2):
    # Check if the player's answer is the one with higher followers
    if ob1['follower_count'] > ob2['follower_count'] and user_input.lower() == 'a':
        return True
    elif ob2['follower_count'] > ob1['follower_count'] and user_input.lower() == 'b':
        return True

    return False


# Funtion play() takes global variable score as input and first data object to start with.
def play(score, obj1):
    # Assigning obj1 to obj1
    obj1 = obj1

    # Random second data object obj2
    obj2 = random.choice(data)

    print(f"Compare A: {obj1['name']}, {obj1['description']}, from {obj1['country']}")
    print(vs)
    print(f"Against B: {obj2['name']}, {obj2['description']}, from {obj2['country']}")

    # Ask player's answer
    user_input = input("Who has more followers? Type 'A' or 'B': ")

    # Call compare() function to compare follower_count of two data objects
    result = compare(user_input, obj1, obj2)

    # If compare gives True i.e; player guessed correctly and can play another round with option2 now acting as option1
    if result:
        score += 1
        clear()
        print(logo)
        print(f"You're right. Current Score: {score}")
        play(score, obj2)

    else:
        clear()
        print(logo)
        print(f"Sorry, that's wrong. Final Score: {score}")


# Calling funtion play()
play(score, obj1)






