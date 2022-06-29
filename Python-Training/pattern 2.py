# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

r = int(input("Enter the Range: \n"))
for i in range(0,r):
    for j in range(0,i):
        print('*',end=" ")
    print('')
for i in range(r,0,-1):
    for j in range(i,0,-1):
        print('*',end=' ')
    print('')