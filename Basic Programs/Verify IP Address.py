ipv4 = input("Enter IPV4 Address")
flag = False

if ("." in ipv4):
    octet = ipv4.strip().split(".")
    if (len(octet) == 4):
        for i in octet:
            if (i.isnumeric() and int(i)>=0 and int(i)<=255):
                flag = True
            else:
                flag = False
                break
if flag:
    print("IPV4 Validated")
else:
    print("Wrong Format")
