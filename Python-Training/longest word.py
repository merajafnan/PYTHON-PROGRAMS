list = ['potato', 'tomato', 'apple', 'kiwi', 'avocado','lichi', 'pear', 'pineapple']

maxlen = len(list[0])
max = list[0]
for i in list:
    if(len(i) > maxlen):
        maxlen = len(i)
        max = i

print('Max item is: {} and length of max item is: {}'.format(max,maxlen))

