s = input("Enter your String: \n")
s = s.split()
z = []
for i in s:
    # z.append(i if i.isalnum() and not i.isalpha() and not i.isnumeric() else '')
    if i.isalnum() and not i.isalpha() and not i.isnumeric():
        z.append(i)
print(z)


# OP:
#
# Enter your String:
# Emma25 is Data scientist50 and AI Expert
# ['Emma25', '', '', 'scientist50', '', '', '']