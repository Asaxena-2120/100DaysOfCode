#!usr/bin/env python3
# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from Resources.number_guessing_art import logo
import random
import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

# Making a dictionary to store number of attempts allowed on each difficulty level.
attempts = {
    'easy': 10,
    'hard': 5,
}


# The function make_a_guess() asks user to guess a number for fixed number of attemots allowed and helps user in making another guess.
def make_a_guess(attempts_allowed, comp_guess):
    # Check if user has crossed the limit of attempts allowed
    if attempts_allowed == 0:
        print("You've run out of guesses, you lose.")
        return True

    print(f"You have {attempts_allowed} attempts remaining to guess the number.")

    # Ask user for an input
    guess = int(input("Make a guess: "))

    if guess > comp_guess:
        print("Too high.\nGuess again.")
        return False
    elif guess < comp_guess:
        print("Too low.\nGuess again.")
        return False
    # if guess == computer_guess
    else:
        print(f"You got it! The answer was {comp_guess}")
        return True




def guess_number():
    # Printing the logo
    print(logo)
    print("Welcome to number guessing game!")
    print("I'm thinking of a number between 1 to 100.")
    computer_guess = random.randint(1, 100)
    print(f"Pssst, the correct answer is {computer_guess}")
    difficulty_level = input("Choose a difficulty.Type 'easy' or 'hard': ")

    attempts_allowed = attempts[difficulty_level]

    # The loops goes on till the number guess by user is correct or user runs our of guesses.
    found = False
    while found == False:
        found = make_a_guess(attempts_allowed, computer_guess)
        # Each time user is not able to guess correctly number of attempts left are reduced ny 1.
        attempts_allowed -= 1

    # Ask user if they want to play again
    new = input("Do you want to play again? ")
    if new == "yes":
        clear()
        guess_number()
    else:
        return "Game Over!"


print(guess_number())
