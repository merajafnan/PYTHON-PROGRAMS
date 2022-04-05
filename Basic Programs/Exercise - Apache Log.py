a = {}
with open('apachelog.txt','r') as fh:
    for i in fh:
        space = i.index(' ')
        ip = i[0:space]
        if ip in a:
            a[ip] = a[ip] + 1
        else:
            a[ip] = 1
for ip in a:
    print('{:16}:{:>6}'.format(ip,a[ip]))

