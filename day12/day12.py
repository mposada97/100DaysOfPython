import random
# the purpose of this code is practicing scope
def initialize_game():
    print('Welcome to the number guessing game!')
    numbers = list(range(1,101))
    number = random.choice(numbers)
    difficulty = input("Choose difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == 'easy':
        return 10, number
    else:
        return 5, number
def get_guess():
    return input()
def decrease_life(cur_lives):
    return cur_lives - 1

def play_game():
    game_over = False
    lives, number_to_guess = initialize_game()
    while not game_over:
        print(f'You have {lives} attempts remaining to guess the number.')
        guess = int(input('Make a guess: '))
        if guess == number_to_guess:
            print(f'You got it! the answer was {guess}')
            break
        elif guess > number_to_guess:
            print('Too high.')
            lives = decrease_life(lives)
            if lives > 0:
                print('Guess again.')
        else:
            print('Too low.')
            lives = decrease_life(lives)
            if lives > 0:
                print('Guess again.')
        if lives == 0:
            game_over = True
            print("You've run out of guesses. Rerun to play again.")
if __name__ == "__main__":
     play_game()

