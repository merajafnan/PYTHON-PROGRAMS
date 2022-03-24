# The following implementation has a bug. (Even though the n was supposed to remove the element
# and the code seems to mean that it does, we still see two items after we removed the first.)

q = []
while True:
    n=input('Enter name:')
    if n == 'n':
        print(q.pop(0))
        print(q)
        # continue
    if n == 's':
        print(q)
        print(len(q))
        exit()
    else:
        q.append(n)
        continue
    