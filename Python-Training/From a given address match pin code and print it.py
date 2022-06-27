add = "Room 23, Kaddubishnahalli , Palm resort, HD/No 83400. Pin Code: 530068 station"

add = add.split()
print(add)
for i in add:
    length = len(i)
    if length == 6 and i.isdigit():  # pincode must be 6 digit and decimal
        pincode = i
        break
print("Pincode: {}".format(pincode))

