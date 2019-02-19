'''
In the U.S., if there is:
    - One person who is born every 6 seconds
    - One person who dies every 12 seconds
    - One person who immigrates every 40 seconds

Write the necessary code to display the total population
for the next 3 years (without a leap year).
Let's say the current population is 380,123,456.

'''

year = 60*60*60*24*365 # total time seconds, minutes, hours, hours in a day, days in a year
birth = 6
death = 12
immigrates = 40
current_population = 380123456

total_population = round(3*year/ (birth-death+immigrates))
difference = current_population - total_population

print(f'In three years the total population is {total_population}')

print(difference)

