'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''

import random


def name(input_user_name):
    print(f'Hello {input_user_name}')
    return my_func()


def my_func():
    print('Here is some free money', end=" ")
    x = random.randint(0, 2)
    return day(x)


def day(x):
    list_1 = ['monday', 'tuesday', 'wednesday']
    print('on',list_1[x].capitalize())


name('Michael')





