'''
Re-write the following listcomp as a lambda expression.

'''

names = ['Anne', 'Amy', 'Bob', 'David', 'Carrie', 'Barbara', 'Zach']

names_starting_with_D = lambda x: x.startswith('D')

for name in names:
    print(name, names_starting_with_D(name))

