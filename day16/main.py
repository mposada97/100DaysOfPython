from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main():
    #initialize the variables, this will be the intial state of the coffee machine
    my_menu = Menu()
    items = my_menu.get_items()
    my_machine = CoffeeMaker()
    cashier = MoneyMachine()

    while True:
        order = input(f'What would you like? ({items}): ').strip().lower()
        drink = my_menu.find_drink(order)
        if order == "report":
            my_machine.report()
            cashier.report()
        if drink is None:
            print("Please enter a valid menu item.")
            continue
        if not my_machine.is_resource_sufficient(drink):
            continue
        if cashier.make_payment(drink.cost):
            my_machine.make_coffee(drink)

if __name__ == "__main__":
     main()