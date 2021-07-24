from menu import menu
from menu import resources


def report() :
    for resource in resources :
        print(f"{resource} : {resources[resource]}")

def money() :
    no_of_pennies = float(input("Enter Pennies :"))
    no_of_nickels = float(input("Enter Nickels :"))
    no_of_dimes = float(input("Enter Dimes :"))
    no_of_quarters = float(input("Enter Quarters :"))

    money_entered = (no_of_pennies*pennies) + (no_of_nickels*nickels) + (no_of_dimes*dimes) + (no_of_quarters*quarters)

    return money_entered


def espresso(money_entered , change) :
    if resources["water"] < menu["espresso"]["ingredients"]["water"] :
        print("Sorry! Out of water")
        print(f"Money refunded : {money_entered}")
    elif resources["coffee"] < menu["espresso"]["ingredients"]["coffee"] :
        print("Sorry! Out of coffee")
        print(f"Money refunded : {money_entered}")
    else :
        if menu["espresso"]["cost"] > money_entered :
            print(f"Money entered not enough, {money_entered} refunded")
        else :
            change = money_entered - menu["espresso"]["cost"]
            print(f"Here is your change : {change}")
            resources["water"] -= menu["espresso"]["ingredients"]["water"]
            resources["coffee"] -= menu["espresso"]["ingredients"]["coffee"]
            resources["money"] += menu["espresso"]["cost"]
            print("Here is you espresso ! ☕")


def latte(money_entered , change) :
        if resources["water"] < menu["latte"]["ingredients"]["water"]:
            print("Sorry! Out of water")
            print(f"Money refunded : {money_entered}")
        elif resources["coffee"] < menu["latte"]["ingredients"]["coffee"]:
            print("Sorry! Out of coffee")
            print(f"Money refunded : {money_entered}")
        elif resources["milk"] < menu["latte"]["ingredients"]["milk"]:
            print("Sorry! Out of milk")
            print(f"Money refunded : {money_entered}")
        else:
            if menu["latte"]["cost"] > money_entered:
                print(f"Money entered not enough, {money_entered} refunded")
            else:
                change = money_entered - menu["latte"]["cost"]
                print(f"Here is your change : {change}")
                resources["water"] -= menu["latte"]["ingredients"]["water"]
                resources["coffee"] -= menu["latte"]["ingredients"]["coffee"]
                resources["milk"] -= menu["latte"]["ingredients"]["milk"]
                resources["money"] += menu["latte"]["cost"]
                print("Here is you latte ! ☕")


def cappuccino(money_entered, change):
    if resources["water"] < menu["cappuccino"]["ingredients"]["water"]:
        print("Sorry! Out of water")
        print(f"Money refunded : ${money_entered}")
    elif resources["coffee"] < menu["cappuccino"]["ingredients"]["coffee"]:
        print("Sorry! Out of coffee")
        print(f"Money refunded : ${money_entered}")
    elif resources["milk"] < menu["cappuccino"]["ingredients"]["milk"]:
        print("Sorry! Out of milk")
        print(f"Money refunded : ${money_entered}")
    else:
        if menu["cappuccino"]["cost"] > money_entered:
            print(f"Money entered not enough, {money_entered} refunded")
        else:
            change = money_entered - menu["cappuccino"]["cost"]
            print(f"Here is your change : ${change}")
            resources["water"] -= menu["cappuccino"]["ingredients"]["water"]
            resources["coffee"] -= menu["cappuccino"]["ingredients"]["coffee"]
            resources["milk"] -= menu["cappuccino"]["ingredients"]["milk"]
            resources["money"] += menu["cappuccino"]["cost"]
            print("Here is you cappuccino ! ☕")


print("Welcome to the coffee machine\n")
machine_on = True

pennies = 0.01
nickels = 0.05
dimes = 0.10
quarters = 0.25

while machine_on :

    print("Enter the coins")

    coffee = input("What would you like? (espresso/latte/cappuccino)")

    change = 0

    if coffee == "report" :
        report()
    elif coffee == "espresso" :
        money_entered = money()
        espresso(money_entered, change)
    elif coffee == "latte" :
        money_entered = money()
        latte(money_entered, change)
    elif coffee == "cappuccino" :
        money_entered = money()
        cappuccino(money_entered, change)
    else :
        print("Not available !!!")

if resources["water"] == 0 or resources["coffee"] == 0 or resources["milk"] == 0 :
    machine_on = False
else :
    machine_on = False

