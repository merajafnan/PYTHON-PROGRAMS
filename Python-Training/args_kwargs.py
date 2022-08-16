def args_kwargs(positional,keyword=3,*args,**kwargs):
    print('Positional: {}'.format(positional))
    print('keyword: {}'.format(keyword))
    print('args: {}'.format(args))
    print('kwargs: {}'.format(kwargs))

list_=[1,2,3,4,5,'a','b','c']
dic_={'a':1,'b':2,'c':3}
positional = 'Sample'
args_kwargs(positional,33,*list_,**dic_)

