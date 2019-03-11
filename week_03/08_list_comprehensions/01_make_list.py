'''
Use a one-line list comprehension to express the following functionality:

letters = []

for letter in 'suchalongword':
    letters.append(letter)

print(letters)

'''
x = []
for letter in 'suchalongword':
    x.append(letter)
print(x)

x = [letter for letter in 'suchalongword']

print(x)