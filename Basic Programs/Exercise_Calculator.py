#Create a script that accepts 2 numbers and an operator (+, -, *, /), and prints the result of the operation.

# def main():
#         a=float(input('Enter the 1st Number: '))
#         b=float(input('Enter the 2nd Number: '))
#         op=input('Enter the Operand(+, -, *, /): ')
#         while 1:
#             if op=='+':
#                 print(a+b)
#             elif op=='-':
#                 print(a-b)
#             elif op=='*':
#                 print(a*b)
#             elif op=='/':
#                 print(a/b)
#             else:
#                 print('Wrong Choice | Try Again')
#             break
# print('Claculate (+, -, *, /)')
# main()


def main():
    a = float(input("Number: "))
    b = float(input("Number: "))
    op = input("Operator (+-*/): ")
    if op == '+':
        res = a+b
    elif op == '-':
        res = a-b
    elif op == '*':
        res = a*b
    elif op == '/':
        res = a/b
    else:
        print("Invalid operator: '{}'".format(op))
    # print(res)
    # return
main()
