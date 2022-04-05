seq = "ACTNGTGCTYGATRGTAGCYXGTN"
c = {}
for i in seq:
    if i in c:
        c[i] = c[i] + 1
    else:
        c[i] = 1
s = len(seq)
print(s)
for j in c:
    print('{}   :   {}   :   {:.2f}'.format(j,c[j],((c[j]/24)*100)))