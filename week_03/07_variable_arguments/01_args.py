'''
Write a script with a function that demonstrates the use of *args.

'''


def pizza(*args):
    string = 'Pizza toppings :\n'
    for items in args:
        string += f'\t-{items}\n'
    return print(string)


pizza('cheese', 'ham', 'pineapple', 'mushroom')
