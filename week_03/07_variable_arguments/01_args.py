'''
Write a script with a function that demonstrates the use of *args.

'''

def pizza(*args):
    print('Pizza toppings :')
    for items in args:
        print(f'\t-{items}')


pizza('cheese', 'ham', 'pineapple', 'mushroom')
