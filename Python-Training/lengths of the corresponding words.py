str = "Rockstar of the Galaxy"
length = {}
str = str.split()
for i in str:
    count = 0
    for j in i:
        count +=1
    length[i] = count

print('Length of each Words: {}'.format(length))


