def result(N):
    for i in range(N):
        if i % 3 == 0 and i % 5 == 0:
            print(str(i) + " ", end = "")
        else:
            pass
if __name__ == "__main__":
    N = 100
    result(N)