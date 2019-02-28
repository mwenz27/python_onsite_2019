'''
Write a program with the following three functions:

    - bark - this function should not take in any arguments and should print the string "bark bark"
    - eat - takes in parameters food_item and amount and prints out "The dog ate <amount> of <food_item>
    - sleep - calls the python sleep method to sleep the program for 5 seconds.



'''

import time


def bark():
    return 'bark bark'


def eat(food_item, amount=0):
    if amount > 0:
        print(f'the dog ate {food_item} , {amount} times')
    else:
        print('the dog is hungry')


def sleep():
    print('the dogs eating')
    time.sleep(5)
    print('the dog is satisfied, thanks for feeding the dog')


flag = True

while flag:
    print(bark())
    ans = input('Do you want to feed the dog (y/n): ')
    if ans == 'y':
        food = input('What do you want to feed the dog :')
        amount = int(input('How much do you want to give the dog: '))
        eat(food, amount)
        sleep()
        flag = False
    else:
        continue



