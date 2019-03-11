'''
Write a lambda function that takes in 3 numbers and returns the sum of the numbers.

'''
def answer_sum2(x,y,z):
    sum = x+y+z
    return sum

answer_sum2(1,2,3)

print(answer_sum2(1,2,3))

answer_sum = lambda x, y, z: x+y+z

print(answer_sum(1, 2, 3))
