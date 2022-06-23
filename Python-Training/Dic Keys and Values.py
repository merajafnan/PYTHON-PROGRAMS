d1 = {"a":1,"b":2,"c":3}
d2 = {"d":4,"e":5,"f":6}
d3 = d1 | d2
Keys = []
values = []

print("d3: ",d3)
for i in d3:
    Keys.append(i)
    values.append(d3[i])

print('Dictionary Keys: {}'.format(Keys))
print('Dictionary values: {}'.format(values))




