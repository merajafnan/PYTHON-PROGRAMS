dna = 'ACCGXXCXXGTTACTGGGCXTTGT'
dna = list(dna)
print(dna)
for i in dna:
    if i != 'A' and i != 'C' and i != 'T' and i != 'G':
        index = dna.index(i)
        # print(dna[index])
        dna[index] = ' '
print(dna)
dna = ''.join(dna)
print(dna)
dna = dna.split()
print(dna)
dna.sort(key=len, reverse=True)
print(dna)
