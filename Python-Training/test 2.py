#
# l = [1,32,323,555,30203]
#
# for i in l:
#     i = str(i)
#     if i[::-1] == i:
#         print('{}  is a palindrome'.format(i))
#     else:
#         print('{}  is not a palindrome'.format(i))


# str1 = """
# regress@lagaf-vc-p1c3-05> show chassis hardware
# Hardware inventory:
# Item             Version  Part number  Serial number     Description
# Chassis                                YK4320080029      Virtual Chassis
# Routing Engine 0          BUILTIN      BUILTIN           RE-EX4400-48F
# Routing Engine 1          BUILTIN      BUILTIN           RE-EX4400-24T
# FPC 0            REV 01   650-114385   YK4320080029      EX4400-48F
#   CPU                     BUILTIN      BUILTIN           FPC CPU
#   PIC 0          REV 01   BUILTIN      BUILTIN           36x 1G SFP, 12x 1G/10G SFP/SFP+
#     Xcvr 4       REV 01   740-021308   ECX01K42325       SFP+-10G-SR
#     Xcvr 5       REV 02   740-013111   I193641           SFP-T
#     Xcvr 9       REV 01   740-031851   AM1125SUQ4W       SFP-SX
#     Xcvr 10      REV 02   740-011613   PJ21625           SFP-SX
#     Xcvr 14               NON-JNPR     PQK4JGP           SFP-T
#     Xcvr 15      REV 02   740-013111   D332835           SFP-T
#     Xcvr 18      REV 02   740-011613   PJH4B3F           SFP-SX
#     Xcvr 19      REV 02   740-011613   AM1039SHWXW       SFP-SX
#     Xcvr 22      REV 01   740-021308   ECX01K42306       SFP+-10G-SR
#     Xcvr 24      REV 02   740-013111   N3ADLS7           SFP-T
#     Xcvr 25      REV 02   740-013111   N3AAHFS           SFP-T
#     Xcvr 30      REV 02   740-011613   PJ21JBQ           SFP-SX
#     Xcvr 36      REV 01   740-031980   ARE10RQ           SFP+-10G-SR
#     Xcvr 38      REV 01   740-021308   09T511102701      SFP+-10G-SR
#     Xcvr 40      REV 01   740-011613   E08G00760         SFP-SX
#     Xcvr 41      REV 01   740-031980   AZP067X           SFP+-10G-SR
#     Xcvr 43      REV 01   740-031980   AZP0NQG           SFP+-10G-SR
#     Xcvr 44      REV 01   740-021308   09T511103510      SFP+-10G-SR
#     Xcvr 45      REV 01   740-021308   A09CVJ3           SFP+-10G-SR
#     Xcvr 46      REV 01   740-021308   CG35KM28L         SFP+-10G-SR
#     Xcvr 47      REV 01   740-021308   13T511102226      SFP+-10G-SR
# """
#
# str1 = str1.split('\n')
# # print(str1)
# str1.pop(0)
# str1.pop(0)
# str1.pop(0)
# str1.pop(-1)
# # print(str1)
#
# count = 0
# for i in str1:
#     j = i.split()
#     if j[-1] == 'SFP+-10G-SR':
#         count += 1
# print('Count of SFP+-10G-SR is : {}'.format(count))




str2 = """
PID USERNAME    THR PRI NICE   SIZE    RES STATE    C   TIME    WCPU COMMAND
18775 root          2  31    0  1295M   501M CPU0     0 275:28  99.67% fxpc
45075 root          2  20    0   696M   152M select   0   1:16   70.76% authd
18403 root          1  20    0   470M    15M select   1   3:44   20.44% eventd
19213 root          1  20    0   508M    42M select   3   4:48   85.40% mib2d
19215 root          1  20    0   787M    28M select   3   3:51   0.32% l2ald
19214 root          3  20    0   608M    93M kqread   0   1:38   0.14% rpd
18774 root          2  20    0    10M  4056K kqread   0   0:41   0.12% lcmd
19217 root          1  20    0   510M    38M select   2   1:28   0.10% pfed
45073 root          2  20    0   561M    43M select   3   0:10   0.09% jdhcpd
18761 root          1  20    0   590M    58M select   3   0:36   0.08% chassisd
"""

str2 = str2.split('\n')
print(str2)
str2.pop(0)
str2.pop(0)
str2.pop(-1)
print(str2)

dict_ = {}

for i in str2:
    j = i.split()
    # print(j)
    dict_[j[10]] = j[11]

print(dict_)

for i in dict_:
    i = i[:-1]
    i = float(i)
    # print(i,type(i))
    if i > 70:
        print(i)


6 year ago a:b = 6:5
4 year after a:b = 11:10










