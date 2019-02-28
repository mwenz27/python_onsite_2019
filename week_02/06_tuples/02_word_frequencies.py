'''
Write a function called most_frequent that takes a string and prints
the letters in decreasing order of frequency.

For example, the follow string should produce the following result.

string_ = 'hello'

Output:
l, h, e, o

For letters that are the same frequency, the order does not matter.

'''

string = 'hello'

set_string = set(string)
#print(set_string)

my_dict = {}

for item in set_string:
    my_dict[item] = 0

print('First dictionary ', my_dict)


for letter in string:
    if letter in set_string:
        my_dict[letter] += 1
    else:
        pass

sorted(my_dict.items(), key=lambda kv: [1], reverse=False)

print(my_dict.keys())


