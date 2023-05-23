from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on :
    require = input("What would you like? (espresso/latte/cappuccino): \n")
    if require == "report":
        coffee_maker.report()
        money_machine.report()
    elif require == "off":
        is_on = False
    else:
        drink = menu.find_drink(require)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)