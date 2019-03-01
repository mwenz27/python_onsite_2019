'''
--------------------------------------------------------
                GUESS THE RANDOM NUMBER
--------------------------------------------------------

Build a Guess-the-number game that asks a player for an input until they
pick the correct (randomly generated) number between 1 and 100.

Tip: Use python's 'random' module.

'''
import random

flag = True

random_num = random.randint(1, 100)
count = 0
while flag:
    x = int(input('Please select a number between 1 to  100: '))
    count += 1
    if x < random_num: # less than
        print('Enter a higher number')
    elif x > random_num:
        print('Enter lower number')
    elif x == random_num:
        print(f'Well done you got the right number {random_num} on {count} times ')
        flag = False