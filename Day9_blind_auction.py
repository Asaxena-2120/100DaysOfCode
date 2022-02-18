import os

# To clear screen cross-platform i.e 'clear' for Linux and 'cls' for Windows
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
from Resources.blind_auction_art import logo

print("Welcome to the blind auction.")
print(logo)
play = True
bidders = {}


# Finding the highest bidder
# If two bids are equal then the bidder who bids first wins!
def highest_bidder():
    maximum_bid = -1
    winner = ''
    for bidder in bidders:
        if bidders[bidder] >= maximum_bid:
            maximum_bid = bidders[bidder]
            winner = bidder

    print(f"The winner is {winner} with a bid of ${maximum_bid}")


# Taking inputs and putting them into a dictionary
while play == True:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bidders[name] = bid
    more_bidders = input("Are there any other bidders?\n")
    if more_bidders == 'no':
        play = False
    #clear screen after each bid
    cls()

highest_bidder()
