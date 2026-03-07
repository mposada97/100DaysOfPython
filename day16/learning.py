#in this exercise we import packages, and use their classes to create our objects and we intercat with those objects using the methods.
import turtle

timmy  = turtle.Turtle()

timmy.shape("turtle")
timmy.color("green")
timmy.forward(100)

my_screen = turtle.Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Charmander", "Squirtle"])
table.add_column("Type", ["Electric", "Fire", "water"])
table.add_row(["Bulbasour", "Grass"])
table.align = "l" #here we modify an attribute of the class, align is not a method

print(table)