from operator import is_
from stack import stack

par_str = "{{{}}}"
s = stack
is_balanced = True
index = 0

while index < len(par_str) and is_balanced:
    par = par_str[index]
    if par in '{([':
        s.push(par)
    else:
        if s.is_empty():
            is_balanced = False
        else:
            top = s.pop()
            if not is_match(par,top):
                is_balanced = False
    index = index +1

    if s.is_empty() and is_balanced:
        print("Balanced")
    else:
        print("not bbalanced")
