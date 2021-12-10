#!/usr/bin/python

def menu():
    print("""

        ~~~~~~~~~~~~~~~~~
        Options:
        1. Addition
        2. Subtraction
        3. Multiplication
        4. Dividing
        0. Exit
        ~~~~~~~~~~~~~~~~~

""")
    option = int(input("> "))
    return option

def addition():
    print("""

        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        You have selected option: Addition
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

""")
    s1 = int(input("First Number: "))
    s2 = int(input("Second Number: "))
    return s1 + s2

def subtraction():
    print("""

        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        You have selected option: Subtraction
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

""")
    s1 = int(input("First Number: "))
    s2 = int(input("Second Number: "))
    return s1 - s2

def multiplication():
    print("""

        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        You have selected option: Multiplication
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

""")
    s1 = int(input("First Number: "))
    s2 = int(input("Second Number: "))
    return s1 * s2

def dividing():
    print("""

        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        You have selected option: Dividing
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

""")
    s1 = float(input("First Number: "))
    s2 = float(input("Second Number: "))
    return s1 / s2

while True:
    option = menu()
    if option == 1:
        result = addition()
        print("Result: " + str(result))
    elif option == 2:
        result = subtraction()
        print("Result: " + str(result))
    elif option == 3:
        result = multiplication()
        print("Result: " + str(result))
    elif option == 4:
        result = dividing()
        print("Result: " + str(result))
    elif option == 0:
        break
    else:
        print("You have chosen a non-existent option !!!")
    
