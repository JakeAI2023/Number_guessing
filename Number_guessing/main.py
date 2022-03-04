#Number Guessing game
import random

guess = 0
guesses = 0
random_number = random.randint(0, 50)

while True:
    guess = int(input("Enter a number between 0 and 50: "))
    if guess < random_number:
        print("Try again pick higher: ")
        guesses+= 1
    if guess > random_number:
        print("Try again pick lower: ")
        guesses+= 1
    if guess == random_number:
        print("You got the Number Right Good JOB!!! It Took you " + str(guesses) + " guesses")
        break