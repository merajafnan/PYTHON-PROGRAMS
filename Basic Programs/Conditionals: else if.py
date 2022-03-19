def main():
    a=input('Enter 1st Number: ')
    b=input('Enter 2nd Number: ')
    if int(a)==int(b):
        print('Numbers are Equal')
    else:
        if int(a)>int(b):
            print('1st Number is Greater')
        else:
            print('2nd Number is Greater')
print('Find the greater of two numbers')
main()