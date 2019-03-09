'''
Demonstrate how to create a generator object. Print the object to the console to see what you get.
Then iterate over the generator object and print out each item.

'''

my_list = [1, 2, 3, 5, 42]

gen = (x**2 for x in my_list)
print(gen)

for x in gen:
    print(x)
