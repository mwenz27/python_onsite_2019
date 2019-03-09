'''
Write a script that takes in two numbers from the user and calculates the quotient. Using a try/except,
the script should handle:

- if the user enters a string instead of a number
- if the user enters a zero as the divisor

Test it and make sure it does not crash when you enter incorrect values.

'''


try:
    a = int(input('Enter Number 1 : '))
    b = int(input('Enter Number 2 : '))
except TypeError as err:
    print(err)

try:
    c = a / b
except ZeroDivisionError as err:
    print(err)
else:
    print(c)
