from menu import MENU
from menu import resources

quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01

money = 0.0

def coffee_machine():
    global money
    # 如果 money 变量在 coffee_machine() 函数的内部，导致每次函数调用时 money 的值都会被重置。
    # 为了解决这个问题，可以将 money 变量移动到函数外部，使其成为全局变量。
    while True:
        require = input("What would you like? (espresso/latte/cappuccino): \n")

        if require == 'off':
            return
        elif require == 'report':
            print(f"{resources},Money = {money}$")
        else:
            choose_coffee = MENU[require]
            if choose_coffee["ingredients"]["water"] < resources["water"] \
                    and choose_coffee["ingredients"]["milk"] < resources["milk"] \
                    and choose_coffee["ingredients"]["coffee"] < resources["coffee"]:
                print("Please insert coins.")
                number_quarters = float(input("how many quarters: \n"))
                number_dimes = float(input("how many dimes: \n"))
                number_nickles = float(input("how many nickles: \n"))
                number_pennies = float(input("how many pennies: \n"))

                money_quarters = number_quarters * quarters
                money_dimes = number_dimes * dimes
                money_nickles = number_nickles * nickles
                money_pennies = number_pennies * pennies
                total_money = money_quarters+money_dimes+money_nickles+money_pennies

                if total_money >= choose_coffee["cost"]:
                    money += choose_coffee["cost"]
                    resources["water"] -= choose_coffee["ingredients"]["water"]
                    resources["milk"] -= choose_coffee["ingredients"]["milk"]
                    resources["coffee"] -= choose_coffee["ingredients"]["coffee"]
                    print(f"Here is ${round(total_money-choose_coffee['cost'],2)} in change.")
                    print(f"Here is your {require}, enjoy!")
                else:
                    print("Sorry that's not enough money. Money refunded.")

            else:
                print(f"Sorry, there is not enough resources")

coffee_machine()