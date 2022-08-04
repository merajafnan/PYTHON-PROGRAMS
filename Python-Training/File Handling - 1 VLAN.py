with open('VLAN_File.txt','r') as fh:
    read_file = fh.readlines()
    read_file.pop(0)
    read_file.pop(0)
    read_file.pop(0)
    vlan_status = {'VLAN ID':'Status'}
    for i in read_file:
        j= i.split()
        vlan_status[j[0]] = j[2]
    print(vlan_status)
