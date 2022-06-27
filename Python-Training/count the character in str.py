str = "abcccccdeegg"

# String to list
str = list(str)
print(str)

# Create Unique List
str_unique = []
dict = {}

for i in str:
    if i not in str_unique:
        str_unique.append(i)
print(str_unique)

# Create Dictionary
for i in str_unique:
    ind = str_unique.index(i)
    dict[str_unique[ind]] = str.count(i)
print(dict)