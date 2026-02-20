from art import logo, vs
from game_data import data
import random

def choose_celeb(celeb_list, side):
    random_index = random.randrange(len(celeb_list))
    # Remove and return the new list and selected celeb
    random_celeb = celeb_list.pop(random_index)
    random_celeb["side"] = side
    return random_celeb, celeb_list

def print_celeb_info(celeb):
     if celeb["side"] == "A":
          return print(f"Compare {celeb["side"]}: {celeb["name"]}, a {celeb["description"]}, from {celeb["country"]}")
     else:
          return print(f"Against {celeb["side"]}: {celeb["name"]}, a {celeb["description"]}, from {celeb["country"]}")

def guess_who_has_more(a,b):
     guess = input("Who has more followers? Type 'A' or 'B': ").upper()
     if guess == "A":
          return a["follower_count"] > b["follower_count"]
     elif guess == "B":
          return a["follower_count"] > b["follower_count"]
     else:
          print("Invalid input, try again")
          guess_who_has_more(a,b)
def new_round(b, list):
     new_a = b
     new_a["side"] = "A"
     new_b, list = choose_celeb(list, "B")
     return new_a, new_b, list

def play_game(celebs):
     print(logo)
     celeb_a, celebs = choose_celeb(celebs, "A") #passes selected celeb and overwrites celebs list to list without the selected celeb, makes the celeb assigned to side A
     print_celeb_info(celeb_a)
     celeb_b, celebs = choose_celeb(celebs, "B")
     print(vs)
     print_celeb_info(celeb_b)
     score = 0
     win = guess_who_has_more(celeb_a, celeb_b)
     while win:
          score += 1
          print("\n" *100)
          print(logo)
          print(f"You're right! Current score: {score}")
          celeb_a, celeb_b, celebs = new_round(celeb_b, celebs)
          print_celeb_info(celeb_a)
          print(vs)
          print_celeb_info(celeb_b)
          win = guess_who_has_more(celeb_a, celeb_b)
     print("\n" *100)
     print(logo)
     print(f"Sorry, that's wrong. Final Score: {score}")
     return


if __name__ == "__main__":
     play_game(data)