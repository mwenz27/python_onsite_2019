'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple


Notes:

If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

'''

#_list = [2, 3, 4, 2, 1, 4, 21, 4, 566, 5, 9]

try:
    _list = (input('Enter numbers with spaces : ')).split()

    f_list = []

    if len(_list) % 2 == 0:
        #print('length is even', len(_list))
        for item in _list:
            f_list.append(float(item)) # Convert list to float
    else: #add a zero to the list to make it even
        _list.append(0)
        for item in _list:
            f_list.append(float(item)) # Convert list to float

except ValueError:
    print('that\'s not a number restart the script')

f_list.sort()



#create pairs
#print('Length ',len(f_list))

tuple_pair_list = []
count = 0
for i in range(0, len(f_list), 2):
    #print(i)
    count += i
    tuple_pair = (f_list[i], f_list[i+1])
    #print('index', i, i +1)
    #print(i,'count ', count)
    #print(tuple_pair)
    tuple_pair_list.append(tuple_pair)

print('Tuple Pair List', tuple_pair_list)

#prints each tuple
for pair in tuple_pair_list:
    print(pair)



