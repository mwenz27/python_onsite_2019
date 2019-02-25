'''
Take in 10 numbers from the user. Place the numbers in a list.
Using the loop of your choice, calculate the sum of all of the
numbers in the list as well as the average.

Print the results.

'''

num = []# create a list of numbers
count = 0
try:
    print('Input numbers 10 times \n')
    for i in range(10):
        count += 1
        x = int(input(f'Enter a number for number {count}: '))
        num.append(x)
except ValueError:
    print('there is no number in one input, please just enter just numbers')

print('\nThe sum of numbers you entered is', sum(num))