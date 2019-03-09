'''
Reproduce the functionality of python's .enumerate()

Define a function my_enumerate() that takes an iterable as input
and yields the element and its index

'''
def my_enumerate(list_input):
    count = -1
    list_pair = []
    for item in list_input:
        count += 1
        pair = [count, item]
        list_pair.append(pair)
    for pair in list_pair:
        print(pair)

my_list = [1, 2, 3, 5, 42]

my_enumerate(my_list)