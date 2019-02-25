'''
Given the two lists below, find the elements that are the same
and put them in a new list.
Put the elements that are different in another list.

Print both.

'''


list_one = [0, 4, 6, 18, 25, 42, 100]
list_two = [1, 4, 9, 24, 42, 88, 99, 100]


common_list = []
not_matching = []

# comparing lists by looking at one element searching through the next list
for item in list_one:
    #print(item, end=' ')
    if item in list_two:
        common_list.append(item)

combined_list = list_one + list_two

# Comparing the list
for item in combined_list:
    #print(item, end='')
    if item not in common_list:
        not_matching.append(item)



print(f'\nCommon numbers are {common_list}')

print(f'Not matching numbers are {not_matching}')


## TODO the Also possible to do look list as sets