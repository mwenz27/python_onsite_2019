'''
Write a script that finds the first vowel in a a user inputted string.

'''


sentence = "Don’t think you are, know you are"
#print(sentence)
vowels = ['a', 'e', 'i', 'o', 'u']
count = 0
tuple_list = []

for letters in sentence:
    for vowel in vowels:
        if letters in vowel: # will only pass letters which are in vowels
            #print(letters)
            count += 1
            tuple_list.append((letters, count))


print(tuple_list)

print(f'The first vowel in found in the sentence is {tuple_list[0]}')