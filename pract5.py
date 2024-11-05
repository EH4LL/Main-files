import math
from graphix import Window, Circle, Point


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

#exercise 1
def circumference_of_circle(radius):
    return math.pi * radius

#exercise 2
def circle_info():
    r = float(input("Enter the radius of a cirlce: "))
    return f"The area is {round(area_of_circle(r),3)} and the circumference is {round(circumference_of_circle(r),3)}"

# For exercise 3
def draw_circle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.fill_colour = colour
    circle.outline_width = 2
    circle.draw(win)


def draw_brown_eye_in_centre():
    win = Window()
    draw_circle(win, Point(200,200), 120, "white")
    draw_circle(win, Point(200,200), 60, "brown")
    draw_circle(win, Point(200,200), 30, "black")
    win.get_mouse()

draw_brown_eye_in_centre()


# For exercise 5
def draw_brown_eye(win, centre, radius):
    pass
    # Remove pass and add your code here
