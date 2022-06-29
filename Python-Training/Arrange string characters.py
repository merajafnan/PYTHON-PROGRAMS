s = input("Enter your string: \n")
print('Default String: <<{}>>'.format(s))
uc = []
lc = []
dc = []
sc = []
s_new = []

for i in s:
    if i.isupper():
        uc.append(i)
    if i.islower():
        lc.append(i)
    if i.isdecimal():
        dc.append(i)

s_new = lc + uc + dc
sc_count = 0
for i in s:
    if i not in s_new:
        s_new.append(i)
        sc_count += 1
print('String after arranging as per User: <<{}>>'.format(''.join(s_new)))
print(' Lower Case = {} \n Upper Case = {} \n Decimal = {} \n Special Character = {}'.format(len(lc),len(uc),len(dc),sc_count))


