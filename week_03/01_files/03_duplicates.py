'''
In a large collection of MP3 files, there may be more than one copy of
the same song, stored in different directories or with different file
names. The goal of this exercise is to search for duplicates.

Write a program that searches a directory and all of its subdirectories,
recursively, and returns a list of complete paths for all files with a
given suffix (like .mp3). Hint: os.path provides several useful
functions for manipulating file and path names.
To recognize duplicates, you can use to compute a “checksum” for
each file. If two files have the same checksum, they probably have the
same contents. To double-check, you can use the Unix command diff.
Solution: http://thinkpython2.com/code/find_duplicates.py.

Go and tackle your duplicate files! :)

Source: Read through the "Files" chapter in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2015.html

'''

import os

import md5checker

#find directory


path = '/Users/Wenz/Desktop/screenshots'

#create a list to compare the files with eachother,

print(os.path.abspath(path))



data_list = []

data_list_dictionary = {}


for root, dirs, files in os.walk(path):

    for filename in files:
        data_list.append(filename)
        #command = f"md5 -r '{os.(filename)}' "


os.chdir(path)
list_of_files = list()
for (dirpath, dirnames, filenames) in os.walk(path):
    #print(dirpath, dirnames, filenames)
    list_of_files += [os.path.join(dirpath, file) for file in filenames]


print(len('a64561d4c0d4fc21a24d9f080447f6de'))
# Create a dictionary

os.chdir(path)
for file in list_of_files:
    hash_file = make_hash(file, algo='sha1')
    print(hash_file)



# use md5check sum to compare the values of files
# for file in list_of_files:
#     command = f"md5 -r '{file}'"
#     print(command)
#     hash_and_file_name = str(os.system(command)) ## this is a bash file command running in python, it returns zero
#     hash_2.append(hash_and_file_name)
#     print(hash_and_file_name[:31])
#     #print(hash_and_file_name)
#     # hash_name = hash_and_file_name
#     # print(hash_name)
#     #print(type(hash_and_file_name))

print(hash_2)




#if the md5checksum is true print duplicates

