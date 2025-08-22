import random

def guess_number():
    userName = input("Enter your Name: ")
    print(f" Hello, {userName} Welcome to Guess the Number Game!")
    number = random.randint(1, 20)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 and 20: "))
            attempts += 1

            if guess < number:
                print(" Too low! Try again.")
            elif guess > number:
                print(" Too high! Try again.")
            else:
                print(f" Congratulations! Correct the number was {number}.") 
                print(f"  You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print(" Please enter a valid number.")

guess_number()
