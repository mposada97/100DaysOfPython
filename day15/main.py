from data import data


def report(water, milk, coffee, money):
    print(f'Water : {water}ml \Milk : {milk}ml \Coffee : {coffee}g \nWMoney ${money} \n')
    return
def entry_point():
    order = print('What would you like? (espresso/latte/cappuccino): ').lower()
    return order
def payment(order):
    amount = data[order]['cost']


def main():
    #initialize the variables, this will be the intial state of the coffee machine
    water = 300
    milk = 200
    coffee = 100
    while True:
        entry_point()

if __name__ == "__main__":
     main(data)