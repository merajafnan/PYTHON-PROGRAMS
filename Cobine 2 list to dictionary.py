l1 = ['a','b','c','d']
l2 = ['1','2','3','4']

dic = {} # {'a':1,'b':'2',.....}
if len(l1) == len(l2):# Compare length between l1 & l2
    for i in range(len(l1)):
        dic[l1[i]] = l2[i]
    print(dic)
else:
    print("Length mismatch between l1 & l2")

# dic = dict(zip(l1,l2))
# print(dic)
