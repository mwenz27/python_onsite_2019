'''
Write a script that takes a user inputted string
and prints it out in the following three formats.
    - All letters capitalized.
    - All letters lower case.
    - All vowels lower case and all consonants upper case.

'''

sentence = "If real is what you can feel, smell, taste and see, then real is simply electrical signals interpreted by your brain."

vowels = ['a', 'e', 'i', 'o', 'u']
print(sentence.upper())
print(sentence.lower())
reconstructed_list = []

for letter in sentence.lower():
    #print(letter, end='')
    if letter in vowels: # membership operator
        #print('passed through here')
        x = letter.lower()
        reconstructed_list.append(x)
    else:
        x = letter.upper()
        reconstructed_list.append(x)

print('\n')
#print(reconstructed_list)
for i in reconstructed_list:
    print(i, end='')