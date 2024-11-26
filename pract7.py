import time
import random
from graphix import Window, Circle, Point, Text, Entry, Line, Rectangle
from pract5 import draw_brown_eye, distance_between_points


def hello_while():
    i = 0
    while i < 10:
        print("i is now", i)
        i = i + 1


def countdown():
    i = 10
    while i > 0:
        print(i, "...", end=" ")
        i = i - 1
    print("Blast Off!")


def mystery_loop():
    i = 1
    # Be careful! This loop will run forever!
    while i < 1000:
        print(i)
        i = i * 2


def add_up_numbers1():
    total = 0
    more_numbers = "y"
    while more_numbers == "y":
        number = int(input("Enter a number: "))
        total = total + number
        more_numbers = input("Any more numbers? (y/n) ")
    print("The total is", total)


def add_up_numbers2():
    total = 0
    number = int(input("Number (0 to stop): "))
    while number != 0:
        total = total + number
        number = int(input("Number (0 to stop): "))
    print("The total is", total)


def add_up_numbers3():
    total = 0
    n_str = input("Number (hit enter to stop): ")
    while n_str != "":
        number = int(n_str)
        total += number
        n_str = input("Number (hit enter to stop): ")
    print("The total is", total)


def add_up_numbers4():
    total = 0
    while True:
        n_str = input("Number (anything else to stop): ")
        if not n_str.isdigit():
            break  # Exit the loop if the input is not a number
        number = int(n_str)
        total += number
    print("The total is", total)


# Note: msg == "" needs to appear twice
def get_string1():
    msg = ""
    while msg == "":
        msg = input("Enter a non-empty string: ")
        if msg == "":
            print("You didn't enter anything!")
    return msg


def get_string2():
    while True:
        msg = input("Enter a non-empty string: ")
        if msg != "":
            break
        print("You didn't enter anything!")
    return msg


def can_apply_for_job(degree, experience):
    if (degree == "1st" or degree == "2:1") and experience >= 1:
        return True
    elif degree == "2:2" and experience >= 2:
        return True
    else:
        return False


def can_vote1():
    age = int(input("How old are you? "))
    while age <= 18:
        print("Wait until you are 18!")
        age = int(input("How old are you? "))


def can_vote2():
    while True:
        age = int(input("How old are you? "))
        if age > 18:
            break
        print("Wait until you are 18!")


#  For question 2
def traffic_lights():
    win = Window()
    red = Circle(Point(100, 50), 20)
    red.fill_colour = "red"
    red.draw(win)
    amber = Circle(Point(100, 100), 20)
    amber.fill_colour = "black"
    amber.draw(win)
    green = Circle(Point(100, 150), 20)
    green.fill_colour = "black"
    green.draw(win)
    while True:
        time.sleep(3)
        amber.fill_colour = "yellow"
        time.sleep(3)
        red.fill_colour = "black"
        amber.fill_colour = "black"
        green.fill_colour = "green"
        time.sleep(3)
        green.fill_colour = "black"
        amber.fill_colour = "yellow"
        time.sleep(3)
        amber.fill_colour = "black"
        red.fill_colour = "red"


# For question 6
def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

# Solutions to the programming exercises:

def get_name():
    name = input("Enter a name: ")
    while not name.isalpha():
        name = input("That name is invalid, enter a new one: ")
        

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

def grade_coursework():
    invalid = False
    mark = input("Enter a mark: ")
    
    if not mark.isdigit():
        invalid = True
    else:
        mark = int(mark)
        if mark > 20 or mark < 0:
            invalid = True
        
    while invalid:
        mark = input("That mark is invalid, enter a new one: ")
        invalid = False
        
        if not mark.isdigit():
            invalid = True
        else:
            mark = int(mark)
            if mark > 20 or mark < 0:
                invalid = True

    print(calculate_grade(mark))
    
def order_price():
    order = 0
    run = "y"
    while run == "y":
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))
        order += round((price * quantity),2)
        run = input("Is there more (y/n)")
    print("")
    print(f"The total price of the order is £{order:.2f}")

def clickable_eye():
    win = Window("Clickable eye",500,500)
    centre = Point(200,200)
    run = True
    output = ""
    draw_brown_eye(win,centre,100)
    message = Text(Point(200,350),output)
    message.draw(win)
    while run:
        pos = win.get_mouse()
        distance = distance_between_points(pos,centre)
        if distance <= 25:
            output = "pupil"
        elif distance <= 50:
            output = "iris"
        elif distance <= 100:
            output = "sclera"
        else:
            run = False
            win.close()
        
        message.text = output

def temperature_converter():
    win = Window()
    msg1 = Text(Point(130,100),"Temp to Convert:")
    msg1.draw(win)
    msg2 = Text(Point(130,130),"Direction: (C2F/F2C)")
    msg2.draw(win)
    msg3 = Text(Point(130,300),"Do you need to convert more? (y/n)")
    msg3.draw(win)
    msg4 = Text(Point(195,160),"")
    msg4.draw(win)

    input_temp = Entry(Point(260, 100), 10)
    input_temp.draw(win)
    input_conv = Entry(Point(260, 130), 10)
    input_conv.draw(win)
    input_run = Entry(Point(300,300),10)
    input_run.draw(win)

    while True:
        if input_conv.text == "C2F":
            converted = celsius_to_fahrenheit(int(input_temp.text))
        elif input_conv.text == "F2C":
            converted = fahrenheit_to_celsius(int(input_temp.text))
        else:
            converted = "Invalid conversion"
        
        msg4.text = f"Output = {converted}"

        if input_run.text == "n":
            break

    win.close()

def table_tennis_scorer():
    win = Window("Table Tennis Scorer")
    run = True
    score1 = 0
    score2 = 0

    divider = Line(Point(200,0),Point(200,400))
    divider.draw(win)

    player1 = Text(Point(100,200),"0")
    player1.draw(win)
    player2 = Text(Point(300,200),"0")
    player2.draw(win)

    def winner(point):
        result = Text(point,"Winner")
        result.draw(win)

    while run:
        pos = win.get_mouse()
        if pos.x < 200:
            score1 += 1
            player1.text = str(score1)
        elif pos.x > 200:
            score2 += 1
            player2.text = str(score2)
        else:
            continue
        
        if score1 > 10:
            if (score1 - 1) > score2:
                run = False
                winner(Point(100,300))
        if score2 > 10:
            if (score2 - 1) > score1:
                run = False
                winner(Point(300,300))
    
    win.get_mouse()
    win.close()
    

def guess_the_number():
    num = random.randint(1,100)
    run = True
    counter = 0
    while run:
        counter += 1
        if counter > 7:
            print(f"You lose! The number was {num}")
            break
        guess = int(input("Guess the number: "))

        if guess < num:
            print("Too low")
        elif guess > num:
            print("Too high")
        else:
            run = False
            print(f"You won in {counter} attempt(s)")

def clickable_box_of_eyes(rows,columns):
    width = (columns + 1) * 100
    height = (rows + 1) * 100
    

    win = Window("Box of eyes",width,height)

    grid = Rectangle(Point(50,50),Point(width-50,height-50))
    grid.draw(win)

    message = Text(Point(width//2,height-25),"")
    message.draw(win)

    for i in range(rows):
        for j in range(columns):
            center = Point(100 + (j * 100),100 + (i * 100))
            draw_brown_eye(win,center,50)
    
    in_box = True
    while in_box:
        in_eye = False

        pos = win.get_mouse()
        for i in range(rows):
            for j in range(columns):
                center = Point(100 + (j * 100),100 + (i * 100))

                distance = distance_between_points(center,pos)
                if distance <= 50:
                    in_eye = True
                    output = f"Eye at row {i + 1} column {j + 1}"
        
        if in_eye:
            message.text = output
        else:
            if pos.x < (width-50) and pos.x > 50:
                if pos.y < (height-50) and pos.y > 50:
                    message.text = "Between eyes"
                else:
                    in_box = False
            else:
                in_box = False