'''
--------------------------------------------------------
                RANDOM HASHTAG GENERATOR
--------------------------------------------------------

Programmatically generate random hashtags by picking from a word list.

Tip: In UNIX systems you can access a dictionary file at this path:
        /usr/share/dict/words

'''
#read the file

file = '/usr/share/dict/words'
with open(file, encoding='utf-8') as words:
    contents = words.read()


with open(file, encoding='utf-8') as words:
    contents = words.read() #also can be done in a iteration using the r.strip function
    #for word in words.readlines():
    #word = word.rstrip()
    #append(word)
    words = contents.split() # creates a list
    words.sort(key=len) #sorts the list by length
    print(words[:10]) # test line
    min_words_list = []
    max_words_list = []
#create a list for words

#find the length of the words

#use the random function and select a word for a hastag

#print hash tag