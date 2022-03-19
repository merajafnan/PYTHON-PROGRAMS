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
from http.server import executable
import imp
import math

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











