def count_lower():
    count = 0
    with open('VLAN_File.txt','r') as fh:
        ln = fh.read()
        for i in ln:
            if i.islower():
                count += 1
        print('Count of lower case elements are : {}'.format(count))
count_lower()