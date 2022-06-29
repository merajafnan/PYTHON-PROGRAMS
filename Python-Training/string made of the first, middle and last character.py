str1 = input("Enter the String: \n")

length = len(str1) # 9
m = length // 2  # int(length/2)
print(str1[0] + str1[m] + str1[length-1])