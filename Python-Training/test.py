str= '''PE1_ESP200x#sh ip int br
Interface              IP-Address      OK? Method Status                Protocol
Fo0/0/0                unassigned      YES unset  up                    up      
Fo0/0/1                unassigned      YES unset  up                    up      
Te0/1/0                99.1.1.1        YES NVRAM  up                    up      
Te0/1/1                unassigned      YES unset  down                  down    
Te0/1/2                77.1.1.1        YES NVRAM  up                    up      
Te0/1/3                unassigned      YES unset  down                  down 
Te1/1/1.4001           102.1.1.2       YES NVRAM  up                    up      
Te1/1/1.4002           102.1.2.2       YES NVRAM  up                    up      
Te1/1/2                65.0.0.2        YES NVRAM  up                    up 
 '''

str = str.split('\n')
# print(str)
str.pop()
str.pop(0)
# print(str)
dic = {}
for i in str:
    z = i.split()
    # print(z)
    dic[z[0]] = z[5]
print(dic)








