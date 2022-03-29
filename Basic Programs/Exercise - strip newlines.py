# How to read all the lines of a file into a list
# and remove trailing newlines?

a = []
with open('sample3.txt','r') as fh:
    for i in fh:
        a.append(i.rstrip('\n'))
print(a)