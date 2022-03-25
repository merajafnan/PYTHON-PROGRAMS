
from itertools import count


celestial_objects = ['Moon', 'Gas', 'Asteroid', 'Dwarf', 'Asteroid', 'Moon', 'Asteroid']

a = []
b=[]

for i in celestial_objects:
    if i in a:
        index = a.index(i)
        b[index] = b[index] +1
    else:
        a.append(i)
        b.append(1)

for z in range(len(a)):
    print('{} {}'.format(a[z],b[z]))
