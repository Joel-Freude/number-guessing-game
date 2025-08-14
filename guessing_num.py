import random
import time

attempts = 0

print("Welcome to my number guessing game!")
input("Press any key to start playing ")

number1 = random.randint(0, 10)

while True:
    guess = int(input("Guess a random number between 0 and 10. "))
    attempts += 1

    if guess == number1:
        playAgain = input(f"Correct! The secret number was indeed {number1}, and you guessed it in {attempts} attempts. Play again? (yes/no) ")
        if playAgain == "yes":
            attempts = 0
            number1 = random.randint(0, 10)
        else:
            break
    elif guess > number1:
        print("Try a smaller number.")
    else:
        print("Try a bigger number.")