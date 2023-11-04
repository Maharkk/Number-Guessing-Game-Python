'''
Welcome to the Number Guessing Game! 
In this game, you'll have the exciting task of guessing the mystery number between 1 and 100. 
Test your luck, intuition, and number-guessing skills as you aim to beat the existing high score. 
With every guess, you'll receive hints to help guide you to the correct number. 
Are you ready to take on the challenge? 
Let's start guessing!
"'''

import random

# Generate a random number between 1 and 100
randNumber = random.randint(1, 100)

userGuess = None
guesses = 0

# Read the current high score from file
with open("hiscore.txt", "r") as f:
    hiscore = int(f.read())
    print("Current High Score:", hiscore)

# Ask the user to guess the number
while userGuess != randNumber:
    userGuess = int(input("Enter your guess: "))
    guesses += 1

    # Check the user's guess against the random number
    if userGuess == randNumber:
        print("You guessed it right!")
    else:
        if userGuess > randNumber:
            print("You guessed it wrong! Enter a smaller number")
        else:
            print("You guessed it wrong! Enter a larger number")

# Display the number of guesses made by the user
print(f"You guessed the number in {guesses} guesses")

# Update the high score if the current guesses are less than the existing high score
if guesses < hiscore:
    print("You have just broken the high score!")
    # Write the new high score to the file
    with open("hiscore.txt", "w") as f:
        f.write(str(guesses))
