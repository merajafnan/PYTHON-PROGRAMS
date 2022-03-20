# Write a script that will ask for the sides of a rectangular and print out the area. 
# Provide error messages if either of the sides is negative.

def main():
    length=float(input('Enter the Length'))
    breadth=float(input('Enter the Bredth'))
    if length<0 or length==0:
        print('length is negative or Equals to Zero')
    elif breadth<0 or breadth==0:
        print('Breadth is negative or Equals to Zero')
    else:
        print('Area',length*breadth)
print('Area of Rectangle')
main()
