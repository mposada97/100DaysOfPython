#the purpose of this excercise is to debug, used the debugger in vs code to add break points, step over, and drill into my code.
import random
import maths

def mutate(a_list):
    b_list = []
    new_item = 0 
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1,3)
        new_item = maths.add(new_item, item)
        b_list.append(new_item)
    print(b_list)

mutate([1,2,3,5,8,13])
