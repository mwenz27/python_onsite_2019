'''
Write a program that gets a number between 1 and 1,000,000,000
from the user and determines whether it is odd or even using an if statement.
Print the result.

NOTE: We will be using the input() function. This is demonstrated below.

'''
import random

number = random.randint(1, 1000000000)
#number = int(input('Choose a number between 1 and 1,000,000,000  :    '))
print(number)

if number % 2 == 0:
    print('The number even ')
else:
    print('The number is odd ')