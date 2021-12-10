# 7.1.

try:
    wholeNumber = int(input("Whole Number: "))
    realNumber = float(input("Real Number: "))
    print(wholeNumber, realNumber)
except:
    print("An error occurred while entering data!")

# 7.2.

# Print character-by-character content 
testFile = open("test.txt", "r")
while True:
    c = testFile.read(1)
    if c == "":
        break
    else:
        print(c)
print("--------------------------")
testFile.close()

# Print line-by-line content 
testFile = open("test.txt", "r")
for line in testFile:
    print(line, end="")
print("\n--------------------------")
testFile.close()

# Print text at once 
testFile = open("test.txt", "r")
print(testFile.read())
testFile.close()

# 7.3.

text = input("> ")
try:
    file = open("test.txt", "w")
    file.write(text)
except:
    print("Error!")

file.close()

# 7.4.

text = input("> ")
try:
    file = open("test.txt", "w")
    file.write(text)
except:
    print("Error!")

file.close()

file = open("test.txt", "r")
print(file.read())
file.close()

# 7.5.

try:
    file = open("test.txt", "r")
except:
    print("Error opening file!")

suma = 0
for i in file:
    try:
        number = int(i)
        suma += number
    except:
        print("Error converting text to number!")

print(suma)

# 7.6.

import pickle
lista = ["London", "New York", "Paris", "Beograd"]
file = open("cities.dat", "wb")
pickle.dump(lista, file)
file.close()

file = open("cities.dat", "rb")
l = pickle.load(file)
file.close()
print(l)






