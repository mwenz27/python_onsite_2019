'''
Take two numbers from the user, an upper and lower bound. Using a loop, calculate the sum
	of numbers from the lower bound to the upper bound. Also, calculate the average of numbers.
	Print the results to the console.

	For example, if a user enters 1 and 100, the output should be:
		The sum is: 5050
		The average is: 50.5
'''


def range_sum(lower, upper):
    total = 0
    for i in range(lower, upper + 1, 1):  # +1 since range is inclusive
        total += i
    average = total / (upper - lower + 1)
    return print(f'the sum is {total} and average is {round(average, 1)}')


x = (input("Enter two numbers with spaces (lower and upper): ")).split()


range_sum(int(x[0]), int(x[1]))
