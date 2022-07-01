# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

s = input("Enter the String: \n")

s = ''.join(i for i in s.lower() if i.isalnum())
print('True' if s == s[::-1] else 'False')
