import random
import time

print("""
************
Number Guessing Game

Guess a number between 1 and 40.
************
""")

random_number = random.randint(1, 40)
guesses = 5

while True:

    guess = int(input("Your guess is: "))

    if guess < random_number:
        print("Calculating..")
        time.sleep(1)
        print("Guess a higher number.")
        guesses -= 1
    elif guess > random_number:
        print("Calculating..")
        time.sleep(1)
        print("Guess a lower number.")
        guesses -= 1
    else:
        print("Calculating..")
        time.sleep(1)
        print("Congratulations, you guessed right! The right number was: ", random_number)
        print("You've beaten the game.")
        break

    if guesses == 0:
        print("You're out of guesses.")
        print("The right number was: ", random_number)
        break
