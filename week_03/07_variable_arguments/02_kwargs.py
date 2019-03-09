'''
Write a script with a function that demonstrates the use of **kwargs.

'''

def pizza(**kwargs):
    print('Pizza toppings :')
    for k, v in kwargs.items():
        print(f'\t - {k}: {v}')


pizza(cheese=12, ham=21, pineapple=23, mushroom=65)