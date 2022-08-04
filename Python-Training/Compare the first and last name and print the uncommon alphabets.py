first= input("Enter First Name: \n")
last= input("Enter last Name: \n")

first= list(first)
last= list(last)

uncommon_ele= []

for i in first:
    count = 0
    for j in last:
        if i == j:
            count += 1
    if count == 0:
        uncommon_ele.append(i)

for k in last:
    count = 0
    for l in first:
        if k == l:
            count += 1
    if count == 0:
        uncommon_ele.append(k)

print(uncommon_ele)

# OR use "not in "
