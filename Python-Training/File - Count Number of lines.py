def count():
    count_ = 0
    with open('VLAN_File.txt','r') as fh:
        l = fh.readlines()
        print('Number of lines: {}'.format(len(l)))
        for i in l:
            if i[0] == 'v' or i[0] == 'V':
                count_ += 1
        print('Number of lines starting with v or V : {}'.format(count_))
        fh.close()
count()