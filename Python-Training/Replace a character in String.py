#Replace 'a' in a string with 't'

str="axbctghn"
str=list(str)

for i in str:
    if i == 'a':
        ind = str.index(i)
        str[ind] = 't'
str = "".join(str)
print(str)