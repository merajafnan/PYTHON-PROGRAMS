dict = {'a': 1, 'b': 2, 'c': 3}
dict_new = {}
for i in dict:
    dict_new[dict[i]] =  i
print("Dictionary after interchanging keys with values: {}".format(dict_new))
