# l = [9,5,0,-1,3,4]
# z = len(l)
# 9,5,0,-1,3,4
# -1
# l = [1,3]

# for i in range(len(l)):
#     for j in range(i,len(l)):
#         if l[i] < l[j]:
#             l[i] , l[j] = l[j] , l[i]
# print(l)

# [4,3,-1,0,5,9]

# for i in range(len(l)-1,-1,-1):
#     l.append(l[i])
#     print(l)
#
# for i in range(z):
#     l.pop(0)
# print(l)


# l = [9,5,0,-1,3,4]
# mid = int(len(l)/2)
# k=0
# for i in range(len(l)-1,mid,-1):
#     l[k],l[i] = l[i],l[k]
#     k += 1
# print(l)

# l = [9,5,0,-1,3,4,6]
# mid = int(len(l)/2)
# k=0
# for i in range(len(l)-1,mid,-1):
#     l[k],l[i] = l[i],l[k]
#     k += 1
# print(l)


var mini=minimum;
  var maxi=maximum;
}
function verify(val){
    if(val<mini)return "Input is less than minimum value";
   if(val>=mini && val<=maxi)return "Input is in range";
    return "Input is more than maximum value";

if len(palindrome) == 1:
    return ""

for i in range(len(palindrome)//2):
    if palindrome[i] != 'a':
        return palindrome[:i] + 'a' + palindrome[i+1:]

return palindrome[:-1] + 'b'


palindromeStr = list(palindromeStr)

if len(palindromeStr) == 1:
    return ''

for index in range(len(palindromeStr) // 2):
    if palindromeStr[index] != 'a':
        palindromeStr[index] = 'a'
        return ''.join(palindromeStr)

palindromeStr[-1] = 'b'
return ''.join(palindromeStr)

palindromeStr = list(palindromeStr)

if len(palindromeStr) == 1:
    return ''

for index in range(len(palindromeStr) // 2):
    if palindromeStr[index] != 'a':
        palindromeStr[index] = 'a'
        return ''.join(palindromeStr)

palindromeStr[-1] = 'b'
return ''.join(palindromeStr)






if len(palindromeStr) <= 1:
    return ""

out = list(palindromeStr)
for i in range(math.floor(len(palindromeStr)/2)):
    if out[i] != "a":
        out[i] = "a"
        return "".join(out)

out[len(out)-1] = "b"
return "".join(out)




n = len(palindromeStr)
if n == 1:
    return 'IMPOSSIBLE'

for i in range(n // 2):
    if palindromeStr[i] != 'a':
        return palindromeStr[:i] + 'a' + palindromeStr[i+1:]

return palindromeStr[:-1] + 'b'



arr = list(palindromeStr)
get = False
for i in range(len(arr)//2):
    if arr[i]=="a" or get:
        continue
    else:
        arr[i] = "a"
        get = True
if not get and len(arr)>1:
    t = ord(arr[-1])+1
    arr[-1] = chr(t)
    return "".join(arr)
if not get:
    return ""
return "".join(arr)










