
#IP add based on RID

with open('log.html','r') as fh:
    str1 = fh.read()
    str1 = str1.split('\n')
    print(str1)
    dict_ = {}
    first = 1
    last = 2
    for i in range(0,len(str1)//4):
        print(i,type(str1[first]),type(str1[last]))
        dict_[str1[first]] = str1[last]
        first += 4
        last +=4
    print(dict_)











