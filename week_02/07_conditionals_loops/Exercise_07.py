'''
Use a "while" loop to print out every third number counting backwards from 1000 to 1.

'''

x = 1000

while x >= 0:
    x -= 3
    print(x, end=" ")
    if x == 0:
        break