from queue import PriorityQueue


def main():
    a=input('Enter 1st Number')
    b=input('Enter 2nd Number')
    if float(b)==0:
        print('Divide by Zero Error')
    else:
        print(float(a)/float(b))
print('Find Divide By Zero Error')
main()