import os
from graphix import Window, Point, Circle, Line, Rectangle, \
                    Polygon, Text, Entry


def student_info():
    course = input("What's your course? ")
    student_id = input("What's your ID number? ")
    print("Welcome to:\t" + course)
    print("\n" * 2 + "Your ID number is:\t" + student_id[2:])


def personal_details():
    name = input("What's your name? ")
    age = int(input("What's your age? "))
    height = float(input("What's your height? "))
    # print("name:\t{:>10}\nage:\t{:>10}\nheight:\t{:>10.2f}".format(name, age, height))
    print(f"name:\t{name:>10}\nage:\t{age:>10}\nheight:\t{height:>10.2f}")


def read_quote():
    print("Current directory:\t" + os.getcwd())
    print("Files in current directory:\t" + str(os.listdir()))
    # Change directory to the folder containing quotation.txt
    os.chdir("text_files")
    # Checking if quotation.txt is in the current directory:
    print("Current directory:\t" + os.getcwd())
    print("Files in current directory:\t" + str(os.listdir()))

    input_file = open("quotation.txt", "r")

    # You can use `read()` to read the whole file into a single string
    content = input_file.read()
    print(content)


def write_quote():
    os.chdir("text_files")
    output_file = open("my_quotation.txt", "w")

    # You can use `write()` to write a single string
    print("I love Python!", file=output_file)
    print("(Matthew Poole)", file=output_file)

    # Or write both lines in one go separated by a newline character ('\n')
    # content = "I love Python!\n(Matthew Poole)"
    # output_file.write(content)


# Solutions below:

def personal_greeting():
    user_input = input("What is your name: ")
    print(f"Hello {user_input}, nice to see you!")


def formal_name():
    name1 = input("Enter your first name: ")
    name2 = input("Enter your last name: ")
    print(f"{name1[0]}. {name2}.")

def kilos_to_ounces():
    kilos = float(input("Enter a weight in kilograms: "))
    ounces = 35.274 * kilos
    print (f"{round(kilos, 2)} kilos is equal to {round(ounces, 2)} ounces")

def generate_email():
    name1 = input("Enter your first name: ").lower()
    name2 = input("Enter your last name: ").lower()
    year = input("What year did you enter university: ")
    email = (f"{name2[:4]}.{name1[0]}.{year[-2:]}@myport.ac.uk")
    print(email)

def grade_test():
    mark_scheme = "FFFFCCBBAAA"
    user_input = int(input("Enter the mark: "))
    print(mark_scheme[user_input])

def graphic_letters():
    win = Window()
    word = input("Enter a word: ")

    for i in range(len(word)):
        pos = win.get_mouse()
        message = Text(pos, word[i])
        message.size(20)
        message.draw(win)

    win.close()

graphic_letters()