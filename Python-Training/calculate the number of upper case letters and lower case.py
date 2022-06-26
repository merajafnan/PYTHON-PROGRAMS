str = input("Enter a String: \n")

upper = 0
lower = 0
digit = 0
space = 0
iden = 0
special = {'`','~','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[','}','}','|','\',''','<',',','>','.','?','/'}
for i in str:
    if i.isupper():
        upper += 1
    if i.islower():
        lower += 1
    if i.isdigit():
        digit += 1
    if i.isspace():
        space += 1
    if i in special:
        iden += 1
print('\n Upper: {} \n Lower: {} \n Digit: {} \n Space: {} \n Special_Characters: {} \n'.format(upper,lower,digit,space,iden))

