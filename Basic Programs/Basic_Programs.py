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
import math
print('Area of Circle=',3.14*math.pi)
print('Circumference of Circle=',2*Rad*math.pi)


