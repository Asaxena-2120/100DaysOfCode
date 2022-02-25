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
    money_needed = MENU[choice]["cost"]
    if money_needed <= money_entered:
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def check_resources(choice):
    # resources needed by user's choice of coffee
    water_needed = MENU[choice]["ingredients"]['water']
    if choice == 'espresso':
        milk_needed=0
    else:
        milk_needed = MENU[choice]["ingredients"]['milk']

    coffee_needed = MENU[choice]["ingredients"]['coffee']


    #print(f"water needed: {water_needed}\nmilk needed: {milk_needed}\ncoffee needed: {coffee_needed}")
    water_available = resources["water"]
    milk_available = resources["milk"]
    coffee_available = resources["coffee"]

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
    print(f"resources left: {resources}")


start = True
while start:
    user_choice = input("What would you like? (espresso/latte/cappuccino)")
    if user_choice == 'report':
        print(f"Water: {resources['water']} ")
        print(f"Milk: {resources['milk']} ")
        print(f"Coffee: {resources['coffee']} ")
        print(f"Money: ${money} ")
    elif user_choice == 'off':
        print("Turning off")
        start = False
    else:
        print("Please insert coins.")
        quarters = int(input("How many quarters? "))
        dimes = int(input("How many dimes? "))
        nickels = int(input("How many nickels? "))
        pennies = int(input("How many pennies? "))
        user_money = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)
        if not check_resources(user_choice):
            start = False
            continue

        money_sufficient = check_money(user_choice, user_money)
        if money_sufficient:

            if user_choice == 'espresso':
                print(f"Here is your {user_choice} ☕️. Enjoy!")

            if user_choice == 'latte':
                print(f"Here is your {user_choice} ☕️. Enjoy!")

            if user_choice == 'cappuccino':
                print(f"Here is your {user_choice} ☕️. Enjoy!")
        resources_left(user_choice)

