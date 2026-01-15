#hangman
import random

# determine number of lives
lives = 10
#Generate random word from list and start hidden word string
word_list = ["mateo", "aardvark", "camel", "baboon"] 
chosen_word = random.choice(word_list).lower()
hidden_word = ""
for a in chosen_word:
    hidden_word += "_"
print(hidden_word)

# enter a loopt to ask for a guess while the user hasnnt won and still has lives left
while lives > 0 and chosen_word != hidden_word:
    # ask and get a guess letter
    guess = input("Guess a letter: ").lower()
    print(guess)
    #check for matches to display the guess if correct or deduct lives if incorrect
    if guess in chosen_word:
        for i, a in enumerate(chosen_word):
            if a == guess:
                hidden_word = hidden_word[:i] + guess + hidden_word[i+1:]
    else:
        lives -= 1
    #display word progress and number of lives or hangman drawing
    print(hidden_word) 
    print(f"you have {lives} lives left")

if lives == 0:
    print(f"You Lost, the correct word was: {chosen_word}")
else:
    print("You Won")