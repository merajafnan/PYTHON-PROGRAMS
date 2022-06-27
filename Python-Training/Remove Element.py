nums = [2,4,3,2,2,3,2]
new_nums = []

for i in nums:
    if i != 2:
        new_nums.append(i)
print('length: {} \n num: {}'.format(len(new_nums),new_nums))