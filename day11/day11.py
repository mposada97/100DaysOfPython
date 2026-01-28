# simplified jack black
# instead of cards we are using the numbers that correspond to the card
# we are using an infinite deck based on the following:

from art import logo
import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10] 

def add_random_card(hand):
    hand.append(random.choice(cards))
    return hand

def adjust_ace(hand):
    if sum(hand) > 21 and 11 in hand:
        hand[hand.index(11)] = 1   # change first ace to 1
    return hand

def play_round(user_hand, dealer_hand, is_first_round, is_last_round):
    if is_first_round:
        add_random_card(user_hand)
        add_random_card(dealer_hand)
        add_random_card(user_hand)
        add_random_card(dealer_hand)
    elif not is_last_round:
        add_random_card(user_hand)
    elif is_last_round:
        add_random_card(dealer_hand)
    
    user_hand = adjust_ace(user_hand)
    dealer_hand = adjust_ace(dealer_hand)
    
    return user_hand, dealer_hand
    

def play_game():
    print(logo)

    play_game = True
    while play_game:
        if input("Do you want to play a game of Blackjack? Type 'y' or 'n': \n").lower() != 'y':
            play_game = False
            print('\n' * 100)
            return
        users_cards = []
        dealers_cards = []
        game_over = False
        users_cards, dealers_cards = play_round(users_cards, dealers_cards, is_first_round=True, is_last_round = False)
        while not game_over:
            print(f"Your cards: {users_cards}, current score: {sum(users_cards)}")
            print(f"Dealer's first card: {dealers_cards[:1]}") 

            if sum(users_cards) > 21: # this is the first losing condition
                print('You went Over: You Lose')
                game_over = True
                break
            elif sum(users_cards) == 21:
                print('You Win!')
                game_over = True
                break
            if input("Type 'y' to get another card, 'n' to pass: \n").lower() != 'y':
                while sum(dealers_cards) < 17:
                    users_cards, dealers_cards = play_round(users_cards, dealers_cards, is_first_round=False, is_last_round = True)
                print(f"Your final hand: {users_cards}, final score: {sum(users_cards)}")
                print(f"Dealer's final hand: {dealers_cards}, final score: {sum(dealers_cards)}") 
                if sum(dealers_cards) > 21:
                    print('Dealer busts: You win!')
                    game_over = True
                    break
                elif sum(users_cards) > sum(dealers_cards):
                    print('You have the higher score, you win!')
                    game_over = True
                    break
                elif sum(users_cards) < sum(dealers_cards):
                    print('You have the lower score, you lose!')
                    game_over = True
                    break
                else:
                    print('equal score, its a tie')
                    game_over = True
                    break
            users_cards, dealers_cards = play_round(users_cards, dealers_cards, is_first_round=False, is_last_round = False)
    

if __name__ == "__main__":
     play_game()
        
