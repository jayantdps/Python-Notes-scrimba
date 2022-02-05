# taking in numbers from user and storing in variables.
num1 = input('Enter the first number: ')
num2 = input('Enter the second number: ')

# adding two numbers
sum = float(num1) + float(num2)

# subtracting two numbers
min = float(num1) - float(num2)

# multiplying two nnumbers
mul = float(num1) * float(num2)

# dividing two numbers
div = float(num1) / float(num2)

# displaying the sum
print('The addition of {0} and {1} is {2}'.format(num1,num2,sum))

# displaying the subtraction
print('The subtration of {0} and {1} is {2}'.format(num1,num2,min))

# displaying the multiplication
print('The multiplication of {0} and {1} is {2}'.format(num1,num2,mul))

# displaying the division
print('The division of {0} and {1} is {2}'.format(num1,num2,div))