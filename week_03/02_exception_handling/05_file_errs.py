'''
Read in the first number from 'integers.txt' and perform a calculation
with it.
Make sure to catch at least two possible Exceptions (IOError and ValueError)
with specific except statements, and continue to do the calculation
only if neither of them applies.

'''

file = 'integers.txt'

try:
    with open(file, 'r') as fir:
        contents = fir.readlines()
except IOError as err:
    print('First block', err)


if len(contents) % 2 == 0:
    pair_list = list(range(0, len(contents), 2))
    for i in pair_list:
        try:
            num = int(contents[i].rstrip() + contents[i+1].rstrip())
            num = num**2
        except ValueError as err:
            print('Second block ', err)
        else:
            print(num, end=" ")



# print([lambda line: line in contents])