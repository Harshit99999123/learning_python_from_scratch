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

COIN_CONVERSION_RATE = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01
}

INITIAL_RESOURCES = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

current_resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def process_coins(quarters, dimes, nickles, pennies):
    return (COIN_CONVERSION_RATE.get("quarters") * quarters + COIN_CONVERSION_RATE.get("dimes") * dimes
            + COIN_CONVERSION_RATE.get("nickles") * nickles + COIN_CONVERSION_RATE.get("pennies") * pennies)


def print_report():
    for item in current_resources:
        print(f"{item.title()}: {current_resources.get(item)}")
    print(f"Money: ${profit}")


def check_each_resource_availability(coffee_choice, resource):
    if MENU.get(coffee_choice).get("ingredients").get(resource) > current_resources.get(resource):
        return False
    return True


def check_sufficient_resources(coffee_choice):
    for resources_required in MENU.get(coffee_choice).get("ingredients"):
        is_sufficient_resource = check_each_resource_availability(coffee_choice, resources_required)
        if not is_sufficient_resource:
            print(f"Sorry there is not enough {resources_required}")
            return False

    return True


profit = 0


def process_money_transaction(coffee_choice):
    global profit
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    amount_in_dollars_entered = process_coins(quarters, dimes, nickles, pennies)
    coffee_cost = MENU.get(coffee_choice).get("cost")
    if coffee_cost > amount_in_dollars_entered:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif coffee_cost < amount_in_dollars_entered:
        print(f"Here is ${round(amount_in_dollars_entered - coffee_cost, 2)} in change")
        profit += coffee_cost
        profit = round(profit, 2)
        return True
    profit += coffee_cost
    profit = round(profit, 2)
    return True


def prepare_coffee(coffee_choice):
    for resource in MENU.get(coffee_choice).get("ingredients"):
        current_resources[resource] = current_resources.get(resource) - MENU.get(coffee_choice).get("ingredients").get(
            resource)
    print(f"Here is your {coffee_choice}")


def order_coffee():
    action = input("What would you like? (espresso/latte/cappuccino): ")
    if action == "off":
        return "off"
    elif action == "report":
        print_report()
        return "on"
    else:
        if check_sufficient_resources(action):
            print("Please insert coins")
            if process_money_transaction(action):
                prepare_coffee(action)
        return "on"


def refill_machine():
    for resource in current_resources:
        current_resources[resource] = INITIAL_RESOURCES[resource]


start_machine_flag = "on"

while start_machine_flag != "off":
    start_machine_flag = order_coffee()

print("Turning off machine........")
