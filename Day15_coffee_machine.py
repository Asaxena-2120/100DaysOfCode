#!usr/bin/env python3

"""

The program represents a software for coffee machine.
The requirements for coffee machine code can be found in Resources directory: requirements_coffee_machine_code

"""
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0.0


def check_money(choice, money_entered):
    # This function checks if money given by user is enough to
    # purchase the selected drink.
    money_needed_for_choice = MENU[choice]["cost"]
    if money_needed_for_choice <= money_entered:

        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def check_resources(choice):
    # This function checks if money given by user is enough to
    # purchase the selected drink.

    # As espresso does not need milk, so setting it 0
    if choice == 'espresso':
        milk_needed=0
    else:
        milk_needed = MENU[choice]["ingredients"]['milk']

    # Getting information for the ingredients needed by the selected drink
    water_needed = MENU[choice]["ingredients"]['water']
    coffee_needed = MENU[choice]["ingredients"]['coffee']

    # Checking the resources available in the coffee machine
    water_available = resources["water"]
    milk_available = resources["milk"]
    coffee_available = resources["coffee"]

    # Check if coffee machine has enough ingredients to make the drink.
    # If yes, returning True. If no, printing a sorry message and retuning False
    if water_needed > water_available:
        print("Sorry there is not enough water")
        return False
    if milk_needed > milk_available:
        print("Sorry there is not enough milk")
        return False
    if coffee_needed > coffee_available:
        print("Sorry there is not enough coffee")
        return False

    return True


# This function helps in building the report, by updating resources after each drink is made.
def resources_left(choice):
    water_needed = MENU[choice]["ingredients"]['water']
    if choice == 'espresso':
        milk_needed = 0
    else:
        milk_needed = MENU[choice]["ingredients"]['milk']
    coffee_needed = MENU[choice]["ingredients"]['coffee']

    resources['water'] -= water_needed
    resources['milk'] -= milk_needed
    resources['coffee'] -= coffee_needed
    #print(f"resources left: {resources}")

print("""Welcome to coffee machine code!!!\nIf you would like to check status of ingredients type 'report' or type 'off to turn off the machine else go ahead and order your favourite drink.""" )
start = True
while start:
    # When the user enters “report” to the prompt,
    # a report should be generated that shows the current resource values

    print()
    user_choice = input("What would you like? (espresso/latte/cappuccino/report/off)")
    if user_choice == 'report':
        print(f"Water: {resources['water']}ml ")
        print(f"Milk: {resources['milk']}ml ")
        print(f"Coffee: {resources['coffee']}g ")
        print(f"Money: ${money} ")
    # Turn off the Coffee Machine by entering “off” to the prompt.
    elif user_choice == 'off':
        print("Turning off")
        start = False
    else:

        #  When the user chooses a drink, the program should check if there are enough
        #  resources to make that drink.
        if not check_resources(user_choice):
            start = False
            continue
        print("Please insert coins.")
        quarters = int(input("How many quarters? "))
        dimes = int(input("How many dimes? "))
        nickels = int(input("How many nickels? "))
        pennies = int(input("How many pennies? "))
        user_money = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)

        # Check if money is sufficient
        money_sufficient = check_money(user_choice, user_money)
        if money_sufficient:
            money_needed = MENU[user_choice]["cost"]
            money_returned = user_money - money_needed

            print("Here is {:0.2f} in change.".format(money_returned))
            money += money_needed
            if user_choice == 'espresso':
                print(f"Here is your {user_choice} ☕️. Enjoy!")

            if user_choice == 'latte':
                print(f"Here is your {user_choice} ☕️. Enjoy!")

            if user_choice == 'cappuccino':
                print(f"Here is your {user_choice} ☕️. Enjoy!")
        # If the transaction is successful and there are enough resources to make the drink the
        # user selected, then the ingredients to make the drink should be deducted from the
        # coffee machine resources.
        resources_left(user_choice)

