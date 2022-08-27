def divzero(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        print('\n!!!!!!division by zero error!!!!!\n')
    else:
        print('Division Result = {}'.format(result))
    finally:
        print('This is always executed')
divzero(2,3)
divzero(2,0)

# try:
#     if a > 2:
#         print('Correct')
# except NameError:
#     print('name < {} > is not defined'.format('a'))
# finally:
#     print('This is always executed')

