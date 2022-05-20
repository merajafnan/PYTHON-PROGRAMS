text = '''
This is a very long text.
OK, maybe it is not that long after all.
'''
a = []
b= []
text = text.replace('\n','')
text = text.replace(' ','')
for i in text:
    if i in a:
        ind = a.index(i)
        b[ind] = b[ind] + 1
    else:
        a.append(i)
        b.append(1)
for j in range(len(a)):
    print('{} : {}'.format(a[j],b[j]))
