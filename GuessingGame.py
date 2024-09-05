#Number Guessing Game
#Input
#User Guess
#Processing
#Loop while user guess is incorrect
#output
#message

import random
mynumber=random.randint(1,10)

#display welcome message
print("Welcome to the guess the number game!\n")
userGuesses = []
count = 1

#loop until correct guess
while True:
    try:
        guess = int(input("Please enter a number between 1 and 10: "))
    except ValueError:
        print("numbers only please!")
        continue
    userGuesses.append(guess)
    if (guess < mynumber):
        print("Too Low")
        count += 1
    elif (guess > mynumber):
        print("Too High")
        count += 1
    elif (guess == mynumber):
        print("You guessed it! It took you ",count," attempts")
        print("You picked the following numbers: ",userGuesses)
        break