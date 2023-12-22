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

profit=0
RESOURCES = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

def check_resources(coffee):
    for ingredient, amount in MENU[coffee]["ingredients"].items():
        if RESOURCES[ingredient] < amount:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True

def insert_coins():
    print("Please insert coins.")
    quarters=float(input("how many quarters?: "))*0.25
    dimes=float(input("how many dimes?: "))*0.10
    nickles=float(input("how many nickels?: "))*0.05
    pennies=float(input("how many pennies?: "))*0.01
    return quarters+dimes+nickles+pennies

def cost_of_coffee(coffee):
    print(f"Total cost of the coffee: ${MENU[coffee]['cost']}")

def update_resources(coffee):
    global profit
    for ingredient, amount in MENU[coffee]["ingredients"].items():
        RESOURCES[ingredient] -= amount
    profit += MENU[coffee]["cost"]
    

def serve_coffee(coffee, total_amount_given):
    if total_amount_given == MENU[coffee]["cost"]:
        print(f"Here is your {coffee} ☕. Enjoy!")
        update_resources(coffee)
    elif total_amount_given > MENU[coffee]["cost"]:
        change = round(total_amount_given - MENU[coffee]["cost"], 2)
        print(f"Here is ${change} in change.")
        print(f"Here is your {coffee} ☕. Enjoy!")
        update_resources(coffee)
    else:
        print("Sorry, that's not enough money. Money refunded.")

while True:
    user_order = input("  What would you like? (espresso/latte/cappuccino): ").lower()
    if user_order == "off":
        print("The coffee machine is turning off..")
        break
    elif user_order == "report":
        print(f"Water: {RESOURCES['water']}ml\nMilk: {RESOURCES['milk']}ml\nCoffee: {RESOURCES['coffee']}g\nMoney: ${profit}")
    elif user_order in MENU:
        if check_resources(user_order):
            cost_of_coffee(user_order)
            total_amount_given = insert_coins()
            serve_coffee(user_order, total_amount_given)
    else:
        print("Please type in the appropriate word (espresso/latte/cappuccino)")
