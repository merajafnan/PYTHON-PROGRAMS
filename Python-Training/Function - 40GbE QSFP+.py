def dvc(device_list):
    device_element = {}
    for i in device_list:
        j = i.split()
        device_element[j[0]] = j[1]
    print("\nDevice element inside Function : ")
    print(device_element)

str = """
Bus info Device Class Description
============================================================
pci@0000:1d:00.0 eno5 network VIC Ethernet NIC
pci@0000:1d:00.1 eno6 network VIC Ethernet NIC
pci@0000:3b:00.0 eno1 network Ethernet Controller 10G X550T
pci@0000:3b:00.1 eno2 network Ethernet Controller 10G X550T
pci@0000:5e:00.0 enp94s0f0 network Ethernet Controller XL710 for 40GbE QSFP+
pci@0000:5e:00.1 enp94s0f1 network Ethernet Controller XL710 for 40GbE QSFP+
pci@0000:5e:02.0 network Illegal Vendor ID
pci@0000:5e:02.1 network Illegal Vendor ID
pci@0000:5e:0a.0 enp94s10 network Illegal Vendor ID
pci@0000:5e:0a.1 enp94s10f1 network Illegal Vendor ID
pci@0000:d8:00.0 enp216s0f0 network Ethernet Controller XL710 for 40GbE QSFP+
pci@0000:d8:00.1 enp216s0f1 network Ethernet Controller XL710 for 40GbE QSFP+
pci@0000:d8:02.0 network Illegal Vendor ID
pci@0000:d8:02.1 network Illegal Vendor ID
pci@0000:d8:0a.0 enp216s10 network Illegal Vendor ID
pci@0000:d8:0a.1 enp216s10f1 network Illegal Vendor ID
vnet0 network Ethernet interface
vnet3 network Ethernet interface
virbr0-nic network Ethernet interface
kvm-monitoring network Ethernet interface
vnet2 network Ethernet interface
virbr0 network Ethernet interface
ex4000 network Ethernet interface
vnet1 network Ethernet interface
"""
str = str.split('\n')
str.pop(0)
str.pop(0)
str.pop(0)
str.pop(-1)
# print(str)
device_list = []
for i in str:
    j = i.split()
    # print(j)
    for k in j:
        if k == '40GbE':
            device_list.append(i)
print("\nDevice with 40GbE QSFP+")
print(device_list)
dvc(device_list)




