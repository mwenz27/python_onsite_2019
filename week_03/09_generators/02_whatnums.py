'''
Adapt your Generator expression from the previous Exercise
(remove the print() statement), then run a floor division by 1111 on it.
What numbers do you get?

'''

# note: range() also works with a generator object internally
nums = range(1, 1000000)


gen = (num for num in nums if num % 1111 == 0)
# print(gen)

