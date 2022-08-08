l = [ 1,'b','c','A','D','Z','f',1,-1]

dig = []
char = []
z = 0
for i in l:
    z = str(i)
    if z.isalpha():
        char.append(i)
    else:
        dig.append(i)

for j in range(len(dig)):
    for k in range(len(dig)-1):
        if dig[k] > dig[k+1]:
            dig[k], dig[k+1] = dig[k+1], dig[k]
j, k = 0,0
for j in range(len(char)):
    for k in range(len(char)-1):
        if char[k] > char[k+1]:
            char[k], char[k+1] = char[k+1], char[k]

print(dig+char)

