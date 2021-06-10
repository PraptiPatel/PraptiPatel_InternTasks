# Python program to swap two variables using temporary variable

# take inputs from user
a = input('Enter the value of a: ')
b = input('Enter the value of b: ')

print('Values Before Swapping')
print('a = ',a, 'and b = ',b)

# create a temporary variable and swap the value
temp = a
a = b
b = temp

# display swapping values
print('Values After Swapping')
print('a = ',a, 'and b = ',b)