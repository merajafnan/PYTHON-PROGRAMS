def area(pi,r):
    return  (pi * r * r)

r = int(input("Enter the radius: \n"))
pi = 22/7
print("Area of Circle is: {:.3f}".format(area(pi,r)))