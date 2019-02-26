'''
Write a script that prints out all the squares of numbers
from a user inputed lower to a user inputed upper bound.

Use a for loop that demonstrates the use of the range function.

'''
try:
    lower = int(input('Select a lower number : '))
    upper = int(input('Select an upper number : '))
except ValueError:
    print('Please select numbers')

print(f'The list of squares from {lower} to {upper}')

for i in range(lower, upper+1, 1): #+1 is inclusive
    x = i**2
    print(x, end=' ')

