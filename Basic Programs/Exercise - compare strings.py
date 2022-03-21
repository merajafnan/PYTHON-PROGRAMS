# Ask the user to enter two strings
# Then ask the user to select if she wants to compare them based on ASCII or based on their length
# Then tell us which one is bigger.

from importlib import import_module

a=input('Enter 1st String : ')
b=input('Enter 2nd String : ')
how=int(input('Press 1 for ASCII Comprision & Press 2 for Length Comparision'))
if how == 1:
    if a>b:
        a_ascii_gr = a
    else:
        a_ascii_gr = b
if how == 2:
    if len(a)>len(b):
        a_ascii_gr = a
    else:
        a_ascii_gr = a
print('Bigger Number is : ',a_ascii_gr)

