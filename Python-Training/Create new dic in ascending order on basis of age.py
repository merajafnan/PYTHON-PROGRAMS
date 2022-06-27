str= "jhon is 34 , Mojo is 30 , Tom is 18 , Rambo is 33 and Jhonny is 31"

#Split String in list
str = str.split()
print(str)

# remove extra items
for i in str:
    if i == 'is' or i == ',' or i == 'and':
        str.remove(i)
print(str)

#create dictionary
new_dic = {}                            # 'Jhon': 34, 'Mojo': 30
for i in range(0,len(str),2):
    new_dic[str[i]] = int(str[i+1])
print(new_dic)

# Arrange Dic in Ascending order
sorted_dic = {}
for i in sorted(new_dic,key=new_dic.get):
    sorted_dic[i] = new_dic[i]
print(sorted_dic)
