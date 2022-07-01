def cal(a,b):
    add = (a+b)
    sub = (a-b)
    return  add,sub

c=int(input("Enter 1st value: \n"))
d=int(input("Enter 2nd value: \n"))

add,sub = cal(c,d)

print(' Addition = {} \n Substraction = {}'.format(add,sub))


# Output:
# Enter 1st value:
# 30
# Enter 2nd value:
# 20
# Addition = 50
# Substraction = 10