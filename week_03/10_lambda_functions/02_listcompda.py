'''
Re-write the following listcomp as a lambda expression.

'''

names = ['Anne', 'Amy', 'Bob', 'David', 'Carrie', 'Barbara', 'Zach']

#print([x.startswith('D') for x in names])

# d_in_names = print(lamba name : for name in names if "D" in name)

# listcomp = [name for name in fish_tuple if 'fish' in name]

f = lambda x: x.startswith('D')

for name in names:
    print(f(name))

