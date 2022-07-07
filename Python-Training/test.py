n1 = int(input("Enter Number"))
n2 = int(input("Enter Number"))
n3 = int(input("Enter Number"))

max = n1 # 30

if max < n2:
    max = n2
if max < n3:
    max = n3
print(max)