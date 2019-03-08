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

from md5checksum import *


from md5checker import make_hash
import md5checker

#find directory


path = '/Users/Wenz/Desktop/screenshots'

#create a list to compare the files with eachother,

# print(os.path.abspath(path))



data_list = []

data_list_dictionary = {}

for root, dirs, files in os.walk(path):
    for filename in files:
        data_list.append(filename)
        # print(filename)
        #print(compute_checksum(filename))
        #command = f"md5 -r '{os.(filename)}' "


os.chdir(path)
list_of_files = list()
for (dirpath, dirnames, filenames) in os.walk(path):
    #print(dirpath, dirnames, filenames)
    list_of_files += [os.path.join(dirpath, file) for file in filenames]

print(list_of_files[0])



#print(len('a64561d4c0d4fc21a24d9f080447f6de'))
# Create a dictionary

file_dict = {}

os.chdir(path)
for file in list_of_files:
    hash_file = make_hash(file, algo='sha1')
    file_dict[file] = hash_file

# use md5check sum to compare the values of files

list_of_duplicates = []

for k1, v1 in file_dict.items():
    k = k1
    v = v1
    for k2, v2 in file_dict.items():
        if v == v2 and k != k2:
            list_of_duplicates.append(k)
            list_of_duplicates.append(k2)

for i in list_of_duplicates:
    print(i, make_hash(i))



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






#if the md5checksum is true print duplicates

