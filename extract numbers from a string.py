str = 'hello 12 hi 89. Howdy 34'

# remove '.' from the string
str = list(str)
for i in str:
    if i == '.' in str:
        ind = str.index(i)
        str.pop(ind)
str = "".join(str)
print(str)

# extract number from the String
str = str.split()
digits = []
for i in str:
    if i.isdigit():
        digits.append(i)
print('Digits in String are: {}'.format(digits))

