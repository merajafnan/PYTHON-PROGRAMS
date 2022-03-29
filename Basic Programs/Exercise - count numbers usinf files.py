# 1. Given the file examples/files/numbers.txt (or a similar file), count how many times each digit
# appears? The output will look like this. Just different values.
# 2. Save the results in a file called report.txt.

count_ = [0]*10
with open('numbers.txt','r') as fh:
    for i in fh: 
        for j in i.rstrip('\n'):
            if j == ' ':
                continue
            j = int(j)
            count_[j] = count_[j] + 1
s
with open('report.txt','w') as fh:
    for k in range(len(count_)):
        fh.write('Number = {} Occurance = {} \n'.format(k,count_[k]))