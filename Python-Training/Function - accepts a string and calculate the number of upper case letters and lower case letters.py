def CountCases(str):
    uc,lc = 0,0

    for i in str:
        if i.isupper():
            uc += 1
        if i.islower():
            lc += 1
    return uc,lc

str = input("enter the string \n")
uc,lc = CountCases(str)
print(" Upper Case: {} \n Lower Case: {}".format(uc,lc))


# Output:
#
# enter the string
# Capgemini Engineering
# Upper Case: 2
# Lower Case: 18