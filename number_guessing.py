# guessing_game.py

import random

number = random.randint(1, 100)
attempts = 0

print("I'm thinking of a number between 1 and 100.")

while True:
    try:
        guess = int(input("Your guess: "))
    except ValueError:
        print("Please enter a whole number.")
        continue

    attempts += 1

    if guess < number:
        print("Too low")
    elif guess > number:
        print("Too high")
    else:
        print(f"Correct! You guessed the number in {attempts} attempt(s).")
        break
