def say_hello():
    print ("Hello World")
    
def say_bye():
    print ("Goodbye Mars")


# A simple kilograms to ounces conversion program
# It asks for a weight in kilograms (for example 10)
# and converts it to ounces (352.74)

def kilos_to_ounces():
    kilos = float(input("Enter a weight in kilograms: "))
    ounces = 35.274 * kilos
    print ("The weight in ounces is", ounces)

def count():
    for i in range(10):
        print ("Number is now: ", i)
        
def say_name():
    print ("Ethan")

def say_hello_2():
    print("hello")
    print("world")

def dollars_to_pounds():
    dollars = float(input("Enter an amount in dollars: "))
    pounds = dollars / 1.35
    print (pounds)

def sum_and_difference():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print (num1 + num2)
    difference1 = num1 - num2
    print (difference1)

def change_counter():
    onep = int(input("How many one pence coins do you have: "))
    twop = int(input("How many two pence coins do you have: "))
    fivep = int(input("How many five pence coins do you have: "))
    totalone = onep
    totaltwo = twop * 2
    totalfive = fivep * 5
    totalchange = totalone + totaltwo + totalfive
    print(totalchange)

def ten_hellos():
    for x in range(10):
        print("Hello World")
        
def zoom_zoom():
    number = int(input("Enter a number: "))
    for x in range(number):
        print ("zoom", x + 1)

def count_to():
    number = int(input("Enter a number: "))
    for x in range (1,number+1):
        print(x)

def count_from_to():
    num1= int(input("Enter the starting number: "))
    num2 = int(input("Enter the ending number: "))
    for x in range(num1,num2 + 1):
        print(x)

def weights_table():
    for x in range(1,11):
        print("Kilograms: " + str(x*10) +" | Ounces: " + str(x*352.74))

def future_value():
    invest = float(input("Enter the value of the investment: "))
    years = int(input("Enter the amount of years that it is to be invested: "))
    for i in range(years):
        invest = invest * 1.035
    print(invest)
    