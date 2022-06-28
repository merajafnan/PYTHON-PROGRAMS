r_start = int(input("Enter Start Range: "))
r_end = int(input("Enter End Range: "))
prime = []   # 29,31,37

for i in range(r_start,r_end+1):    # 25 to 50
    for j in range(2,i):   # 2 - 24 | 2 - 29
        if i % j == 0:
            break
    else:
        prime.append(i)
print(prime)
