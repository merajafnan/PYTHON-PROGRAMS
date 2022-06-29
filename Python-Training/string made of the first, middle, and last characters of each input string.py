s1 = input("Enter your 1st String: \n")
s2 = input("Enter your 2nd String: \n")

mid_s1 = len(s1) // 2
mid_s2 = len(s2) // 2

print(s1[0]+s2[0]+s1[mid_s1]+s2[mid_s2]+s1[len(s1)-1]+s2[len(s2)-1])

