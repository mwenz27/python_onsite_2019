'''
Using the PokéAPI https://pokeapi.co/docs/v2.html#pokemon
fetch the name and height of all 151 Pokémon of the main series.

Create a text document that describes each Pokémon using the information
available in the JSON response.
NOTE: only using 'height' is enough, but if you want more, go crazy.

BONUS: Using your script, create a folder and download the main 'front_default'.
       sprites for each Pokémon using requests into that folder.
       Name the files appropriately using the name data from your response.

'''

import requests
import os

flag = True
while flag:
    print('Running', end='')

    # with open('pokemon_height.txt', 'a') as fiw:
    #     fiw.write('Num\tName\tHeight(cm)' + '\n')

    for num in range(1, 10, 1):
        print('.', end='') # not needed in the code but added to look at the speed of each request
        url = f'https://pokeapi.co/api/v2/pokemon/{num}'
        r = requests.get(url)
        pokemon = r.json()
        name = pokemon['forms'][0]['name']
        height_cm = pokemon["height"]*10  # data in decimeters
        # with open('pokemon_height.txt', 'a') as fiw:
        #     fiw.write(f'{num}\t{name.capitalize()}\t{height_cm}' + '\n')

        url_image = f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/{num}.png'
        image_object = requests.get(url_image, allow_redirects=True)
        pathname = 'images/pokemon_images'
        os.path.dirname(pathname)
        with open(f'{num}_{name}_image.png', 'wb') as fiw:
            fiw.write(image_object)



    flag = False
    print()
else:
    print('Finished')

