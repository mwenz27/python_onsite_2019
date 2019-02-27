'''
Sum up all elements from the nested list of integers below.

'''

list_ = [1, 2, [10, 11], [42, 3], 9]
flattened_list = [] #first need to unwrap the list in a nested for loop



for i in list_:
    if isinstance(i, list): # if type(i) == list :
        for j in i: # if the item is a list loop in the list
            flattened_list.append(j)
    else:
        flattened_list.append(i)

print(flattened_list,'\n', sum(flattened_list))

