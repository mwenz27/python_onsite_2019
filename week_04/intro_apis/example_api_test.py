import requests

import random


params = {
    'type' : 'trivia',
    'notfound': 'floor'

}
#
# num = random.randint(1, 1000)
#
# url = f"http://numbersapi.com/{num}?{'&'.join(f'{k}={v}' for k, v in params.items())}"
# # url += '&'.join(f'{k}={v}' for k, v in params.items())
# print(url)
#
#
# r = requests.get(url)
# print(r.text)

for i in range(1000):
    num = i
    url = f"http://numbersapi.com/{num}?{'&'.join(f'{k}={v}' for k, v in params.items())}"
    r = requests.get(url)
    with open('numbers_api_0-1000.txt', 'a') as fiw:
        fiw.write(r.text+'\n')
