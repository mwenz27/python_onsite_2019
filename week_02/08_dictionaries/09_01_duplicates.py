'''
Using a dictionary, write a function called has_duplicates that takes
a list and returns True if there is any element that appears more than
once.


'''
'''

words = {}
words["Hello"] = "Bonjour"
words["Yes"] = "Oui"
words["No"] = "Non"
words["Bye"] = "Au Revoir"
words['Cool'] = "Bonjour"

print(words)

list_count = []

#print key and values,
#count values
#if values > 1 list the
for k, v, in words.items():
    #print(k, v)
    if v in words:
        print(v)
    else:
        print('music')

'''

inputlist = ['a','a','b','c']

def dulipicate_checker(user_list):
    my_dict = {}
    for i in user_list:
        my_dict[i] = 0 #assigns a value to each one
    for i in user_list:
        my_dict[i] += 1

    # for i in my_dict: # iterates over keys (also could iterate over values
    #     if my_dict[i] > 1:
    #         my_dict[i] = True
    #     else:
    #         my_dict[i] = False

    for i in my_dict: # iterates over keys (also could iterate over values
        print(i)
        if my_dict[i] > 1:
            return True

    return False

    #print(my_dict)

dulipicate_checker(inputlist)

# TODO review this with debugger