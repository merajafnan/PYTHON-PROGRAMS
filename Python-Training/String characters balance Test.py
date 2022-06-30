 # s1,s2 = "Ynf","PYnative"
 # s1,s2 = "Ynz","PYnative"

s1 = input("Enter the Sub - String that need to be verified: \n")
s2 = input("Enter the String: \n")

k = [] # Y
for i in s1: # S1 = Y n z
    for j in s2: # s2 = PYnative
        if j == i and j not in k:
            k.append(j)
k = ''.join(k)
print('True' if k==s1 else 'False')

# Output:
#
#  Enter the String:
#  PYnative
#  Enter the Sub - String that need to be verified:
#  Ynz
#  False