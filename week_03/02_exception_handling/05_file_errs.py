'''
Read in the first number from 'integers.txt' and perform a calculation
with it.
Make sure to catch at least two possible Exceptions (IOError and ValueError)
with specific except statements, and continue to do the calculation
only if neither of them applies.

'''

file = 'integers.txt'
with open(file, 'r') as fir:
    contents = fir.readlines()


print([lambda line: line in contents])