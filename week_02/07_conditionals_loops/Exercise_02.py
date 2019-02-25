'''
Take in a number from the user and print "Monday", "Tuesday", ...
"Sunday", or "Other" if the number from the user is 1, 2,... 7,
or other respectively. Use a "nested-if" statement.

'''

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
length_of_days = len(days)
#print(length_of_days)

user = int(input('Select a Number for a day: '))

if user <= length_of_days:
    print(days[user - 1]) # the minus 1 is to reference the index of the list
else:
    print(f'Other\nThe number you chosen is not in the range of the seven days {user}')
