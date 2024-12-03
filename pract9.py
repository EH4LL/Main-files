from graphix import Window, Point, Polygon

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
def display_date(d,m,y):
    print(f"{d} {months[m-1]} {y}")

def word_lengths(list):
    for i in range(len(list)):
        print(f"{list[i]} {len(list[i])}")

def draw_hexagon():
    win = Window()
    vertices = []
    for i in range(6):
        pos = win.get_mouse()
        vertices.append(pos)
    hexagon = Polygon(vertices)
    hexagon.draw(win)
    hexagon.fill_colour = "red"
    
    win.get_mouse()
    win.close()
    
def test_marks():
    mark = []
    print("Enter a non number to finish")
    print("")
    while True:
        num = input("Enter mark: ")
        if num.isdigit():
            num = int(num)
            mark.append(num)
        else:
            break
    mark.sort()
    for i in range(mark[-1] + 1):
        print(f"{mark.count(i)} student(s) got {i} marks")
        
def draw_bar_chart(numbers):
    for y in range(1,max(numbers) + 1):
        line = ""
        for x in range(len(numbers)):
            if numbers[x] >= y:
                line += "#"
            else:
                line += " "
        print(line)

def unique_modules(module):
    output = []
    for i in range(len(module)):
        if module[i] not in output:
            output.append(module[i])
            print(module[i])














