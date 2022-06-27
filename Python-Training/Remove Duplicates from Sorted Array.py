nums = [1,2,2,3,4,5,5,6,6,7,8,8]
nums_new = []

for i in nums:
    if i not in nums_new:
        nums_new.append(i)
nums = [0]
nums = nums_new
print('length: {} \n nums: {}'.format(len(nums),nums))