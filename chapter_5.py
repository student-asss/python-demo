# 5.1.

list = [1, 2, 3, 4, 5, 6, "seven"]
print(list)
for i in list:
    print(i)

# 5.2.

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, "ten"]
n = len(list)
for i in range(0, n, 2):
    print(list[i])

# 5.3.

list = [1, 2, 3, 4, "five", 6, 7, "eight", 9]
n = len(list)
s = ""
for i in range(0, n, 2):
    s += str(list[i]) + " "

print(s)

# 5.4.

n = int(input("List size: "))
list = []
for i in range(n):
    index = input("Enter " + str(i) + ". index of list: ")
    list.append(index)
list1 = list[:int(n/2)]
list2 = list[int(n/2):]
print(list1)
print(list2)

# 5.5.

d1 = int(input("List size 1: "))
list1 = []
for i in range(d1):
    index = input("Enter " + str(i) + ". index of list: ")
    list1.append(index)

d2 = int(input("List size 2: "))
list2 = []
for i in range(d2):
    index = input("Enter " + str(i) + ". index of list: ")
    list2.append(index)

list = list1 + list2
print(list)

# 5.6.

list = []
print("""
        Select Option From Menu:
        
        1. New member: ,
        2. Delete member from list: ,
        3. Print list: ,
        0. Exit: 
""")
while True:
    option = int(input("Enter Option From Menu: "))
    if option == 1:
        member = input("New member: ")
        list.append(member)
    elif option == 2:
        n = input("Member of the List You Want to Delete: ")
        list.remove(n)
    elif option == 3:
        print(list)
    else:
        break

# 5.7.

sequence = ["first", ("second", "third"), ["fourth", "fifth"]]
print(sequence)

# 5.8.

list = [1, 2, 3, 4, 5, 6]
copy = list
list.append(7)
print(list, copy)

# What happened?
# It's the same list, we don't copy the list to another memory location,
# we are just copying the address where the original list is located. 

# 5.9.

dictionary = {"cow": "milk", "tomato": "vegetable", "banana": "fruit"}
print(dictionary["banana"])

# 5.10.

dictionary = {"plum": "blue", "pomegranate": "red", "pea": "green"}

if "pomegranate1" in dictionary:
    print(dictionary["pomegranate1"])
else:
    print("The requested key is not in the dictionary.")

# 5.11.

import random

list = ["banana", "pomegranate", "limun", "apple", "kiwi", "plum"]
while len(list) > 0:
    n = random.randint(0, len(list)-1)
    print(list[n])
    list.remove(list[n])

# 5.12.

list = []
while True:
    entry = input("> ")
    if entry == "end":
        break
    else:
        broj = int(entry)
        list.append(broj)

max = list[0]
for i in list:
    if max < i:
        max = i
print(max)

min = list[0]
for i in list:
    if min > i:
        min = i
print(min)

sum = 0
for i in list:
    sum += i
print(sum/len(list))

# 5.13.

list = []
while True:
    entry = input("> ")
    if entry == "end":
        break
    else:
        broj = int(entry)
        list.append(number)
print(list)
list.sort()
print(list)

# 5.14.

list = []
while True:
    entry = input("> ")
    if entry == "end":
        break
    else:
        number = int(entry)
        list.append(number)
print(list)
n = len(list)
for i in range(n):
    for j in range(i+1, n):
        if list[i] > list[j]:
            list[i], list[j] = list[j], list[i]
print(list)

# 5.15.

import random

print("""
        *** Game Hanging ***
""")
word_list = ["banana", "plum", "pomegranate", "apple", "apricot", "mandarin",
             "peach", "strawberry", "watermelon", "limun", "cherry"]
while True:
    print("""

        Press "Enter" for a new game.
        Write "Exit" to exit the game.

""", end="")
    option = input("> ")
    if(option == "Exit"):
        break
    index_word = random.randint(0, len(word_list) -1)
    word = word_list[index_word]
    guessNumber = 5
    print("Word has " + str(len(word)) + " letters!")
    hitLetter = []
    for i in word:
        print("_ ", end="")
        hitLetter.append("_")
    print()

    while True:
        hit = False
        guess = input("Letter: ")

        for j in range(len(word)):
            if(word[j] == guess):
                hit = True

                hitLetter[j] = guess
        if(not hit):
            guessNumber -= 1
        endGame = True

        for j in hitLetter:
            if(j == "_"):
                endGame = False
            print(j, end=" ")
        print()

        if(endGame):
            print("Congratulations!!!")
            break
        elif(guessNumber == 0):
            print("Unfortunately you didn’t guess the word!!!")
            print("Word: " + word)
            break
        else:
            print("You have more: " + str(guessNumber) + " guesses!")
    












