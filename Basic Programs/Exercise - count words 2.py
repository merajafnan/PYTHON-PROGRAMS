words = ['Wombat', 'Rhino', 'Sloth', 'Tarantula', 'Sloth', 'Rhino', 'Sloth']
a = []
b = []

for i in words:
    if i in a:
        ind = a.index(i)
        b[ind] = b[ind] + 1
    else:
        a.append(i)
        b.append(1)
for j in range(len(a)):
    print('{} : {}'.format(a[j],b[j]))