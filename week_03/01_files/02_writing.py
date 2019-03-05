'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''

file = 'words.txt'

with open(file, 'r') as fir:
    lines = fir.readlines()

with open('words_reverse.txt', 'w') as fiw:
    for line in lines:
        x = line.strip()
        xr = x[::-1] + "\n"
        #print(xr)
        fiw.write(xr)




