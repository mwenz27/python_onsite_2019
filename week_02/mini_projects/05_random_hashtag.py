'''
--------------------------------------------------------
                RANDOM HASHTAG GENERATOR
--------------------------------------------------------

Programmatically generate random hashtags by picking from a word list.

Tip: In UNIX systems you can access a dictionary file at this path:
        /usr/share/dict/words

'''

import random

file = '/usr/share/dict/words'

with open(file, encoding='utf-8') as words:
    contents = words.read()
    words = contents.split() #create a list for words

for i in range(10):
    number = random.randint(1, len(words))
    print(f'#{words[number].capitalize()}', end=" ")


