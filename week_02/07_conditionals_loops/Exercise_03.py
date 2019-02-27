'''
Using a "for-loop", print out all even numbers from 1-100.

'''
for i in range(0, 102):
    if i % 2 == 0:
        print(i, end=' ')
print('\n')

for i in range(0,102, 2):
    print(i, end=' ')