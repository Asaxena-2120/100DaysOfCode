#!usr/bin/env python3

#A classic rock paper scissors game

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
comp_input = random.randint(0,2)
if user_input == 0:
  print(f"Your choice is rock {rock}")
if user_input == 1:
  print(f"Your choice is paper {paper}")
if user_input == 2:
  print(f"Your choice is scissors {scissors}")
if comp_input == 0:
  print(f"Computer's choice is rock {rock}")
if comp_input == 1:
  print(f"Computer's choice is paper {paper}")
if comp_input == 2:
  print(f"Computer's choice is scissors {scissors}")

# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.
if user_input<0 or user_input>2 or comp_input<0 or comp_input>2:
  print("It's an invalid choice")
elif (user_input == 0 and comp_input == 2) or (user_input > comp_input):
  print("You win!")
elif user_input == comp_input:
  print("It's a draw.")
else:
  print("You lose.")