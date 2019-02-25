'''
Write the necessary code to display the follow message to the console
Challenge: write code to duplicate the "co-" part
instead of writing it 3 times.

Time for co-co-co-ding.

'''
stem_word = "ding"
prefix = "co-"

one_word = prefix*3+stem_word
print('Time for', one_word)

new_word = ""
for i in range(3):
    new_word += prefix
print('Time for', new_word+stem_word)

print(f'time of {"co-"*3}ding')
