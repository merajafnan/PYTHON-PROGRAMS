from tkinter import PROJECTING


a = {}
b = []
c = []
with open('candidate.txt','r') as fh:
    for i in fh:
        i=i.rstrip('\n')
        b.append(i)
c = b.pop(0)
print(c)
for j in b:
    z = ''.join(j)
    z = z.split(',')
    
    a['fname'] = z[0]
    a['lname'] = z[1]
    a['DOB'] = z[2]
print(a)
