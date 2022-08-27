with open('Sample1.txt','r+') as fh:
    words = fh.read()
    words = words.replace('down','up')
    fh.truncate(0)
    fh.write(words)
fh.close()




