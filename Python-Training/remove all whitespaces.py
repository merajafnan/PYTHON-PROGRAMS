str = 'hello 12 hi 89. Howdy 34'

for i in str:
    if i == ' ':
        str = str.replace(' ','')
print('New String after replacing the Whitespace: <{}>'.format(str))