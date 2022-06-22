# program to print even elements of a list

list1=[11,12,18,16,13,19,22,36]

for i in list1: # i 11,12,18,16 ----- 36
    if i % 2 == 0:
        print('Even Element {}'.format(i))
    else:
        print('Odd Element {}'.format(i))