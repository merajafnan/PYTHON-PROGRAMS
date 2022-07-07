import fileinput

1. This will print every line one by one in the file
fn = open('Example.txt','r')
for i in fn:
    print(i)

2. Python code to illustrate read() mode
print(fn.read())

3. Read the first five characters of stored data and return it as a string
print(fn.read(10))

4. Create a file and how to write mode works
fw = open('Example1.txt','w')
fw.write("This file is created using write Command")
fw.write("File.write allows to create files")
fw.close()

fn = open('Example1.txt','r')
print(fn.read())
fn.close()

5. File Handeling using with
with open('Example.txt') as fn:
    print(fn.read())
fn.close()