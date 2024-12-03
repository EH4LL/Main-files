from graphix import Window, Point, Rectangle, Polygon
import random


def main():
    # `get_inputs` returns two values, so we need to receive them both
    door_colour, lights_chance, house_number = get_inputs()
    win = Window("street",200 * house_number,200)
    for i in range(house_number): #drawing all the houses
        #probability of light being on
        num = random.random()
        if num > (1 - lights_chance):
            lights_on = True
        else:
            lights_on = False
        
        draw_house(win,door_colour, lights_on,(200 * i))


def get_inputs():
    house_number = int(input("Enter how many houses: "))
    door_colour = input("Enter shared door colour: ")
    lights_chance = float(input("Probability the lights are on (0 <= x <= 1): "))
    return door_colour, lights_chance, house_number


def draw_house(win,door_colour, lights_on, bottom_left_x):
    list_of_points = [Point(bottom_left_x, 60), Point(bottom_left_x + 100, 0), Point(bottom_left_x + 198, 60)]
    roof = Polygon(list_of_points)
    roof.fill_colour = "pink"
    roof.outline_colour = "pink"
    roof.draw(win)

    # draw wall and door
    draw_rectangle(win, Point(bottom_left_x + 2, 60), Point(bottom_left_x + 198, 198), "brown")
    draw_rectangle(win, Point(bottom_left_x + 30, 110), Point(bottom_left_x + 80, 198), door_colour)

    # draw window
    if lights_on:
        window_colour = "yellow"
    else:
        window_colour = "black"
    draw_rectangle(win, Point(bottom_left_x + 110, 110), Point(bottom_left_x + 170, 170), window_colour)


def draw_rectangle(win, point1, point2, colour):
    rectangle = Rectangle(point1, point2)
    rectangle.fill_colour = colour
    rectangle.outline_colour = colour
    rectangle.draw(win)


main()