from pprint import pprint


num = int(input('Enter your number'))
z = 0
for i in range(2,num):
    if (num % i) == 0:
        z = z + 1

if z == 0:
    print('Prime Number')
else:
    print('Not a Prime Number')