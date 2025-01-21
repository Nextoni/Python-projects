from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
cash_machine = MoneyMachine()
drinks = Menu()

choice = input(f"What would you order? {drinks.get_items()}")

while choice != "stop":
    if choice == "report":
        coffee_machine.report()
        cash_machine.report()
    else:
        drink = drinks.find_drink(choice)
        if coffee_machine.is_resource_sufficient(drink):
            if cash_machine.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)

    choice = input(f"What would you order? {drinks.get_items()}")