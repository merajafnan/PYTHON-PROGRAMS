print("List of prime numbers from 1 to 100 :")
for n in range (1, 101):
    count = 0
    t = n//2
    for i in range(2, (t + 1)):
        if(n % i == 0):
            count = count + 1
            break
    if (count == 0 and n > 1):
        print(" %d" %n, end = '  ')

