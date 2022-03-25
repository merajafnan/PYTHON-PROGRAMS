# Given a list of numbers numbers = [1203, 1256, 312456, 98]
# count how many times each digit appears? The output will look like this:


# num_ = [1203, 1256, 312456, 98]
# temp_ = [0]*10
# for i in num_:
#     for j in list(str(i)):
#         temp_[int(j)] = temp_[int(j)]+1
# print(temp_)
# for z in range(len(temp_)):
#     print('{} {}'.format(z,temp_[z]))


num_ = [1203, 1256, 312456, 98]
num_ = list(''.join(map(str,num_)))
print(num_)

a = []
b = []

for i in num_:
    if i in a:
        index = a.index(i)
        b[index] = b[index]+1
    else:
        a.append(i)
        b.append(1)

for j in range(len(a)):
    print('{} {}'.format(a[j],b[j]))