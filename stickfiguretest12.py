from graphix import Window, Point, Line, Circle, Rectangle, Text

def boxer():
    win = Window("Stick figure", 600, 400)
    head = Circle(Point(400, 120), 40)
    head.draw(win)
    body = Line(Point(400, 160), Point(400, 240))
    body.draw(win)
    arms = Line(Point(320, 180), Point(480, 180))
    arms.draw(win)
    
    #gloves
    glove1 = Circle(Point(305, 180), 15)
    glove1.fill_colour = "blue"
    glove1.draw(win)
    glove2 = Circle(Point(495, 180), 15)
    glove2.fill_colour = "blue"
    glove2.draw(win)
    
    leg1 = Line(Point(400, 240), Point(340, 340))
    leg1.draw(win)
    leg2 = Line(Point(400, 240), Point(460, 340))
    leg2.draw(win)
    
    #eyes
    eye1 = Circle(Point(420,120), 10)
    eye1.draw(win)
    eye2 = Circle(Point(380,120), 10)
    eye2.draw(win)
    
    #text
    message = Text(Point(150, 50), "punch!!!")
    message.draw(win)
    
    for x in range(1,10):
        win.get_mouse()
        message.text = ("o" * x) + "w"
    
    win.get_mouse()
    message.text = "stop!"
    eye1.fill_colour = "black"
    
    
    win.get_mouse()
    win.close()

boxer()