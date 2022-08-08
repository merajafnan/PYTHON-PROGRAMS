min = int(input("Enter the Starting range of Prime Number: "))
max = int(input("Enter the End range of Prime Number: "))

pr = [x for x in range(min,max+1) if all(x%y!=0 for y in range(2,x))]
print(pr)
