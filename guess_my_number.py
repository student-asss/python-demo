# Guess My Number

import random

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")

# set the initial values
theNumber = random.randint(1, 100)
guess = int(input("Take a guess: "))
tries = 1

# guessing loop
while guess != theNumber:
    if guess > theNumber:
        print("Lower...")
    else:
        print("Higher...")

    guess = int(input("Take a guess: "))
    tries += 1

print("You guessed it! The number was", theNumber)
print("And it only took you", tries, "tries!\n")

input("\n\nPress the enter to exit.")



