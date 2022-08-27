def arguments_(default,*args,**kwargs):
    print(default)
    print(args)
    print(kwargs)
name = 'Meraj Hassan'
Skills = ['CCNA','CCNP ENCOR','CCNP ENARSI','CCIE R&S','DEVOPS','AWS','PYTHON','ROBOT FW']
Ratings = {
    'CCNA': 9,
    'CCNP': 9,
    'ENCOR':9,
    'CCNP ENARSI': 9,
    'CCIE R&S': 7,
    'DEVOPS':5,
    'AWS':5,
    'PYTHON':7,
    'ROBOT FW':8
}
arguments_(name,*Skills,**Ratings)