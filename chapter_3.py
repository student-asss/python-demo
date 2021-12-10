# 3.1.
##import random
# num = random.randint(1,100)
# print(num)

# 3.2. - 3.3.
#password = input("Password: ")
#if(password == "yourPassword"):
#    print("Welcome")
#else:
#    print("Error password")

#3.4.
# Guess Number
#import random
#number = random.randint(1,100)

#while True:
    #num1 = int(input("Enter number: "))
    #if num1 == number:
      #  print("You guessed secret number.")
       # break
    #elif num1 < number:
      #  print("My number is greater than your number.")
    #elif num1 > number:
       # print("My number is lower than your number.")

#3.5.   
#import random
#number = random.randint(1,100)

#while True:
#    num = int(input("Enter number between 1 and 99: "))
#    if (num < 100 and num > 0):
#        if num == number:
#            print("Congratulations !!!!")
#            break
#        elif num < number:
#            print("My number is greater than your number.")
#        elif num > number:
#            print("My number is lower than your number.")
#        elif num == -1:
#            print("You gave up guessing!!!")
#            break
#        else:
#            print("The number is out of range!!!")
# input("\nPress thr enter to exit.")

#3.6.
#print("Welcome to the Fast Food Restaurant.")
#print("Select the Menu of your choice.", "\n")
#print("Chinese menu, option 1: ", "\n"
#      "Italian menu, option 2: ", "\n"
#      "French menu, option 3: ", "\n"
#      "Spanish menu, option 4: ", "\n"
#      "Japanese menu, option 5: \n")

#menu = input("Yours option: ")
#k = "1"
#i = "2"
#f = "3"
#s = "4"
#j = "5"
#if menu == k:
#    print("You have chosen Chinese menu.")
#elif menu == i:
#    print("You have chosen Italian menu.")
#elif menu == f:
#    print("You have chosen French menu.")
#elif menu == s:
#    print("You have chosen Spanish menu.")
#elif menu == j:
#    print("You have chosen Japanese menu.")
#else:
#    print("This option does not exist in the menu.")

#input("\nPress thr enter to exit.")

#3.7.
#print("Welcome to the Fast Food Restaurant.")
#print("Select the Menu of your choice.", "\n")
#print("Chinese menu, option 1: ", "\n"
#      "Italian menu, option 2: ", "\n"
#      "French menu, option 3: ", "\n"
#      "Spanish menu, option 4: ", "\n"
#      "Japanese menu, option 5: ", "\n"
#      "For Exit, option 0: ", "\n")

#while True:
#    menu = input("Your choice: ")
#    k = "1"
#    i = "2"
#    f = "3"
#    s = "4"
#    j = "5"
#    e = "0"
#    if menu == k:
#        print("You have chosen Chinese menu.")
#    elif menu == i:
#        print("You have chosen Italian menu.")
#    elif menu == f:
#        print("You have chosen French menu.")
#    elif menu == s:
#        print("You have chosen Spanish menu.")
#    elif menu == j:
#        print("You have chosen Japanese menu.")
#    elif menu == e:
#        print("Exit.")
#        break
#    else:
#        print("This option does not exist in the menu.")

#input("\nPress thr enter to exit.")

# 3.8. 
#n = int(input("N: "))
#counter = 1
#while(counter <= n):
#    print(counter)
#    counter += 1

# 3.9.
#n = int(input("N: "))
#counter = 1
#suma = 0
#while(counter <= n):
#    suma += counter
#    counter += 1
#print(suma)

# 3.10.
#import random
#option1 = "Message 1"
#option2 = "Message 2"
#option3 = "Message 3"
#option4 = "Message 4"
#option5 = "Message 5"

#message = ""

#option = random.randint(1, 5)
#if (option == 1):
#    message = option1
#elif (option == 2):
#    message = option2
#elif (option == 3):
#    message = option3
#elif (option == 4):
#    message = option4
#elif (option == 5):
#    message = option5
#print(message)

#3.11.
#import random
#counter = 0
#while counter < 100:
#    option = random.randint(1,2)
#    if(option == 1):
#        print("Head")
#    elif(option == 2):
#        print("Letter")
#    counter += 1

# 3.12.
#import random
#counter = 0
#head = 0
#letter = 0
#while counter < 100:
#    option = random.randint(1,2)
#    if(option == 1):
#        head += 1
#        print("Head")
#    elif(option == 2):
#        letter += 1
#        print("Letter")
#    counter += 1
#print("Head: ", head, "Letter: ", letter)

#3.13.
#import random
#broj = random.randint(1,100)
#counter = 0
#User have 10 times guesses
#while counter < 10:
    #Enter number
#    guess = int(input("Broj: "))
#    if(guess < 100 and guess > 0):
#       if(guess == number):
#           print("Congratulations you guessed the number !!!")
#           break
#       else:
#           print("Unfortunately , you didn't guess the number.")
#       counter += 1
       #Guess left
#       print("You have: ", 10 - counter, " guesses left.")
    # 
#    elif(guess == -1):
#        print("You gave up guesses.")
#        break
#    else:
#        print("The number is out of range.")

# 3.14.
#import random

#number = int(input("number: "))
#counter = 0

#while counter < 10:
#    guess = random.randint(1,100)
#    if(number < 100 and number > 0):
#        if(number == guess):
#            print("Congratulations !!!", guess)
#            break
#        else:
#            print("Unfortunately , you didn't guess the number.", guess)
#        counter += 1
#        print("You have: ", 10-counter, "guesses left.")
#    elif(number == -1):
#        print("You gave up guesses.")
#        break
#    else:
#        print("The number is out of range.")
        
#print("\nPress the enter to exit.")

# 3.16.
#import random

#from = int(input("From: "))
#toThe = int(input("To the: "))
#attemptNumber  = int(input("Number of guesses: "))

#while True:
#    number = int(input("Number: "))
#    if(number < toThe and number > from):
#        break
#    else:
#        print("The number is out of range, please try again.")
#counter = 0
#while counter < attemptNumber :
#    try = random.randint(from, toThe)
#    if(try == number):
#        print("The computer successfully guessed the number.", try)
#        break
#    else:
#        print("Wrong computer attempt.", try)
#    counter += 1

# 3.17.
while True:
    print("\n\tSimple Calculator", "\n")
    print("Your option: ", "\n")
    print("Addition:  1", "\n"
          "Subtraction: 2", "\n"
          "Multiplication:   3", "\n"
          "Division:    4", "\n"
          "Exit: 0", "\n")
    op = int(input("Your option: "))
    if(op) == 0:
        print("You have chosen exit.")
        break
    else:
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))

        if(op) == 1:
            print(num1, "+", num2, "=", num1 + num2)
        elif(op) == 2:
            print(num1, "-", num2, "=", num1 - num2)
        elif(op) == 3:
            print(num1, "*", num2, "=", num1 * num2)
        elif(op) == 4:
            print(num1, "/", num2, "=", num1 / num2)  
        else:
            print("This option does not exist.")
        
        






    
