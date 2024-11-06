import math
import random
from graphix import Window, Circle, Point, Text, Line


def greet(name):
    return f"Hello, {name}!"


def product(a, b):
    return a * b


def divide(a, b):
    return a / b


def divide_and_product(a, b):
    product_result = product(a, b)
    divide_result = divide(a, b)
    return product_result, divide_result


def main():
    my_name = input("What is your name? ")
    greeting = greet(my_name)
    print(greeting)

    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    product_result, divide_result = divide_and_product(num1, num2)
    print(f"{num1} * {num2} = {product_result}")
    print(f"{num1} / {num2} = {divide_result}")


def calc_future_value(amount, years):
    interest_rate = 0.065
    for year in range(years):
        amount = amount * (1 + interest_rate)
    return amount


def future_value():
    amount = float(input("Enter an amount to invest: "))
    years = int(input("Enter the number of years: "))
    final = calc_future_value(amount, years)

    output = f"Investing £{amount:0.2f} for {years} years "
    output += f"results in £{final:0.2f}."
    print(output)


# For exercises 1 and 2
def area_of_circle(radius):
    return math.pi * radius ** 2


# For exercise 3
def draw_circle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.fill_colour = colour
    circle.outline_width = 2
    circle.draw(win)


# For exercise 5
def draw_brown_eye(win, centre, radius):
    draw_circle(win, centre, radius, "white")
    draw_circle(win, centre, radius//2, "brown")
    draw_circle(win, centre, radius//4, "black")

#solutions

def circumference_of_circle(radius):
    return math.pi * radius


def circle_info():
    r = float(input("Enter the radius of a cirlce: "))
    return f"The area is {round(area_of_circle(r),3)} and the circumference is {round(circumference_of_circle(r),3)}"


def draw_brown_eye_in_centre():
    win = Window()
    draw_circle(win, Point(200,200), 120, "white")
    draw_circle(win, Point(200,200), 60, "brown")
    draw_circle(win, Point(200,200), 30, "black")
    win.get_mouse()


def draw_block_of_stars(width,height):
    for _ in range(height):
        print("*" * width)

def draw_block_of_spaces(width,height):
    for _ in range(height):
        print(" " * width)

def draw_letter_e():
    draw_block_of_stars(8,2)
    draw_block_of_stars(2,2)
    draw_block_of_stars(5,2)
    draw_block_of_stars(2,2)
    draw_block_of_stars(8,2)

def draw_pair_of_brown_eyes():
    win = Window()
    draw_brown_eye(win,Point(100,200),100)
    draw_brown_eye(win,Point(300,200),100)
    win.get_mouse()
    

def distance_between_points(p1,p2):
    a = p1.x - p2.x
    b = p1.y - p2.y
    return math.sqrt(a**2 + b**2)


def distance_calculator():
    win = Window()
    message = Text(Point(200, 150), "Click on two locations")
    message.draw(win)

    pos1 = win.get_mouse()
    pos2 = win.get_mouse()

    message.text = str(distance_between_points(pos1,pos2))

    win.get_mouse()

def draw_blocks(s1,a1,s2,a2,h):
    for _ in range(h):
        print(" "*s1 + "*"*a1 + " "*s2 + "*"*a2)

def draw_letter_a():
    draw_blocks(1,8,1,0,2)
    draw_blocks(0,2,6,2,2)
    draw_blocks(0,10,0,0,2)
    draw_blocks(0,2,6,2,3)

def draw_four_pairs_of_brown_eyes():
    win = Window()

    click1 = win.get_mouse()    
    click2 = win.get_mouse()
    pos1 = int(math.ceil(distance_between_points(click1,click2)))
    
    draw_brown_eye(win,click1,pos1)
    draw_brown_eye(win,Point(click1.x + pos1*2,click1.y),pos1)

    click3 = win.get_mouse()    
    click4 = win.get_mouse()
    pos2 = int(math.ceil(distance_between_points(click3,click4)))

    draw_brown_eye(win,click3,pos2)
    draw_brown_eye(win,Point(click3.x + pos2*2,click3.y),pos2)
    win.get_mouse()


def display_text_with_spaces(win,string,size,coord):
    result = ""
    for x in range(len(string)):
        result += string[x].upper()
        result += " "
    message = Text(coord,result)
    message.size = size
    message.draw(win)

def construct_vision_chart():
    win = Window()
    sizes = 30
    # the wolf howls and the hawk tuahs
    for i in range(6):
        user_input = input("Enter a string: ")
        display_text_with_spaces(win,user_input,sizes - (i * 5),Point(200,50 + (i * 50)))
    
    win.get_mouse()

def draw_stick_figure(win,pos,size):
    radius = 5 * size
    r2 = radius//2
    center = Point(pos.x, pos.y - (radius*2))
    bottom = Point(pos.x, pos.y + radius)
    head = Circle(Point(pos.x, pos.y - (radius*3)), radius)
    head.draw(win)
    body = Line(center, Point(pos.x, pos.y + radius))
    body.draw(win)
    arm1 = Line(center,Point(pos.x + (r2),pos.y))
    arm1.draw(win)
    arm2 = Line(center,Point(pos.x - (r2),pos.y))
    arm2.draw(win)
    leg1 = Line(bottom,Point(pos.x + (r2),pos.y + math.ceil(radius * 2.5)))
    leg1.draw(win)
    leg2 = Line(bottom,Point(pos.x - (r2),pos.y + math.ceil(radius * 2.5)))
    leg2.draw(win)

def draw_stick_figure_family():
    win = Window()
    
    for j in range(1,5):
        draw_stick_figure(win,Point(75*j,250),random.randint(2,7))
    win.get_mouse()

draw_stick_figure_family()