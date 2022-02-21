#!usr/bin/env python3
############### Blackjack Project #####################


############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

# Flowchart for the game:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt


import random
from Resources.blackjack_art import logo
import os

# To clear screen cross-platform i.e 'clear' for Linux and 'cls' for Windows
def cls():
    os.system('cls' if os.name=='nt' else 'clear')


start = True


# Create a deal_card() function that uses the List below to *return* a random card.11 is the Ace.
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


# Create a function called calculate_score() that takes a List of cards as input and returns the score.

def calculate_score(cards_list):
    # Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    if len(cards_list) == 2 and 11 in cards_list and 10 in cards_list:
        return 0
    # Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
    if sum(cards_list) > 21 and 11 in cards_list:
        cards_list.remove(11)
        cards_list.append(1)
    score = sum(cards_list)

    return score


# Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose."
    if user_score == computer_score:
        return "Draw."
    elif computer_score == 0:
        return "Lose, opponent has Blackjack."
    elif user_score == 0:
        return "Win with a Blackjack."
    elif user_score > 21:
        return "You went over. You lose."
    elif computer_score > 21:
        return "Opponent went over. You win."
    elif user_score > computer_score:
        return "You win."
    else:
        return "You lose."


while start:
    print(logo)
    game_end = False
    # Deal the user and computer 2 cards each using deal_card() and append().
    user_cards = []
    computer_cards = []
    for _ in range(0, 2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    while game_end == False:
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        if computer_score == 0 or user_score == 0 or user_score > 21:
            game_end = True
            continue


        # If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
        else:
            print()
            draw_card = (input("Type 'y' to get another card, type 'n' to pass: "))
            if draw_card == 'y':
                next_card = deal_card()
                user_cards.append(next_card)

                # The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
                user_score += next_card

            else:
                game_end = True

    # Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
    while computer_score != 0 and computer_score < 17:
        next_computer_card = deal_card()
        computer_cards.append(next_computer_card)
        computer_score += next_computer_card

    print()
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

    print(compare(user_score, computer_score))

    # Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack.
    print()
    new_game = input("Do you want to start new game? Type 'y' to start and 'n' to end the game. \n")
    if new_game == 'n':

        start = False

    else:
        cls()



