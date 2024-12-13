from graphix import Window, Rectangle, Point, Line, Polygon

def plain_patch(win,colour,top_left):
    bot_right = Point(top_left.x + 100,top_left.y + 100)
    rect = Rectangle(top_left,bot_right)
    rect.draw(win)
    rect.fill_colour = colour

def lattice_patch(win,colour,top_left):
    #lattice lines using coords and for loops
    for i in range(0,101,20):
        start = Point(top_left.x + i,top_left.y)
        end_1 = Point(top_left.x + 100,top_left.y - i + 100)
        end_2 = Point(top_left.x,top_left.y + i)

        line_1 = Line(start,end_1)
        line_1.draw(win)
        line_1.outline_colour = colour

        line_2 = Line(start,end_2)
        line_2.draw(win)
        line_2.outline_colour = colour
    
    for i in range(20,100,20):
        start = Point(top_left.x, top_left.y + i)
        end_1 = Point(top_left.x + 100 - i,top_left.y + 100)
        end_2 = Point(top_left.x + 100,top_left.y + 100 - i)

        line_1 = Line(start,end_1)
        line_1.draw(win)
        line_1.outline_colour = colour

        line_2 = Line(end_1,end_2)
        line_2.draw(win)
        line_2.outline_colour = colour

def triangle_patch(win,colour,top_left):
    #printing both rows of triangles
    for i in range(0,81,40):
        triangle_row_1(win,colour,Point(top_left.x,top_left.y + i))
    for i in range(20,61,40):
        triangle_row_2(win,colour,Point(top_left.x,top_left.y + (i)))

def triangle_row_1(win,colour,top_left):
    #triangle row (reg triangles)
    for i in range(0,100,20):
        triangle(win,colour,Point(top_left.x + i,top_left.y),1)

def triangle_row_2(win,colour,top_left):
    #triangle row (featuring half triangles)
    triangle(win,colour,Point(top_left.x - 10,top_left.y),2)
    for i in range(10,90,20):
        triangle(win,colour,Point(top_left.x + i,top_left.y),1)
    triangle(win,colour,Point(top_left.x + 90,top_left.y),3)


def triangle(win,colour,top_left,type):

    top_right = Point(top_left.x + 20,top_left.y)
    middle = Point(top_left.x + 10,top_left.y)
    bottom = Point(top_left.x + 10,top_left.y + 20)

    if type == 1:
        points = [top_left,top_right,bottom]
    
    elif type == 2:
        points = [middle,top_right,bottom]
    
    elif type == 3:
        points = [top_left,middle,bottom]
    
    else:
        return "Parameter type error"


    triangle = Polygon(points)
    triangle.draw(win)
    triangle.outline_colour = colour
    triangle.fill_colour = colour

def validation(value,valid_list):
    if value not in valid_list:
        value = input("This value was not valid, please enter a new one: ")
        value = validation(value,valid_list)
    return value

def main():
    patches = {}
    valid_sizes = ["5","7","9"]
    valid_colours = ["red","green","blue","magenta","orange","purple"]
    #inputs
    size = input("Enter the size of the patchwork: ")
    size = int(validation(size,valid_sizes))
    
    colour_1 = input("Enter the first colour: ")
    colour_1 = validation(colour_1,valid_colours)
    valid_colours.remove(colour_1)

    colour_2 = input("Enter the second colour: ")
    colour_2 = validation(colour_2,valid_colours)
    valid_colours.remove(colour_2)

    colour_3 = input("Enter the third colour: ")
    colour_3 = validation(colour_3,valid_colours)



    width = size * 100
    height = size * 100
    win = Window("Patchwork",width,height)
    for x in range(0,width,100):
        for y in range(0,height,100):
            pos = Point(x,y)
            #lattices
            if x == y:
                patch = lattice_patch(win,colour_1,pos)
            elif y == 0:
                patch = lattice_patch(win,colour_2,pos)
            elif x == width - 100:
                patch = lattice_patch(win,colour_2,pos)

            #plain
            elif x == 0:
                patch = plain_patch(win,colour_3,pos)
            elif y == height - 100:
                patch = plain_patch(win,colour_3,pos)

            #triangle + plain in gaps
            elif x > y:
                patch = plain_patch(win,colour_2,pos)
            else:
                patch = triangle_patch(win,colour_3,pos)
            
            #adding patches to dictionary
            patches.append(patch,pos)
            
    patches(Point(200,100)).undraw(win)
    win.get_mouse()
    win.close()

main()