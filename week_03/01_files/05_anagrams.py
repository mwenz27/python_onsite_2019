'''
Download http://thinkpython2.com/code/anagram_sets.py.
You’ll see that it creates a dictionary that maps from a sorted string
of letters to the list of words that can be spelled with those letters.
For example, 'opst' maps to the list:
['opts', 'post', 'pots', 'spot', 'stop', 'tops'].

Write a module that imports anagram_sets and provides two new functions:
store_anagrams should store the anagram dictionary in a “shelf”;
read_anagrams should look up a word and return a list of its anagrams.
Solution: http://thinkpython2.com/code/anagram_db.py.


Source: Read through the "Files" chapter in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2015.html

'''

import itertools

file = '/usr/share/dict/words'

with open(file, encoding='utf-8') as words:
    contents = words.read()
    words = contents.split() #create a list for words


def read_anagrams(string):
    print('Please wait.....compute is long if with the increase of combination of characters')
    list_ = list(string)
    read_anagrams_list = []
    count = 0
    for c in itertools.permutations(list_):
        count += 1
        x = ''.join(c)
        if x in words:
            read_anagrams_list.append(x)
    y = len((read_anagrams_list))
    print('Finished')

    return print('Combinations',y, read_anagrams_list)

        #print('Combination', count, ': ', x)


# for c in itertools.combinations(list_, 2): # unrelated but keeping for learning
#     print(c)

read_anagrams('spine')