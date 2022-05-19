'''
print vlan id which are up form below O/P:

Interface Secondary VLAN(Type) Status Reason
-------------------------------------------------------------------------------
Vlan1 -- down Administratively down
Vlan10 -- down VLAN/BD is down
Vlan139 -- up --
Vlan1001 -- up --
Vlan1101 -- down VLAN/BD is down
Vlan1102 -- down VLAN/BD is down

'''

import re
with open("vlan.txt","r") as f1:
    for line in f1:
        vlan = re.search(r"_______",line)
        print(vlan)