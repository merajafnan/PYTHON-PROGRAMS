print('Add numbers entered by the user')
def main():
    a=input('Enter 1st Number: ')
    b=input('Enter 2nd Number: ')
    print('Before Type Caste: ',a+b)
    print('After Type Caste: ',int(a)+float(b))   # Use Float as 'int' will give error if user with enter floating values
print('Enter 2 Nubers for Addition')
main()
