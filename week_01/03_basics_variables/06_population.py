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

total_population = current_population + round(3*year/ (birth-death+immigrates))

print(f'In three years the total population is will be {total_population}')

''' Testing other solutions
current_pop = 380123456

secondsperyear = 365*24*60*60*60


born = secondsperyear/6
died = secondsperyear/12
immigrants = secondsperyear/40

year1 = current_pop + born - died + immigrants
year2 = year1 + born - died + immigrants
year3 = year2 + born - died + immigrants

print(f"\n There is a population of {year1} after the first year, a population of {year2} after year 2, and a population of {year3} after year 3.")

print(f'\n{total_population} {year3}')


pop_now = 380123456
sec_per_yr = 60 * 60 * 24 * 365
pop_3yr = pop_now + (sec_per_yr / 120) * (120/6 - 120/12 + 120/40) * 3

print('\n', format(pop_3yr))
'''