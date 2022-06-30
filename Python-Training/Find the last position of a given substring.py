# s1 = input("Enter the String")
# s2 = input("Enter the Sub-String")

s1 = "Emma"
s2 = "Emma is a data scientist who knows Python. Emma works at google."

print('Sub - String Found' if s1 in s2 else 'Not Found')
z = s2.rfind('Emma')
print(z)

# Output:
#
# Sub - String Found
# 43