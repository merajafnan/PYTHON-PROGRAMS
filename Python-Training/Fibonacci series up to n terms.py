r = int(input("Enter the range for Fibonacci Series: "))
fibo = [0,1]
s = 0
for i in range(0,r-2):
    s = fibo[i] + fibo[i+1]
    fibo.append(s)
print(fibo)
print(fibo)