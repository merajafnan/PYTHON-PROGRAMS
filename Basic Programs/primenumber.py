num = 1

if num > 1:
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")

# n=int(input("Enter an integer:"))
# a=[]
# for i in range(2,n+1):
#     if(n%i==0):
#         a.append(i)
# a.sort()
# print("Smallest divisor is:",a[0])