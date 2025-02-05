import random

number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

if number == guess:
    print("You Won!")
else:
    print("You Lose!")

