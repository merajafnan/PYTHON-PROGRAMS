str = 'jump zoo zoo jump Taxi Aeroplane Taxi zoo'
str = str.split()
print("List with duplicate values: ",str)
new_str = []

for i in str: # remove duplicate items & append unique values in new_str
    if i not in new_str:
        new_str.append(i)
print("List with unique values: ",new_str)

for i in new_str:
    print('Frequency of', i, 'is :', str.count(i))

# for i in range(0, len(new_str)): # range(0 to 3)
#     print('Frequency of', new_str[i], 'is :', str.count(new_str[i])) # 'jump'