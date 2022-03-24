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
from cProfile import run
from cgi import print_arguments, print_form
from decimal import ROUND_CEILING
from http.server import executable
import imp
from inspect import stack
import math
from operator import indexOf, itemgetter, length_hint, truediv
from os import system
from sqlite3 import adapt
from time import monotonic, strftime
from tkinter.messagebox import YESNO
from turtle import st
from winreg import REG_OPTION_BACKUP_RESTORE

from attr import define
from sortedcontainers import SortedDict
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

print('\nFormatted printing')
a = 23
n = 'Rockstar'
print('Concat Basic - ' + 'Name = ' + n + ' Age = ' + str(a))
print('Concat Modulous - ' +'Name = %s and Age = %s' % (n,str(a)))
print('Concat F String - ' + f'Name = {n} and Age = {a}')
print('Concat Format - ' + 'Name = {} and Age = {}'.format(n,a))
print('Concat Format - ' + 'Name = {0} and Age = {1}'.format(n,a))
print('Concat Format - ' + 'Name = {1} and Age = {0}'.format(n,a))
print('Concat Format - ' + 'Name = {name} and Age = {age}'.format(age=a,name=n))


print('\nFormat columns')
l=[['Rockstar',1],
['Galaxy',12],
['Moon',123],
['Sun',1234567],
['Star',123456789]]

for i in l:
    print('{}{}'.format(i[0],i[1]))

print('_'*16)
for j in l:
    print("{:<8}|{:>7}".format(j[0],j[1]))

print('\nExamples using format - alignment')
a='Rockstar'
print('{}'.format(a))
print("'{:}'".format(a))
print("'{:^15}'".format(a))
print("'{:>15}'".format(a))
print("'{:<15}'".format(a))

print('\nFormat characters and types')
n = 97
print('Number :     {:n}'.format(n))
print('Binary :     {:b}'.format(n))
print('Character :     {:c}'.format(n))
print('Decimal :     {:d}'.format(n))
print('Octal :     {:o}'.format(n))
print('Hexa :     {:X}'.format(n))
print('hexa :     {:x}'.format(n))
print('Default to decimal :     {}'.format(n))

print('\nFormat floating point number')
n=34.567887695
print('exponent :       {:e}'.format(n))
print('Exponent :       {:e}'.format(n))
print('fixed point (Default Precision 6):       {:f}'.format(n))
print('Fixed Point (Default Precision 6) :       {:F}'.format(n))
print('Fixed Point (Precision set to 2) :       {:.2f}'.format(n))
print('generic (Default Precision Combined 6) :       {:g}'.format(n))
print('Generic (Default Precision Combined 6) :       {:G}'.format(n))
print('Number :       {:n}'.format(n))
print('Default :       {}'.format(n))


print('\nf-strings (formatted string literals)')
name='Meraj Hassan'
age=28.3
pi=3.141592653589793
r=2

print(f'The user {name} was born {age} years ago')
print(f'The user {name:20} was born {age} years ago')
print(f'The user {name:>20} was born {age} years ago')
print(f'The user {name:*^20} was born {age:#<20} years ago')

print(f'Pi is {pi:.3}')     # number of digits (defaults n = number)
print(f'Pi is {pi:.3f}')    # number of digits after decimal point

print(f"Area is '{pi*r**2}'")
print(f"Area is '{pi*r**2:.3f}'")

print('\nprintf using old % syntax \
It is recommended to use the format method! \
\nTo print { include {{. \
\nTo print } include }}.')

n=65
print('%s'%n)
print('a = {} b = {}'.format(2,3))
print('a = %d b = %d'% (2,3))
print('%10s'%n)
print('%c'%n)
print('%0.5d'%n)
print('{{}}'.format(n))
print('{{ {} }}'.format(n))
print('%{}'.format(n))

print('\nExamples using format with attributes of objects')
import sys
print('{0.executable}'.format(sys))
print('{system.argv[0]}'.format(system=sys))

print('\nraw f-strings')
n='Rockstar'
print(r'This is {n}')
print(f'This is {n}')
print(rf'This is {n}')
print(fr'This is {n}')  # this is better (for vim)

# LIST - Square Bracket
print('\nlists example 1')
l=['a',1,'Rockstar Galaxy',['Moon','Stars',99],
{a : ' \ Gardian of Galaxy 1 ', b : 'Gardian of Galaxy 2'}]
print(l)


print('\nlists example 2')
p=['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune','Pluto']
print(p)
print(p[0],p[1])
print(type(p[0]))
print(p[0:2])
print(p[2:4])
print(p[:])
print(p[:5])
print(p[5:])


print('\n List slice with steps \
    \n List slice with step: [start:end:step]')
n=['a','b','c','d','e','f','g','h','i','j','k','l']
print(n[::])
print(n[:1])
print(n[::1])
print(n[::2])
print(n[::3])
print(n[1::3])
print(n[1:5:2])
print(n[1:20:3])

print('\nChange the list')
x = ['abc', 'def', 'ghi', 'jkl']
y = 'Rockstar'
x[1]='mno'
print(x)
x[1:3]=['ijk','lmn','opq']
print(x)
x[1:3]=['rst']
print(x)
x[1:1]=['uvw','xyz']
print(x)
x[1]=['123','456']
print(x)
print(list(y))

print('\nChange with steps')
y=list('Rockstar')
y[1::2]=[0,0,0,0]
print(y)

print('\nShallow Copy')
y=list('Rockstar')
x=y
y[0:4]='Galaxy '
print(y)
print(x)

print('\nDeep Copy')
y=list('Rockstar')
x=y[:]
y[0:4]='Galaxy '
print(y)
print(x)

print('\nDeep Copy')
import copy
y=list('Rockstar')
x=copy.deepcopy(y)
y[0:4]='Galaxy '
print(y)
print(x)

print('\nJoin')
y=list('Rockstar')
j=':'.join(y)
print(j)

print('\njoin list of numbers & strings - Using map')
b=['G','A',2,3,'X','Y']
j=':'.join(map(str,b))
print(j)

print('\njoin list of numbers & strings - Using link commpression')
b=['G','A',2,3,'X','Y']
j=":".join(str(x) for x in b)
print(j)

print('\nSplit')
b='G:A:2:3:X:Y'
print(b.split(':'))
c='Rockstar of the Galaxy'
print(c.split())

print('\nin list')
c=['Rockstar','of','the','Galaxy']
if 'moon' in c:
    print('Item Found')
else:
    print('Item not found')

print('\nWhere is the element in the list')
c=['Rockstar','of','the','Galaxy']
print(c.index('the'))

print('\n.insert')
c=['Rockstar','of','the','Galaxy']
c.insert(3,'Moon')
print(c)
c.insert(len(c),'star')
print(c)

print('\nappend')
c=['Rockstar','of','the','Galaxy']
c.append("and the stars")
print(c)

print('\nremove')
c=['Rockstar','of','the','Galaxy','the']
c.remove('the')
print(c)

print('\nRemove element by index [].pop')
c=['Rockstar','of','the','Galaxy','the']
c.pop()
print(c)
c.pop(2)
print(c)

print('\nRemove several elements of list by index')
c=['Rockstar','of','the','Galaxy','the']
c[2:4]=[]
print(c)

print('\nUse list as a queue | FIFO Logic ') # FIFO Logic
a_queue = []
print(a_queue)
a_queue.append('Rockstar')
a_queue.append('of')
a_queue.append('the')
a_queue.append('Galaxy')
print(a_queue)
pop = a_queue.pop(2)
print(pop)
print(a_queue)

print('\nQueue using deque from collections | FIFO Logic')
from collections import deque
a_dqueue = deque(['Rockstar','of','the','Galaxy'])
print(a_dqueue)
a_dqueue.append('and Stars')
print(a_dqueue)
a_dqueue.popleft()
print(a_dqueue)

print('\nFixed size queue | FIFO Logic')
from collections import deque
a_dqueue = deque([],maxlen=3)
a_dqueue.append('Rockstar')
a_dqueue.append('of')
a_dqueue.append('the')
print(a_dqueue)
a_dqueue.append('Galaxy')
print(a_dqueue)


print('\nList as a stack | LIFO Logic')  # LIFO Logic
stack = []
print(stack)
stack.append('Rockstar')
stack.append('of')
stack.append('the')
stack.append('Galaxy')
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)

print('\nstack with deque')
dstack = deque([])
print(dstack)
dstack.append('Rockstar')
dstack.append('of')
dstack.append('the')
dstack.append('Galaxy')
print(dstack)
dstack.pop()
print(dstack)
dstack.pop()
print(dstack)


# SORTING

print('\nSorting & Reverse Sort')
planets = ['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune','Pluto']
print(planets)
planets.sort()
print(planets)
planets.sort(reverse=True)
print(planets)

print('\nReverse a number and name')
num = 1234567
name = 'Rockstar'
num = str(num)
num = list(num)
num.sort(reverse=True)
name = list(name)
name.sort(reverse=True)
print(num)
print(name)

print('\nReverse ignoring negative number')
num_list = [1,4,6,8,-1,-5,9,12,-11,16,-20]
num_list.sort()
print(num_list)
num_list.sort(reverse=True)
print(num_list)
num_list.sort(key=abs)
print(num_list)
num_list.sort(key=abs, reverse=True)
print(num_list)

print('\nsort mixed')
mixed_data = [1,'a',2,'c',9,'f',4,'d']
mixed_data_str = []
for i in mixed_data:
    mixed_data_str.append(str(i))
    continue
mixed_data_str.sort()
print(mixed_data_str)

print('\nKey Sort')
planets = ['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune','Pluto']
planets.sort(key=len)
print(planets)

print('\nSort tuples')
planets = [('Mercury','M',1),('Venus','V',2,6),('Earth',3,7),('Mars','M',4)]
print(sorted(planets)) # Sort by the first Element of each Tuple
print(sorted(planets, key=lambda s:s[2]))   # Sort by the 3rd Element of each Tuple
print(sorted(planets,key=itemgetter(2)))
print(planets)

# The sort() method will sort a list in-place and return None.
# The built-in sorted() function will return the sorted list and leave the original list intact

print('\nSorting Characters of String')
item = 'Rockstar'
l = sorted(item)
item_sorted = ''.join(l)
print(item_sorted)

# RANGE
print('\nRange')
for i in range(1,9,2):
    print(i,end='')

print('\nLooping over index')
item = ['Rokstar','Of','The','Galaxy',78]
for i in item:
    print(i,end=' ')
for j in range(len(item)):
    print(item[j],end=' ')



