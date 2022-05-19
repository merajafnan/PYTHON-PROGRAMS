n = int(input("Enter ypur value : "))
row, col, i, j, k = n, n, 0, 0, 1
for i in range(row):
    for j in range(col):
        if (k == 1):
            print("B",end='')
        else:
            print("W",end='')
        k = k * -1
    k = k * -1
    print("")


