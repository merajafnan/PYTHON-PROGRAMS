# Implement the MasterMind game.
# The computer “thinks” a number with 4 different digits.
# You guess which digits. For every digit that matched both
# in value, and in location the computer gives you a *. For every
# digit that matches in value, but not in space the computer gives
# you a +. Try to guess the given number in as few guesses as possible.

# Computer: 2153
# You: 2467 *
# You: 2715 *++

from errno import ENETRESET
import random
v=str(random.randrange(1000,9999))
print(v)
n = str(input('\nEnter 4 digit number '))
nv = list(map(int, n))
vv = list(map(int, v))
# print(guess)
# nv = n[:]
# vv = v[:]
k = '_'
if len(n) == 4:
    for i in range(0,len(v)):
        if nv[i] == vv[i]:
            print('*',end='')
            nv[i] = k
    for i in range(0,len(v)):
        for j in range(0,len(n)):
            if nv[i] == vv[j]:
                print('+',end='')
                nv[j] = k
else:
    print('Wrong Choice | Quiting the Program now ')





