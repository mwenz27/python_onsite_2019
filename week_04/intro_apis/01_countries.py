'''
Use the countries API https://restcountries.eu/ to fetch information
on your home country and the country you're currently in.

In your python program, parse and compare the data of the two responses:
* Which country has the larger population?
* How much does the are of the two countries differ?
* Print the native name of both countries, as well as their capitals

'''
from requests_html import HTMLSession

import random


def compareTwoCities():

    urlall = 'https://restcountries.eu/rest/v2/all'
    session = HTMLSession()  # HTMLSession keeps the active
    all_data = session.get(urlall).json() # converts jason into a dictionary

    city1_index = random.randint(1, len(all_data))
    city2_index = random.randint(1, len(all_data))

    while city1_index == city2_index:
        city2_index = random.randint(1, len(all_data))
    else:
        pass

    pop1 = all_data[city1_index]['population']
    pop2 = all_data[city2_index]['population']

    if pop1 > pop2:
        print(all_data[city1_index]['name'], 'has a higher population', all_data[city2_index]['name'], f'by {pop1 - pop2} people')
        print('The native name is', all_data[city1_index]['nativeName'], 'and the capital is', all_data[city1_index]['capital'], '\n')
    else:
        print(all_data[city2_index]['name'], all_data[city1_index]['population'], 'has a higher population',  all_data[city1_index]['name'], f'by {pop2 - pop1} peopleR')
        print('The native name is', all_data[city2_index]['nativeName'], 'and the capital is', all_data[city2_index]['capital'], '\n')


compareTwoCities()
