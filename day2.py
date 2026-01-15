print("Welcome to the tip calculator")
total = float(input("What was the total of the bill?"))
tip = int(input("how much do you wanna tip? 10, 12 or 15?"))/100 + 1
people = int(input("How many people are paying?"))
total_pp = round((total * tip) / people, 2)
print(f"each person should pay {total_pp}")