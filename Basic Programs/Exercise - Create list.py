# Given a list of strings with words separated by spaces,
# create a single list of all the words.


fruits = ['grape banana mango','nut orange peach','apple nut banana apple mango']
fruits = ' '.join(fruits)
print(fruits)
fruits = fruits.split()
print(fruits)

unique_fruits = []
for i in fruits:
    if i not in unique_fruits:
        unique_fruits.append(i)
print(unique_fruits)

# OR Using Sets

fruits_2 = ['grape', 'banana', 'mango', 'nut', 'orange', 'peach', 'apple', 'nut', 'banana', 'apple', 'mango']  
print(fruits_2)
print(sorted(set(fruits_2)))

