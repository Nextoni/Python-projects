def coffee_machine():
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
        "profit" : 0,
    }

    def report():
        print(f"Water: {resources["water"]}")
        print(f"Milk: {resources["milk"]}")
        print(f"Coffee: {resources["coffee"]}")
        print(f"Profit: {resources["profit"]}")


    def coffee(blend):
        coffee_blend = MENU[blend]
        for item in coffee_blend["ingredients"]:
            if resources[item] < coffee_blend["ingredients"][item]:
                return print(f"Sorry there is not enough {item}.")

        print("Please insert coins.\n")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))
        total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01

        if total >= coffee_blend["cost"]:
            total -= coffee_blend["cost"]
            total = round(total, 2)
            resources["profit"] += coffee_blend["cost"]

            for item in coffee_blend["ingredients"]:
                resources[item] -= coffee_blend["ingredients"][item]

            print(f"Your change is ${total}.\nHere is your {blend}.")
        else:
            print("Not enough money were inserted.")

    is_on = True

    while is_on:

        choice = input("What would you like? (espresso/latte/cappuccino): ")

        if choice == "stop":
            is_on = False
        elif choice == "report":
            report()
        else:
            coffee(choice)

coffee_machine()
