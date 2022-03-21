# Given a string like “The black cat climbed the green tree.”, 
# Print out the location of every “c” charcater.

def main():
    A='The black cat climbed the green tree.'
    lnA=len(A)
    for i in range(lnA):
        if A[i] == 'c':
            print(i+1)
main()


# text = "The black cat climbed the green tree."
# start = 0
# while True:
#     loc = text.find("c", start)
#     if loc == -1:
#         break
#     print(loc)
#     start = loc + 1