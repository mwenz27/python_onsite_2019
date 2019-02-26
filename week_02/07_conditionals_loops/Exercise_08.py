'''
Demonstrate the use of the "break" statement to exit a loop.

'''


for i in range(100):
    print(i, end=' ')
    if i == 80:
        break

print(f'\n the loop broke at 80 {i}')