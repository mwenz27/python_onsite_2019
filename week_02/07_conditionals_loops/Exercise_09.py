'''
Use a nested loop to generate a multiplication table for numbers 1-10.
The output should look something like this:
	1 |2 |3 |4 |5 |6 |7 |8 |9 |10 |
	2 |4 |6 |8 |10|12|14|16|18|20 |
	3 |6 |9 |12|15|18|21|24|27|30 |
	4 |8 |12|16|20|24|28|32|36|40 |
	5 |10|15|20|25|30|35|40|45|50 |
	6 |12|18|24|30|36|42|48|54|60 |
	7 |14|21|28|35|42|49|56|63|70 |
	8 |16|24|32|40|48|56|64|72|80 |
	9 |18|27|36|45|54|63|72|81|90 |
	10|20|30|40|50|60|70|80|90|100|

'''

new_list = []
count_list = list(range(10, 110, 10))
count = 0


for i in range(1, 11):  # 11 is used since range is inclusive
    for j in range(i, i * 11, i):
        count += 1
        if j < 10:
            print(j, end='  |')  # Two spaces for one digit
        else:
            print(j, end=' |')  # one space for two digits

        if count in count_list:  # at the end of the row need to break the previous print function
            print('')


# TODO  the tenth row has no spaces  add a condition to break it up