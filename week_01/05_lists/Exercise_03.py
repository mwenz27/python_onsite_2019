'''
Sum up all elements from the nested list of integers below.

'''

list_ = [1, 2, [10, 11], [42, 3], 9]
flattened_list = [] #first need to unwrap the list in a nested for loop
sum = 0

## TODO Flatten list



for i in list_:
    #print(index)
    if isinstance(i, list): # if type(i) == list :
        for j in i: # if the item is a list loop in the list
            flattened_list.append(j)
    else:
        flattened_list.append(i)

print(sum(list_))


def flatten(l, a):
    sum += a
    for i in l:
        if isinstance(i, list):
            flatten(i, a)
        else:
            a.append(i)
    return a


#flatten(list_)