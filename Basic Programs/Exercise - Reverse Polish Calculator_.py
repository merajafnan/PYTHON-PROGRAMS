# input token = ['4','13','5','/','+']
# output = 6
# Explaination = (4+(13/5))


Stack_Cal = []
Stack_ = []
while True:
    User_Inp = input(':')
    if User_Inp != 'D':
        Stack_.append(User_Inp)
        print(Stack_)
        continue
    else:
        print('Claculation will be done on below data')
        print(Stack_)
        break
def isnum(s):
    try:
        int(s)
        return(True)
    except:
        return(False)
for i in Stack_:
    if isnum(i):
        Stack_Cal.append(i)
    else:
        if i != '=':
            S1 = int(Stack_Cal.pop())
            S2 = int(Stack_Cal.pop())
            if i == '+':
                # S1 = int(Stack_Cal.pop())
                # S2 = int(Stack_Cal.pop())
                S3 = S2 + S1
                Stack_Cal.append(S3)
                print(Stack_Cal)
            elif i == '-':
                # S1 = int(Stack_Cal.pop())
                # S2 = int(Stack_Cal.pop())
                S3 = S2 - S1
                Stack_Cal.append(S3)
                print(Stack_Cal)
            elif i == '*':
                # S1 = int(Stack_Cal.pop())
                # S2 = int(Stack_Cal.pop())
                S3 = S2 * S1
                Stack_Cal.append(S3)
                print(Stack_Cal)
            elif i == '/':
                # S1 = int(Stack_Cal.pop())
                # S2 = int(Stack_Cal.pop())
                S3 = S2 / S1
                Stack_Cal.append(S3)
                print(Stack_Cal)
        else:
           print('Result of Reverse Polish Number:',end=' ')
           print(Stack_Cal)
           break



