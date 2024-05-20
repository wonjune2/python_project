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

total_money = 0


def report():
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${total_money}")


def cost():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = (0.25 * quarters) + (0.1 * dimes) + (0.05 * nickles) + (0.01 * pennies)
    return total


def resource_check(coffee_name):
    coffee = MENU[coffee_name]["ingredients"]
    for key in coffee:
        if resources[key] - coffee[key] < 0:
            print(f"Sorry there is not enough {key}.")
            return False

    for key in coffee:
        resources[key] -= coffee[key]
    return True


off = False
while not off:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")

    if user_input == "report":
        report()
    elif user_input == "off":
        off = True
    else:
        coffee_name = user_input
        coffee_cost = cost()
        remain_dollar = coffee_cost - MENU[user_input]["cost"]
        if remain_dollar >= 0:
            if resource_check(coffee_name):
                print(f"Here is you ${remain_dollar} in change.")
                print(f"Here is your {coffee_name} Enjoy!")
                total_money += MENU[user_input]["cost"]
        else:
            print("Sorry that's not enough. Money refunded.")