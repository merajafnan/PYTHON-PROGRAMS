from operator import le, length_hint
import sys
if len(sys.argv) != 3:
    exit(f"Usage: {sys.argv[0]} short-STRING long-STRING")
string = sys.argv[1]
text = sys.argv[2]
print('\nString,text = ',string,text)
if string in text:
    oc = text.index(string)
    print(string, "can be found in ", text, "at", loc)
else:
    print(string, "can NOT be found in ", text)

# print(sys.argv[0])
# # print(sys.argv[1])
# # print(sys.argv[2])
# # print(sys.argv[3])
# # print(sys.argv[4])
# print(len(sys.argv))