'''
Create a script that asks a user to input an integer, checks for the
validity of the input type, and displays a message depending on whether
the input was an integer or not.

The script should keep prompting the user until they enter an integer.

'''

flag = True

while flag:
    try:
        user_input = input('Enter a Number : ')
        user_input = float(user_input)
    except ValueError as err:
        print(err)
        print('Your still in the loop')
    else:
        print('congrats this is a number!, your out of the loop')
        flag = False