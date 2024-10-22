from graphix import Window, Point, Circle, Line, Rectangle, \
                    Polygon, Text, Entry
import math

def hello_graphix():
    win = Window()
    message = Text(Point(200, 200), "hello graphix!")
    message.draw(win)

def draw_line():
    win = Window()
    message = Text(Point(200, 50), "click on first point")
    message.draw(win)
    p1 = win.get_mouse()
    message.text = "click on second point"
    p2 = win.get_mouse()
    line = Line(p1, p2)
    line.draw(win)
    message.text = "click anywhere to quit"
    win.get_mouse()
    win.close()



# Solutions below:

def draw_stick_figure():
    win = Window()
    head = Circle(Point(200, 120), 40)
    head.draw(win)
    body = Line(Point(200, 160), Point(200, 240))
    body.draw(win)
    arm1 = Line(Point(200,160),Point(220,200))
    arm1.draw(win)
    arm2 = Line(Point(200,160),Point(180,200))
    arm2.draw(win)
    leg1 = Line(Point(200,240),Point(220,300))
    leg1.draw(win)
    leg2 = Line(Point(200,240),Point(180,300))
    leg2.draw(win)
    win.get_mouse()
    win.close()

def draw_circle():
    win = Window()
    radius = int(input("Enter the radius of the circle: "))
    c = Circle(Point(200,200),radius)
    c.draw(win)
    win.get_mouse()
    win.close()

def draw_archery_target():
    win = Window()

    circle1 = Circle(Point(200,200),30)
    circle1.outline_width = 60
    circle1.outline_colour = "blue"
    circle1.draw(win)

    circle2 = Circle(Point(200,200),20)
    circle2.outline_width = 40
    circle2.outline_colour = "red"
    circle2.draw(win)

    circle3 = Circle(Point(200,200),10)
    circle3.outline_width = 20
    circle3.outline_colour = "yellow"
    circle3.draw(win)


    win.get_mouse()
    win.close()

def draw_rectangle():
    win = Window()
    height = int(input("Enter the height: "))
    width = int(input("Enter the width: "))

    line1 = Line(Point(200-(width//2),200+(height//2)),Point(200+(width//2),200+(height//2)))
    line1.draw(win)
    line2 = Line(Point(200-(width//2),200-(height//2)),Point(200+(width//2),200-(height//2)))
    line2.draw(win)

    line3 = Line(Point(200+(width//2),200-(height//2)),Point(200+(width//2),200+(height//2)))
    line3.draw(win)
    line4 = Line(Point(200-(width//2),200-(height//2)),Point(200-(width//2),200+(height//2)))
    line4.draw(win)

    win.get_mouse()
    win.close()

def blue_circle():
    win = Window()

    pos = win.get_mouse()
    circle1 = Circle(Point(pos.x,pos.y),100)
    circle1.outline_colour = "blue"
    circle1.fill_colour = "blue"
    circle1.draw(win)

    win.get_mouse()
    win.close()

def ten_lines():
    win = Window()

    for _ in range(10):
        p1 = win.get_mouse()
        p2 = win.get_mouse()
        line = Line(p1, p2)
        line.draw(win)

    win.get_mouse()
    win.close()

def ten_strings():
    win = Window()

    for _ in range(10):
        input_box = Entry(Point(200, 50), 10)
        input_box.draw(win)
        win.get_mouse()
        user_input = input_box.text

        pos = win.get_mouse()
        message = Text(Point(pos.x, pos.y), user_input)
        message.draw(win)



    win.get_mouse()
    win.close()

def ten_coloured_rectangles():
    win = Window()

    colour = "blue"

    for _ in range(10):
        input_box = Entry(Point(200, 50), 10)
        input_box.text = colour
        input_box.draw(win)
        win.get_mouse()
        user_input = input_box.text
        colour = user_input

        pos1 = win.get_mouse()
        pos2 = win.get_mouse()

        rectangle = Rectangle(Point(pos1.x,pos1.y),Point(pos2.x,pos2.y))
        rectangle.draw(win)
        rectangle.fill_colour = colour

    win.get_mouse()
    win.close()

def five_click_stick_figure():
    win = Window()

    pos1 = win.get_mouse()
    pos2 = win.get_mouse()
    radius = math.sqrt(((pos1.x-pos2.x)**2)+((pos1.y-pos2.y)**2))
    head = Circle(Point(pos1.x,pos1.y),math.ceil(radius))
    head.draw(win)

    pos3 = win.get_mouse()
    body = Line(Point(pos1.x,pos1.y+math.ceil(radius)),Point(pos1.x,pos3.y))
    body.draw(win)

    pos4 = win.get_mouse()
    arm = Line(Point(pos4.x,pos4.y),Point(pos1.x+(pos1.x-pos4.x),pos4.y))
    arm.draw(win)

    pos5 = win.get_mouse()
    leg1 = Line(Point(pos5.x,pos5.y),Point(pos1.x,pos3.y))
    leg1.draw(win)
    leg2 = Line(Point(pos1.x+(pos1.x-pos5.x),pos5.y),Point(pos1.x,pos3.y))
    leg2.draw(win)

    win.get_mouse()
    win.close()
