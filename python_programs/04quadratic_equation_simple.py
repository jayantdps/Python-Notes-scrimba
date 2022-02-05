# calculate the discriminant  
#   d= sqrt of b -  (4*a*c)
  
# find two solutions  
# sol1 = (-b sqrt of d ) /2*a
# sol2 = (+b sqrt of d ) /2*a


import cmath

a = float(input('Enter the first number'))
b = float(input('Enter the second number'))
c = float(input('Enter the third number'))

# calculating discriminant
d = (b**2) - (4*a*c)

# Solution 1
sol1 = (-b-cmath.sqrt(d))/(2*a)  

# Solution 2
sol2 = (b-cmath.sqrt(d))/(2*a)

# printing the solution
print('The solution are {0} and {1}'.format(sol1,sol2))