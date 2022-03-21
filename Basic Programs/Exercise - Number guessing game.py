# Using the random module the computer “thinks” about a whole number between 1 and 20.
# The user has to guess the number. After the user types in the guess the computer tells if this was bigger or smaller than the number it generated, or if was the same.
# The game ends after just one guess.
# Level 1 : 
# The user can guess several times. The game ends when the user guessed the right number.
# If the user hits ‘x’, we leave the game without guessing the number.
# If the user presses ‘s’, show the hidden value (cheat)
# Level 2:
# Soon we’ll have a level in which the hidden value changes after each guess. In oredr to make that mode easier to track and debug, first we would like to have a “debug mode”.
# If the user presses ‘d’ the game gets into “debug mode”: the system starts to show the current number to guess every time, just before asking the user for new input.
# Pressing ‘d’ again turns off debug mode. (It is a toggle each press on “d” changes the value to to the other possible value.)
# Level 3:
# The ‘m’ button is another toggle. It is called ‘move mode’. When it is ‘on’, the hidden number
# changes a little bit after every step (+/-2). Pressing ‘m’ again will turn this feature off.

from operator import mod
import random
debug = False
mode = False
def main():
    while True:
        global debug
        global mode
        r=random.randrange(1,21)
        n=input('Enter a number between 1 to 20: ')
        if mode:
            mr=random.randrange(-2,3)
            r=r+mr
        if debug:
            print('Debug Enabled | Last Secret Number was',r)
        if n=='m':
            print('Mode Activated')
            mode = not mode
            continue
        if n=='x':
            print('game ends')
            break
        if n=='i':
            print('Cheat Activated - Random Number is :  ',r)
            continue
        if n=='d':
            print('Debug Activated')
            debug = not debug
            continue
        nI=int(n)
        if nI==r:
            print('Correct Guess')
            break
        if nI<r:
            print('Your Guess is less than & The number generated: ')
        else:
            print('Your Guess is greater than & The number generated: ')
print('Number Guessing Game')
main()
