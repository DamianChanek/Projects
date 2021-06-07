'''Guess the number game'''

# import random module to generate a random integer for the game #
import random

# import color modules #
from termcolor import colored as color

# welcome message #
print(color("Welcome to my guessing game!"
      '\n\nThe goal is to guess a number between 0 and 100 in the least amount of tries possible.'
      "\nAfter each guess you'll receive an advice that will put you on the right track."
      "\n\nIf you'd like to quit the game, enter 'q'."
      "\n\nGood luck!", 'magenta',attrs=['bold']))

# create a variable for the count of tries the player enters #
count = 0

# get the first random number the player has to guess #
guess = random.randint(0, 100)

# game loop #
while True:
    # check for value error (player input is not an integer) #
    try:
        answer = input(color("\nGuess: ", 'magenta'))
        # check exit condition #
        if answer == 'q':
            print(color('Thanks for playing!', 'magenta'))
            break
        else:
            answer = int(answer)
            
    # reset loop if value error #
    except ValueError:
        print(color('Invalid input - you must enter only a number between 0 and 100. Please try again.', 'red'))
        continue

    # count the player guess for a final result #
    count += 1

    # check if input is in range 0 - 100 #
    if answer not in range(0,101):
        print(color('You must enter a number between 0 and 100. Please try again.', 'red'))
        continue

    # check win condition, if yes - reset loop, reset count, generate a new answer #
    if answer == guess:
        if count == 1:
            print(color("Hole in one, nice! If you were planning on doing something risky today,"
                  " this may just be your lucky day.", 'green', attrs = ['bold']))
        else:
            print(color("Congratulations, you've won! It took you " + str(count) +
                " tries to guess the number. Try beating that score!", 'green', attrs = ['bold']))
            count = 0
            guess = random.randint(0, 100)
            continue

    # prompts to guide the player to the answer #
    elif abs(answer - guess) < 5:
        print(color("You're very close!", 'magenta'))

    if answer > guess:
        print(color('Lower...', 'magenta'))

    if answer < guess:
        print(color('Higher...', 'magenta'))
