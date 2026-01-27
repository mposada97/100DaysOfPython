# simplified jack black
# instead of cards we are using the numbers that correspond to the card
# we are using an infinite deck based on the following:

from art import logo
import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10] 

users_cards = []
dealers_cards = []

def add_random_card(list):
    list.append(random.choice(cards))

def play_round():
    if len(users_cards) == 0:
        add_random_card(users_cards)
        add_random_card(users_cards)
        add_random_card(dealers_cards)
    else:
        add_random_card(users_cards)

def play_game():
    print(logo)
    start = input("Do you want to play a game of Black Jack? Type 'y' or 'n': ").lower()
    if start != 'y':
        exit
    else:
        while True:
            play_round()
            print(users_cards)
            print(dealers_cards)
            cont = input("Do you want another card? Type 'y' or 'n': ").lower()
            if cont != 'y':
                break
            else:
                continue

if __name__ == "__main__":
     play_game()
        
