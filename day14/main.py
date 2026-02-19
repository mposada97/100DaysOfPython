from art import logo, vs
from game_data import data
import random

def choose_celeb(celeb_list):
    random_index = random.randrange(len(celeb_list))
    # Remove and return the item at that index
    random_celeb = celeb_list[random_index]
    return random_celeb, random_index

def play_game(celebs):
     celeb_a, index_a = choose_celeb(celebs)
     celebs.pop(index_a)
     print(celeb_a)
     print(celebs)
     return


if __name__ == "__main__":
     play_game(data)