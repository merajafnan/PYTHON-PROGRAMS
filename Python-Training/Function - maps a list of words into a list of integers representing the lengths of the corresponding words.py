def CountWords(str):
    dic = {}
    str = str.split()
    for i in str:
        if i not in dic:
            dic[i] = len(i)
    return(dic)

str = input("Enter the String \n")
str = CountWords(str)
print(str)

# Output:
#
# Enter the String
# test cases
# {'test': 4, 'cases': 5}