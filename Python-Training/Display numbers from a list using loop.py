l = [12, 75, 150, 180, 145, 525, 50]
l_new = []
for i in l:
    if i > 500:
        break
    if i > 150:
        continue
    if i % 5 == 0:
        l_new.append(i)
print("New List with matching parameters: {}".format(l_new))

Write a program to display all prime numbers within a range