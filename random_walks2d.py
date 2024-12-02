import math
import random

def get_inputs():
    num_walks = int(input("How many random walks to take? "))
    num_steps = int(input("How many steps for each walk? "))
    return num_walks, num_steps

def take_a_walk(num_steps):
    step_x = 0
    step_y = 0
    for step in range(num_steps):
        number = random.randint(1,4)
        if number == 1:
            step_y += 1
        elif number == 2:
            step_y -= 1
        elif number == 3:
            step_x += 1
        else:
            step_x -= 1
    
    distance = round(math.sqrt(step_x**2 + step_y**2),2)
        
            
    return (distance)

def take_walks(num_walks, num_steps):
    total_steps = 0
    for walk in range(num_walks):
        steps_away = take_a_walk(num_steps)
        total_steps = total_steps + steps_away
    return total_steps / num_walks

def print_expected_distance(average_steps):
    print("The expected distance is", end=" ")
    print("start point is", average_steps)

def main():
    num_walks, num_steps = get_inputs()
    average_steps = take_walks(num_walks, num_steps)
    print_expected_distance(average_steps)

main()