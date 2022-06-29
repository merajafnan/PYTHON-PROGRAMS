str = input("Enter your word >=3 digits: \n")
length = len(str)
if length >= 3:
    m = length // 2
    print(str[m-1]+str[m]+str[m+1])
else:
    print("wrong input")

