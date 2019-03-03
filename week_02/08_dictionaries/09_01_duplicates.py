'''
Using a dictionary, write a function called has_duplicates that takes
a list and returns True if there is any element that appears more than
once.


'''


words = {}
words["Hello"] = "Bonjour"
words["Yes"] = "Oui"
words["No"] = "Non"
words["Bye"] = "Au Revoir"
words['Cool'] = "Bonjour"

def duplicate_checker(user_list):
    my_dict = {}

    for i in user_list:
        my_dict[i] = 0  # assigns a value to each one
    for i in user_list:
        my_dict[i] += 1

    for k, v in my_dict.items():  # iterates over keys (also could iterate over values)
        if v > 1:
            print(f'There is a duplicate word in the list its \'{k}\' occuring {v} times')
    #print(my_dict)
    return

input_list = ['a', 'a', 'b', 'c', 'd', 'd']

duplicate_checker(input_list)
duplicate_checker(words)
