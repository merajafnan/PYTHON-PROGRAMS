
# interface Gi1/1/1.${INT__}
# encapsulation dot1Q 1${INT__}
# ip add 60.1.1.${IP} 255.255.255.252
# shut
# no shut

# z = 1
# with open('subint.txt','w') as fh:
#     for i in range(1,255,4):
#         if z < 10:
#             fh.write("interface Gi1/1/1.{}\\nencapsulation dot1Q 100{}\\nip add 60.1.1.{} 255.255.255.252\\nno shut\\n".format(z,z,i))
#         if z >= 10 and z < 100:
#             fh.write("interface Gi1/1/1.{}\\nencapsulation dot1Q 10{}\\nip add 60.1.1.{} 255.255.255.252\\nno shut\\n".format(z,z,i))
#         z += 1
#     for i in range(1,255,4):
#         if z >= 10 and z < 100:
#             fh.write("interface Gi1/1/1.{}\\nencapsulation dot1Q 10{}\\nip add 60.1.2.{} 255.255.255.252\\nno shut\\n".format(z,z,i))
#         if z >= 100:
#             fh.write("interface Gi1/1/1.{}\\nencapsulation dot1Q 1{}\\nip add 60.1.2.{} 255.255.255.252\\nno shut\\n".format(z,z,i))
#         z += 1
#     for j in range(3,9):
#         for i in range(1,255,4):
#             if z >= 100:
#                 fh.write("interface Gi1/1/1.{}\\nencapsulation dot1Q 1{}\\nip add 60.1.{}.{} 255.255.255.252\\nno shut\\n".format(z,z,j,i))
#             z += 1


#####################################################################################

# z = 1
# with open('subint.txt','w') as fh:
#     for i in range(1,255,4):
#         if z < 10:
#             fh.write("interface Gi1/1/1.{}\\nencapsulation dot1Q 100{}\\nip add 60.1.1.{} 255.255.255.252\\nno shut\\n".format(z,z,i))
#         z += 1


#####################################################################################

# with open('subint.txt','w') as fh:
#     for i in range(1,513):
#         fh.write('no interface Gi1/1/1.{}\\n'.format(i))


##################################--OSPF--#############################################
# 71.1.X.X

with open('subint.txt','w') as fh:
    for i in range(0,8):
        for j in range(1,255,4):
            fh.write('network 71.1.{}.{} 0.0.0.3 area 83\\n'.format(i,j))

##################################--OSPF--#############################################
# 71.1.X.X

# with open('subint.txt','w') as fh:
#     for i in range(0,8):
#         for j in range(1,255,4):
#             fh.write('no router ospf 1\\n'.format(i,j))







