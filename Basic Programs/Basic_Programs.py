print ("Rockstar")

a = 'Galaxy'
print (a)

print('\nVariable type')
print (type(23))
print (type(2.3))
print (type('23'))
print (type("23"))
print (type(True))
print (type(False))
print (type(None))
print (type([]))
print (type({}))

print('\nFloating numbers 0.1 0.2')
print (0.1+0.2)

print("\nArea of Rectangle 4 3.6")
a=4
b=3.6
print('area=',a*b)

print('\nMultiply String')
a='32'
b='23'
#print(a*b) 
#TypeError: can't multiply sequence by non-int of type 'str'

print('\nAdd String 32 + 23')
print(a+b)

print('\nArea & Circumference of Rectangle and Circle Rad=2.5 L=4 B=5')
Rad=7 
L=4 
B=5
print('Area of Rectangle=',L*B)
print('Circumference of Rectangle=',2*(L+B))
print('Area of Circle=',3.14*Rad*Rad)
print('Circumference of Circle=',2*Rad*3.14)

print('\nArea & Circumference Circle using Math function')
from cgi import print_arguments
from http.server import executable
import imp
import math
from operator import indexOf, length_hint

from attr import define
print('Area of Circle=',3.14*math.pi)
print('Circumference of Circle=',2*Rad*math.pi)

import sys
print('\nModules')
print(sys.executable)
print(sys.platform)
print(sys.argv[0])
print(sys.version_info.major)
print(sys.getsizeof(1))
print(sys.getsizeof(12))
print(sys.getsizeof(1.0))
print(sys.getsizeof(''))
print(sys.getsizeof(""))
print(sys.getsizeof("a"))
print(sys.getsizeof('a'))
print(sys.getsizeof('ab'))
print(sys.getsizeof('abc'))

print('\nUse Of Functions')
def main():
    print('Rockstar')
    print('Galaxy')
print('Before')
main()
print('After')

print('\n')
def main():
    print('Conditional Rockstar')
    print('Conditionla Galaxy')
if __name__ == "__main__":
    main()

print('\nNo newline, but a space is added at the end of the output and between values.')
import sys
sys.stdout.write('Rockstar')
sys.stdout.write('Galaxy')
print('\n')

print('\nNo newline, Alternate method')
print('Rockstar',end='')
#print('Rockstar',end='','dj',end='')   #SyntaxError: positional argument follows keyword argument
print('Galaxy')
print('Dinsours',end=' ')
print('Eggs')

print('\nNo newline, set the character separating values')
print('Rockstar','Galaxy','Dinosour','Egg',sep='')

#print in Python 2 as if it was Python 3
#from __future__ import print_function

print('\nTernary operator')
a=6
answer='positive' if a>0 else 'negative'
print(answer)

print('\nPseudo Random Number')
import random
a=random.random() # a value between 0.0 <= < 1.0
print(a)
print(random.random())

print('\nFixed Random Number')
b=random.seed(19)
print(random.random())
c=random.seed(19)
print(random.random())

print('\nRolling dice - randrange')
print(1+int(6*random.random()))
print(random.randrange(1,7))

print('\nRandom choice')
a='abchdjdkdodjsns'
b=['apple','banana','watermelon','muskmelon']
print(random.choice(a))
print(random.choice(b))

a=random.random
y=a()
print(a)
print(y)

print('\nTrue and False values in Python')
v=[None,0,"",False,[],(),{},"0",True,'a',1]
for i in v:
    if i:
        print('True value: ',i)
    else:
        print('False Value: ',i)

# def check_money():
#     return money > 1000000
# def check_salary():
#     salary += 1
#     return salary >= 1000
# while True:
#     has_good_money = check_money()
#     has_good_salary = check_salary()
#     if has_good_money or has_good_salary:
#         print("I can live well")

print('\nMultiple Strings with \ output same line')
a='abc' 'def' 'ghi'
print(a)
b='abc' \
  'def' \
  'ghi'
print(b)

print('\nTripple Coated Strings in output diffrent line')
a='''Rocstar
moving ahead
of the 
galaxy'''
print(a)

print('\nString repetition and concatenation')
a=2*'Rockstar'
print(a)
b='Rockstar'+'Galaxy'
print(b)
c='Dinosours'
print('-'*len(c))

print('\nCharacter in a string')
a='Rockstar of the Galaxy'
print(a[0],a[5],a[11],sep='    ')

print('\nString slice (instead of substr)')
a='Rockstar of the Galaxy'
print(a[1:4],a[:6],a[4:],sep='<--->')

# In Python strings are “immutable”, meaning you cannot change them. You can replace a whole string in avariable, but you cannot change it.

print('\nHow to change a string')
a='Rockstar of the Galaxy'
b=a[0:9]+'and the Biggest Hero '+a[9:]
print(b)

print('\nString functions and methods (len, upper, lower)')
a='rockstar'
b='GALAXY'
print(a.upper())
print(b.lower())
print(len(a))

print('\nindex in string')
a='Rockstar of the Galaxy'
print(a.index('x'))
print(a.index('of'))
print(a.index('a',3))
print(a.index('a',10))
print(a.index('of',4,16))

print('\nrindex in string / Last Occurance')
a='Rockstar of the Galaxy'
print(a.rindex('a'))

print('\n rfind,find,index,rindex')
print(a.rfind('a'))
print(a.rfind('z'))
print(a.find('a'))
print(a.find('z'))
print(a.index('a'))
print(a.rindex('a'))

print('\nin string')
a='Rockstar of the Galaxy'
if 'of' in a:
    print('Present')
else:
    print('not present')

print('\nindex if in string')
a='Rockstar of the Galaxy'
t='of'
if t in a:
    l=a.index(t)
    print(t+" is at "+str(l))

file = r'C:\Users\merhassa\sample.txt'
print(file)

print('\nFor Loop with Break')
a='Rockstar of the Galaxy'
for i in a:
    if i == " ":
        break
    print(i,end="")

print('\nFor Loop with Continue')
a='Rockstar of the Galaxy'
for i in a:
    if i == " ":
        continue
    print(i,end="")

print('\nWhile Loop')
import random
a=0
while a<=150:
    print(a)
    a += random.randrange(1,35)

# You can stop an infinite loop with CTRL + C 
# exit - will stop your program no matter where you call it.
# return - will return from a function (it will stop the specific function only)
# break - will stop the current “while” or “for” loop
# continue - will stop the current iteration of the current “while” or “for” loop









