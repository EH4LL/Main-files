import os
from graphix import Window, Point, Circle, Line, Rectangle, \
                    Polygon, Text, Entry
import math


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
        message.size = 30
        message.draw(win)

    win.close()

def sing_a_song():
    song = ""
    word = input("Enter the song's word: ")
    line = int(input("How many lines should the song be? "))
    repeat = int(input("How many times should the word be repeated? "))

    for i in range(repeat):
        song += word + " "
    for j in range(line):
        print(song)

def exchange_table():
    print("Euros    Pounds")
    for i in range(21):
        print(f"{i}         {round(i*1.17,2)}")

def make_initialism():
    user_input = input("Enter a phrase: ")
    words = user_input.split()

    result = ""
    for i in range(len(words)):
        result += words[i][0].upper()
    print(result)

def file_in_caps():
    file = open("quotation.txt","r")
    for line in file:
        print (line.upper())
    file.close()

def total_spending():
    total = 0
    file = open("spending.txt","r")
    for line in file:
        total += float(line)
    print(total)
    file.close()

def name_to_number():
    user_input = input("Enter your name: ")
    total = 0
    for x in range(len(user_input)):
        total += ord(user_input[x].lower()) - 96
    print(total)

def rainfall_chart():
    file = open("rainfall.txt","r")
    for line in file:
        data = line.split()
        asterisk = "*" * int(data[1])
        print(f"{data[0]} {asterisk}")
    file.close()

def rainfall_graphics():
    win = Window()
    file = open("rainfall.txt","r")
    counter = 0

    for line in file:
        data = line.split()
        city = Text(Point(50,20+counter),data[0])
        city.draw(win)
        bars = Rectangle(Point(100,15+counter),Point(100+5*int(data[1]),25+counter))
        bars.fill_colour = "blue"
        bars.draw(win)

        counter += 20
    
    file.close()
    win.get_mouse()
    win.close()

def rainfall_in_inches():
    file1 = open("rainfall.txt","r")
    file2 = open("rainfallInches.txt","w")
    data2 = ""
    for line in file1:
        data1 = line.split()
        city = data1[0]
        rainInch = round(int(data1[1]) * 25.4,2)
        data2 = data2 + city +" "+str(rainInch) + "\n"
    
    file2.write(data2)
    file1.close()
    file2.close()

def wc():
    user_input = input("Enter the file name: ")
    file = open(user_input,"r")

    charC = 0
    wordC = 0
    lineC = 0

    for line in file:
        lineC += 1
        text = line.split()
        wordC += len(text)
        for i in range(len(text)):
            charC += len(text[i])
    
    print(f"Lines: {lineC}\nWords: {wordC}\nCharacters: {charC}")
    file.close()