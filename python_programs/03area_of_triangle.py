# Area of a triangle = (s*(s-a)*(s-b)*(s-c))-1/2 (herons formula)

# taking user input for 3 sides of triangle
a = float(input('Enter the first side'))
b = float(input('Enter the second side'))
c = float(input('Enter the third side'))

# calculate the semi-perimeter  
s = (a + b + c) / 2  

# calculating area of triangle
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5 

# printing the area
print('The area of the triangle is %0.2f' %area)   