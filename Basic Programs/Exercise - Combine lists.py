an = [] #name
av = [] #values
with open('a.txt','r') as fh:
    for i in fh:
        k,v = i.rstrip('\n').split('=')
        an.append(k)
        av.append(v)
print(an,av)
bn = [] #name
bv = [] #values
with open('b.txt','r') as fh:
    for i in fh:
        k,v = i.rstrip('\n').split('=')
        bn.append(k)
        bv.append(v)
print(bn,bv)

cn = []*10
cv = []*10

for i in an:
    if i in cn:
        ind = an.index(i)
        cv[ind] = cv[ind] + av[av.index(i)]
    else:
        cn.append(i)
        cv.append(av[av.index(i)])

for i in bn:
    if i in cv:
        ind = cv.index(i)
        cv[ind] = cv[ind] + bv[bv.index[i]]
    else:
        cn.append(i)
        cv.append(bv[bv.index[i]])

print('Vegetable {} Occurance {}'.format(cn,cv))



