'''
Pokemon rpg game


to become in the game

To start the game  I will initialise character's name than that will have its own attributes and properties

 following this object will move around interacting wild grass area
  for a random period of time  and will attack  Pokémon


 will will will willafter attacking it will have the ability to capture if the Pokémon is
very low on health.

 this will be the start,  that I would consider having other objects battling the opponent



'''

#
#
#
# import requests
#
# flag = True
# while flag:
#     print('Running', end='')
#
#     # with open('pokemon_height.txt', 'a') as fiw:
#     #     fiw.write('Num\tName\tHeight(cm)' + '\n')
#
#     for num in range(1, 152, 1):
#         print('.', end='') # not needed in the code but added to look at the speed of each request
#         url = f'https://pokeapi.co/api/v2/pokemon/{num}'
#         r = requests.get(url)
#         pokemon = r.json()
#         name = pokemon['forms'][0]['name']
#         height_cm = pokemon["height"]*10  # data in decimeters
#         with open('pokemon_height.txt', 'a') as fiw:
#             fiw.write(f'{num}\t{name.capitalize()}\t{height_cm}' + '\n')
#
#     flag = False
#     print()
# else:
#     print('Finished')
#
class  Player():
    def __init__(self,  age,  height,  potions=0):
        self.age = age
        self.height = height
        self.backpack = backpack

    def seeProf(self):
        self.pokeball = 3

class wildPokemon:
    def __init__(self, level=0, health=100, attack, defence):
        self.level = level
        self.health =  health
        self.attack = attack
        self.defence = defence


class Opponent(Player):
    pass