l = [1,5,2,6,-1,0]

for i in range(len(l)):
    for j in range(len(l)-1):
        if l[j] < l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]
print(l)


