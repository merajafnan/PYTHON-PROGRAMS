import re
str="""
switch01,te0/1,2378748485,8474857587
switch02,te0/2,2378748486,5474857187
switch03,te0/3,3378748485,9474857587
switch04,te0/4,4378748486,15474857187
"""

switch = re.findall(r'switch\d\d',str)
interface = re.findall(r'te\d/\d',str)
data_output = re.findall(r'(?<=te\d/\d,)..........',str)
# print(switch,'\n',interface,'\n',data_output)
op = {}
for i in switch:
    for j in interface:
        op[i] = j

z=0
for k,v in op.items():
    op[k] = {}
    op[k][v] = data_output[z]
    z = z + 1
print(op)
