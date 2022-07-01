def sum(n):
    while n:
        s = n + sum(n-1) # 10 + 9 + 8 + 7 + 6.....1
        return s
    else:
        return 0

num = int(input("Enter your number: \n"))
result = sum(num)
print(result)

