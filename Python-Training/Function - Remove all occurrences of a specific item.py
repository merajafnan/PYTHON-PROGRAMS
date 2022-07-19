def remove_(lst,item):
    k = 0
    lst = [i for i in lst if i != item]
    return lst

lst = ['test','boot','swim','test','test','test','test','find','test']
item = 'test'
remove_ = remove_(lst,item)
print("New list after removal of perticulat item : {}".format(remove_))

# Output:
#
# New list after removal of perticulat item : ['boot', 'swim', 'find']