lst = ['p',3,4,1,"A",6,'A','B',8,8,"c",9,"D","E", "E", "AA", "aa", "aa"]
l1 = []
for i in lst:
    if i not in l1:
        l1.append(i)
dic = {}
for i in l1:
    dic[i] = lst.count(i)
print(dic)