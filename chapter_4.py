# 4.1.
txt = input("Enter text: ")
for i in txt:
    print(i)

# 4.2.
n = int(input("N: "))
if(n < 0):
    print("n have to be greater than 0")
else:
    for i in range(n):
        print(i)
        print(i + 1)

# 4.3.
for i in range(0, 101, 5):
    print(i)

# 4.4.
n = int(input("N: "))
if(n < 0):
    print("N have to be greater than 0")
else:
    for i in range(n, -1, -1):
        print(i)

# 4.5.
num1 = int(input("First number "))
num2 = int(input("Second number: "))
step = int(input("Enter the step by which the count is performed: "))
for i in range(num1, num2, step):
    print(i)

# 4.6.
n = int(input("N: "))
sum = 0
for i in range(n + 1):
    sum += i
print(sum)

# 4.7.
while True:
    word = input("Enter word: ")
    if "a" in word:
        print("Your word contains the letter a")
    else:
        print("Your word does not contains the letter a")

# 4.8.
while True:
    word = input("Enter word: ")
    if(len(word) > 5):
        print(word[4])
    elif(len(word) > 0):
        print(word[0])
    else:
        print("Please, Enter word.")

# 4.9.
while True:
    word = input("Enter word: ")
    if(len(word) == 0):
        print("Please, Enter word.")
    else:
        for i in range(len(word) -1, -1, -1):
            print(word[i])

# 4.10.
while True:
    word = input("Enter word: ")
    if(len(word) == 0):
        print("Please, Enter word.")
    else:
        half = int(len(word) / 2)
        firstHalf = word[:half]
        secondHalf = word[half:]

        print("First Half: ", firstHalf)
        print("Second Half: ", secondHalf)

# 4.11.
while True:
    word = input("Enter word: ")
    if(len(word) == 0):
        print("Please, Enter word.")
    else:
        for i in range(len(word)):
            if(word[i] == "a"):
                print(i)

# 4.12.
nTorka = ()
while True:
    word = input("word: ")
    if(word != "end"):
        nTorka += (word,)
    else:
        break
print(nTorka)
