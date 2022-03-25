colour_ = ['red','blue','green','yellow']
print('Enter the digit that you want to use for colour')
for i in range(len(colour_)):
    print('{} {}'.format((i+1), colour_(i)))