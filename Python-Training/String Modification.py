str1 = 'jump zoo zoo jump Taxi Aeroplane Taxi zoo'
str2 = 'fly up till next universe'

# Create string with only unique words
# add 'saturn' at end of str1
# add 'jupiter' after 'jump' of str1
# delete 'aeroplane' of str1
# merge Str1 & str2 string with '_'
# split after merging the string

# Create string with only unique words
str_list = str1.split()
str3 = []
for i in str_list:
    if i not in str3:
        str3.append(i)
print('New Unique String: {}'.format(str3))

# add 'saturn' at end of str1
str_list.append("Saturn")
str_string = " ".join(str_list)
print('<Saturn> added at the end of String: <{}>'.format(str1))

# add 'jupiter' after 'jump' of str1
ind = str_list.index('jump')
str_list.insert(ind+1,'Jupiter')
print('New item added after <jump>: {}'.format(str_list))

# delete 'aeroplane' of str1
ind = str_list.index('Aeroplane')
str_list.pop(ind)
print('<Aeroplane> removed from the list: {}'.format(str_list))

# merge Str1 & str2 string with '_'
str_list = " ".join(str_list)
str_merge = '_'.join([str_list,str2])
print('String after merge: <{}>'.format(str_merge))

print('Split String after merge: {}'.format(str_merge.split()))


