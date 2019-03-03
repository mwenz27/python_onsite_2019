'''
Write a function that takes in a list and finds the max, min, average and sum.

'''

#TODO convert to floating point

def letsgo():
    input_list = []#float(input('Please enter a list of numbers with spaces ').split())
    input_list = [1.2, 2, 1, 3]
    lmax = max(input_list)
    lmin = min(input_list)
    lsum = sum(input_list)
    laverage = lsum / len(input_list)
    print(f'List {input_list}\n\tMax = {lmax}\n\tMin = {lmin}\n\tSum = {lsum}\n\tAverage = {laverage}')

letsgo()