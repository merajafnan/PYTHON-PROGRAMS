def show_word_less_than_four_char():
    with open('VLAN_File.txt','r') as fh:
        ln = fh.readlines()
        print('Characters less than 4 digits')
        for i in ln:
            z = i.split()
            for j in z:
                if len(j) <= 4:
                    print('    ',j,end=' ')
show_word_less_than_four_char()
