from graphix import Window,Line,Point,Circle
import random
import math

def get_inputs():
    num_walks = int(input("How many random walks to take? "))
    distance = int(input("Distance of the furthest walk? "))
    return num_walks, distance

def distance_calc(center,pos):
    a = center.x - pos.x
    b = center.y - pos.y
    c = math.sqrt(a**2 + b**2)
    return c


def take_walks(win,num_walks,distance):
    colours = ["red","blue","green","pink"]
    for i in range(num_walks):
        center = Point(distance,distance)
        pos_x = distance
        pos_y = distance
        in_bounds = True
        while in_bounds:
            old_x = pos_x
            old_y = pos_y
            num = random.randint(1,4)
            if num == 1:
                pos_x += 5
            elif num == 2:
                pos_x -= 5
            elif num == 3:
                pos_y += 5
            else:
                pos_y -= 5
            
            step = Line(Point(old_x,old_y),Point(pos_x,pos_y))
            step.draw(win)
            num = random.randint(0,3)
            step.fill_colour = colours[num]

            displacement = distance_calc(center,Point(pos_x,pos_y))
            if displacement < distance:
                in_bounds = True
            else:
                in_bounds = False


def main():
    inputs = get_inputs()
    distance = inputs[1]

    win = Window("graphical walks",distance * 2,distance * 2)
    circle = Circle(Point(distance,distance),distance)
    circle.draw(win)

    take_walks(win,inputs[0],inputs[1])

    win.get_mouse()
    win.close()

main()