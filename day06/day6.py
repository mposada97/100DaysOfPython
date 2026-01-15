#solution to: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=problem_world2.json&url=user_world%3Aproblem_world2.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def go_straight():
    while front_is_clear():
        move()
def find_wall_on_right():
    go_straight()
    turn_left() 
    
find_wall_on_right()
while at_goal() == False:
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
        
        