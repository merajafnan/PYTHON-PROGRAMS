s = input("Enter Your String: \n")
s1 = s
z = []
for i in s1:
    if i.isalpha() or i.isnumeric() or i.isspace():
        z.append(i)
    else:
        z.append('#')
z = ''.join(z)
print("Original string: {}".format(s))
print("New string     : {}".format(z))

# Output:
# Enter Your String:
# /*Jon is @developer & musician!!
# Original string: /*Jon is @developer & musician!!
# New string     : ##Jon is #developer # musician##













