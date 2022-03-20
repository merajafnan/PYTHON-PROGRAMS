# Using the random module the computer “thinks” about a whole number between 1 and 20.
# The user has to guess the number. After the user types in the guess the computer tells if this was bigger or smaller than the number it generated, or if was the same.
# The game ends after just one guess.

import random

def main():
    n=int(input('Enter a number between 1 to 20: '))
    x=random.randrange(1,21)
    if n==x:
        print('Correct Guess')
    elif n<x:
        print('Your Guess is less than & The number generated: ',x)
    else:
        print('Your Guess is greater than & The number generated: ',x)
print('Number Guessing Game')
main()
