'''
Write a script that demonstrates a try/except/else.

'''


for i in range(3):
    try:
        user_input = input('enter a number : ')
        y = int(user_input)
    except ValueError as err:
        print(err)
    else:
        my_list = [1, 2, 3, 5, 42]
        x = lambda z: z**2 + y
        squared_list = [x(num) for num in my_list]
        print(my_list)
        print(squared_list)
