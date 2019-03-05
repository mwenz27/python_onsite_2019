'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''
file = 'words.txt'

with open(file, encoding='utf-8') as words:
    contents = words.read()
    words = contents.split() #create a list for words

words.sort(key=len)
print(len(words[0]))

for word in words:

    if len(word) == 2: #smallest word is 1 (len(words[0]))
        print(word)
    elif len(word) == len(words[len(words)-1]):
        print(word)


print('\nTotal number of words in the file ', len(words))

