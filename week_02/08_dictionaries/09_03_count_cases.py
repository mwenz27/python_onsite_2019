'''
Write a script that takes a sentence from the user and returns:

- the number of lower case letters
- the number of uppercase letters
- the number of punctuations characters
- the total number of characters

Use a dictionary to store the count of each of the above.
Note: ignore all spaces.

Example input:
    I love to work with dictionaries!
Example output:
    Upper case: 1
    Lower case: 26
    Punctuation: 1

'''

#iterating starting varibles
def wordcount(string):
    upper_count = 0
    lower_count = 0
    punt_count = 0
    punctuation = [",", ".", "!", "?", ":", ";", "(", ")", "'"]
    number_of_charaters = len(string)

    for letter in string:
        if letter in punctuation:
            punt_count += 1
        elif letter == letter.lower():
            lower_count += 1
        elif letter == letter.upper():  # upper case characters
            upper_count += 1

    new_dict = {}
    #TODO is there another way to make a dictionary?

    new_dict['Upper case'] = upper_count
    new_dict['Lower case'] = lower_count
    new_dict['Punctuation'] = punt_count
    new_dict['Number of characters'] = number_of_charaters

    print('Information from the string : ', string)
    for k, v in new_dict.items():
        print('\t', k, v)

string = 'There\'s a difference, betwEEn knowing the path and Walking the path.'

wordcount(string)







