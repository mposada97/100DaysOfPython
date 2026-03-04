#coffee machine problem solution
from data import data


def report(water, milk, coffee, money):
    return print(f'Water : {water}ml \nMilk : {milk}ml \nCoffee : {coffee}g \nMoney ${money}')

def get_info(order):
    water = data[order]['water']
    milk = data[order]['milk']
    coffee = data[order]['coffee']
    cost = data[order]['cost']

def entry_point(machine_water, machine_coffee, machine_milk, machine_money):
    order = input('What would you like? (espresso/latte/cappuccino): ').strip().lower()
    if order == 'report':
        report(machine_water, machine_milk, machine_coffee, machine_money)
        return None
    if order not in ['espresso', 'latte', 'cappuccino']:
        print('Invalid input, try again')
        return None
    return order

def get_coin_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def get_payment():
    print('Please insert coins.')
    quarters = get_coin_input('How many quarters? ')
    dimes = get_coin_input('How many dimes? ')
    nickles = get_coin_input('How many nickles? ')
    pennies = get_coin_input('How many pennies? ')
    total = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
    return total

def check_resources(order, machine_coffee, machine_milk, machine_water):
    milk_needed = data[order]['milk']
    coffee_needed = data[order]['coffee']
    water_needed = data[order]['water']
    if milk_needed > machine_milk:
        print('Sorry there is not enough Milk')
        return False
    elif coffee_needed > machine_coffee:
        print('Sorry there is not enough Milk')
        return False
    elif water_needed > machine_water:
        print('Sorry there is not enough Milk')
        return False
    return True

def transaction(order, payment, machine_money, machine_coffee, machine_milk, machine_water):
    cost = data[order]['cost']
    milk_used = data[order]['milk']
    coffee_used = data[order]['coffee']
    water_used = data[order]['water']
    if payment < cost:
        print('Sorry thats not enough money, Money refunded')
    else:
        machine_money += cost
        change = payment - cost
        change = round(change,2)
        machine_coffee -= coffee_used
        machine_milk -= milk_used
        machine_water -= water_used
        if change > 0:
            print(f'Here is ${change} in change.')
        print(f'Here is your {order}. Enjoy!')
    return machine_money, machine_coffee, machine_milk, machine_water


def main():
    #initialize the variables, this will be the intial state of the coffee machine
    water = 300
    milk = 200
    coffee = 100
    money = 0
    while True:
        order = entry_point(water, coffee, milk, money)
        if order is None:
            continue
        if not check_resources(order,coffee, milk, water):
            continue
        payment = get_payment()
        money, coffee, milk, water = transaction(order, payment, money, coffee, milk, water)

if __name__ == "__main__":
     main()