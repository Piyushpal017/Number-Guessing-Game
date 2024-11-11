import random

import art

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
numbers = random.randint(2, 99)


def decision(attempts):
    while attempts != 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        attempts -= 1
        guess = int(input("Make a guess : "))
        if attempts == 0:
            print("You've run out of guesses, you lose.")
        elif guess < numbers:
            print("Too low")
            print("Guess again.")
        elif guess > numbers:
            print("Too high")
            print("Guess again.")
        else:
            print(f"You got it! The answer was {numbers}")
            break


if difficulty == "easy":
    decision(10)
else:
    decision(5)
