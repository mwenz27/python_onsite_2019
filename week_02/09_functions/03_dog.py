'''
Write a program with the following three functions:

    - bark - this function should not take in any arguments and should print the string "bark bark"
    - eat - takes in parameters food_item and amount and prints out "The dog ate <amount> of <food_item>
    - sleep - calls the python sleep method to sleep the program for 5 seconds.



'''

import time

def bark():
    print('bark bark')


def eat(food_item, amount=0):
    if amount > 0:
        print(f'the dog ate {food_item} , {amount} times')
    else:
        print('the dog is hungry')


def sleep():
    print('Look here')
    time.sleep(5)
    print('this printed 5 seconds after')


bark()
eat('meat', 10)
sleep()