# program to print the elements of a list on even position

list1=[11,12,18,16,13,19,22,36]  # [3,5,7,9]
print("Element in Even position is {}".format(list1[2::2]))

#############################################################

for i in range(1,len(list1)):  # i = 0  range (1 to 10)
    if i % 2 == 0: # 1,2,3,4,5-----10
        print('Element in Even position is {}'.format(list1[i]))
    else:
        print('Element in Odd position is {}'.format(list1[i]))


###################################################################

# a = "potato"
# print("This is a Vegitable: {}".format(a))