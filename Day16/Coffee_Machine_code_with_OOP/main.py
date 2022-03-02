from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# making objects for all classes
menu = Menu()

# Making coffee objects
# espresso = MenuItem(name = 'espresso', water = 50, milk = 0, coffee = 18, cost = 1.5)
# latte = MenuItem(name = 'latte', water = 200, milk = 150, coffee = 24, cost = 2.5)
# cappuccino = MenuItem(name = 'espresso', water = 250, milk = 100, coffee = 24, cost = 3.0)

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

start = True
while start:
    # Print Report
    money_machine.report()

    user_input = input("Do you want to turn off the machine? Type 'off' if yes else type 'no': ")
    if user_input == 'off':
        print("Turning off the machine.")
        start = False
        continue
    option = input(f"Please select an option: {menu.get_items()}: ")

    menu_item = menu.find_drink(option)
    if not coffee_maker.is_resource_sufficient(menu_item):
        start = False
    else:
        money_machine.money_received = money_machine.process_coins()
        if not money_machine.make_payment(money_machine.money_received):
            start = False
            continue
        else:
            coffee_maker.make_coffee(menu_item)
            money_machine.profit += money_machine.money_received



