'''
Write a program that reads in the file words.txt and prints only the
words with more than 20 characters (not counting whitespace).

Source: http://greenteapress.com/thinkpython2/html/thinkpython2010.html

'''

file = 'words.txt'

#one way
# with open(file, encoding='utf-8') as words:
#     contents = words.read()
#     words = contents.split() #create a list for words

# for word in words:
#     if len(word) > 20:
#         print(word)

with open(file, 'r') as fin:
    lines = fin.readlines()
    for line in lines:
        if len(line.strip()) > 20:
            print(line.rstrip())

