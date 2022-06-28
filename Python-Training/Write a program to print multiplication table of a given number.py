n = int(input("Enter the number to Print table: "))
r = int(input("Enter the Range : "))
if n == 0 or r == 0:
    print("Wrong Input")
else:
    for i in range (1,r+1):
        print("{} X {} = {}".format(n,i,n*i))