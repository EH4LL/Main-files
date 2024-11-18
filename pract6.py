import math
import random
from graphix import Circle, Window, Point, Text, Rectangle
# Remember to update the line above if you are using other Graphix objects
from pract5 import distance_between_points


def greet(name):
    print("Hello", name + ".")
    if len(name) > 20:
        print("That's a long name!")


def can_you_vote(age):
    if age >= 18:
        print("You can vote")
    else:
        print("Sorry, you can't vote")


def get_degree_class(mark):
    if mark >= 70:
        return "1st"
    elif mark >= 60:
        return "2:1"
    elif mark >= 50:
        return "2:2"
    elif mark >= 40:
        return "3rd"
    else:
        return "Fail"


# We will simplify this function later in the term
def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def days_in_month(month, year):
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    else:
        return 31


def overly_complex_days_in_month(month, year):
    if month == 1 or month == 3 or month == 5 or month == 7 or \
       month == 8 or month == 10 or month == 12:
        return 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif is_leap_year(year):
        return 29
    else:
        return 28


def count_down():
    for i in range(10, 0, -1):
        print(i, "...", end=" ")
    print("Blast Off!")


def numbered_triangle(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


# For exercises 8 & 11
def draw_circle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.fill_colour = colour
    circle.outline_width = 2
    circle.draw(win)


# For exercise 8
def draw_coloured_eye(win, centre, radius, colour):
    draw_circle(win, centre, radius, "white")
    draw_circle(win, centre, radius//2, colour)
    draw_circle(win, centre, radius//4, "black")

def fast_food_order():
    price = float(input("Enter the price of the order: "))
    if price >= 20:
        price -= 2.5
    price += 2.5
    print(f"The total price of your order is £{price}")

def what_to_do_today():
    temp = int(input("Enter the temperature: "))
    if temp > 25:
        print("Go swimming in the sea")
    elif temp >= 10:
        print("Go shopping in gunwarf quays")
    else:
        print("Watch a film at home")

def display_square_roots(start,end):
    for i in range(start,end+1):
        root = math.sqrt(i)
        print(f"The square root of {i} is {round(root,3)}")

def calculate_grade(mark):
    if mark > 20 or mark < 0:
        return "X"
    elif mark >= 16:
        return "A"
    elif mark >= 12:
        return "B"
    elif mark >= 8:
        return "C"
    else:
        return "F"
    
def peas_in_a_pod():
    num = int(input("Enter a number: "))
    win = Window("Pod",100*num,100)
    for i in range(num):
        pea = Circle(Point((i*100) + 50,50),50)
        pea.fill_colour = "green"
        pea.draw(win)

    win.get_mouse()
    win.close()

def ticket_price(distance,age):
    cost = 10 + (distance * 0.15)
    if age >= 60 or age <= 15:
        cost *= 0.4
    return round(cost,2)

def numbered_square(n):
    for x in range(n):
        line = ""
        for y in range(n,n*2):
            line += str(y-x)
            line += " "
        print(line)

def eye_picker():
    win = Window()
    x = int(input("Enter the x coordinate for the center: "))
    y = int(input("Enter the y coordinate for the center: "))

    coord = [x,y]
    valid_colour = ["blue","green","grey","brown"]

    for _ in range(2):
        if coord[_] > 400 or coord[_] < 0:
            return("Eye centre not in window")
    
    r = int(input("Enter the radius: "))
    colour = input("Enter the colour: ")
    if colour not in valid_colour:
        return("Not a valid eye colour")

    draw_coloured_eye(win,Point(x,y),r,colour)

def draw_patch_window():
    win = Window()
    for i in range(5):
        for j in range(5):
            square = Rectangle(Point(20*i,20*j),Point(20*(i+1),20*(j+1)))
            square.outline_colour = "red"
            square.draw(win)
    
    for i in range(5):
        for j in range(5):
            message = Text(Point(10+(20*i),(10+20*j)),"hi!")
            message.text_colour = "red"
            message.size = 10
            message.draw(win)
    

def draw_patch(win, x, y, colour):
    for i in range(5):
        for j in range(5):
            square = Rectangle(Point(x+(20*i),y+(20*j)),Point(x+(20*(i+1)),y+(20*(j+1))))
            square.outline_colour = colour
            square.draw(win)
    
    for i in range(5):
        for j in range(5):
            message = Text(Point((x+10)+(20*i),(y+10)+(20*j)),"hi!")
            message.text_colour = colour
            message.size = 10
            message.draw(win)
    

def draw_patchwork():
    win = Window()
    for i in range(2):
        for j in range(3):
            draw_patch(win,j*100,i*100,"blue")
    
    win.get_mouse()
    win.close()

def eyes_all_around():
    win = Window("eyes",500,500)

    colour = ["blue","grey","green","brown"]
    count = 0
    for x in range(30):
        pos = win.get_mouse()
        draw_coloured_eye(win,pos,30,colour[count])
        count += 1
        if count == 4:
            count -= 4
    
    win.get_mouse()
    win.close()

def archery_game():
    win = Window()
    score = 0
    centre = Point(200,200)

    draw_circle(win,centre,180,"blue")
    draw_circle(win,centre,120,"red")
    draw_circle(win,centre,60,"yellow")

    for _ in range(5):
        pos = win.get_mouse()
        x = pos.x + random.randint(-50,50)
        y = pos.y + random.randint(-50,50)
        arrow = Point(x,y)

        draw_circle(win,arrow,5,"black")
        distance = distance_between_points(centre,arrow)
        if distance <= 60:
            score += 10
        elif distance <= 120:
            score += 5
        elif distance <= 180:
            score += 2

    print(score)
    win.get_mouse()
    win.close()