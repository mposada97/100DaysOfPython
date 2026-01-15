import random
import sys

user = int(input("What do you choose? 0 for Rock, 1 for paper, 2 for scissor "))
machine = random.randint(0,2)
options = ("Rock", "Paper", "Scissors")

if user < 0 or user >=3:
    print("you typed an invalid number, you lose")
    sys.exit()

print(f"you chose {options[user]}")
print(f"machine chose {options[machine]}")

if user == machine:
    print("tie")
elif (user == 0 and machine == 2) or (user == 1 and machine == 0) or (user == 2 and machine == 1):
    print("you win")
else:
    print("you lose")
