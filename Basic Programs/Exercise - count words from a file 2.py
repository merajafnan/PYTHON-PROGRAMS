
a = []
b = []
with open('sample_file.txt','r') as fh:
    for i in fh:
        a.append(i)
b = ' '.join(a) #Create a string
b = b.replace('\n','')
b = b.replace('\\','')
b = b.split(' ') # create a List
print(b)

m = []
n = []

for i in b:
    if i in m:
        ind = m.index(i)
        n[ind] = n[ind] + 1
    else:
        m.append(i)
        n.append(1)
for j in range(len(m)):
    print('{} : {} '.format(m[j],n[j]))
