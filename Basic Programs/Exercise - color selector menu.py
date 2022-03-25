# In a script have a list of colors. Write a script that will display a menu (a list of numbers and the
# corresponding color) and prompts the user for a number. The user needs to type in one of the
# numbers. That’s the selected color.
    # 1. blue
    # 2. green
    # 3. yellow
    # 4. white
# For extra credit make sure the system is user-proof and it won’t blow up on various incorrect input
# values. (e.g Floating point number. Number that is out of range, non-number)
# For more credit allow the user to supply the number of the color on the command line. python
# color.py 3. If that is available, don’t prompt.
# For further credit allow the user to provide the name of the color on the command line: python
# color.py yellow Can you handle color names that are not in the expected case (e.g. YelloW)?
# Any more ideas for improvement?



colour_ = ['red','blue','green','yellow']
print('Enter the digit that you want to use for colour')
for i in range(len(colour_)):
    print('{} {}'.format((i+1), colour_[i]))
user_inp = input()
if not user_inp.isdecimal():
    print('Number must be decimal')
    exit
elif int(user_inp) < 1 or int(user_inp) > len(colour_):
    print('Number must be in range 1 - 4')
    exit
else:
    col = int(user_inp)-1
    print(colour_[col])