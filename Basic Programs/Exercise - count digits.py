# Given a list of numbers numbers = [1203, 1256, 312456, 98]
# count how many times each digit appears? The output will look like this:


num_ = [1203, 1256, 312456, 98]
temp_ = [0]*10
for i in num_:
    for j in list(str(i)):
        temp_[int(j)] = temp_[int(j)]+1
print(temp_)
for z in range(len(temp_)):
    print('{} {}'.format(z,temp_[z]))
