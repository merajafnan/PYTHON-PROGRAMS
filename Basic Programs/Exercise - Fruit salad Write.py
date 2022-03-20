# Write a script that will pick 3 fruits from a list of fruits like the one we had in one of the earlierslides. Print the 3 names.
# Could you make sure the 3 fruits are different?


import random
fruits = ["Apple", "Banana", "Peach", "Orange", "Durian", "Papaya"]
print(random.sample(fruits,3))