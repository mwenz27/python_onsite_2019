'''
Write a script that connects to the http://numbersapi.com/ and fetches trivia on all
numbers from 0 through 100.

Store the responses in a new JSON file called numbers.json

BONUS:
* fetch information of all the prime numbers from 1-1000
* cycle through the different endpoints the API provides (trivia, math, date, year)
  in a way that they change in binary chunks, e.g.:
  - the info on the first 2 numbers are of type trivia
  - info on the next 4 numbers are of type math
  - the next 8 are on dates
  - etc. (cycle back to the trivia after year)

'''
import requests
import time

params = {
    'type' : 'trivia',
    'notfound': 'floor'
}

with open('numbers_api_0-100.txt', 'a') as fiw: #Opening brackets
    fiw.write('{')

for i in range(100):
    num = i
    url = f"http://numbersapi.com/{num}?{'&'.join(f'{k}={v}' for k, v in params.items())}"
    time.sleep(2) # sleeping before request to not get a bad gateway
    r = requests.get(url)
    with open('numbers_api_0-100.txt', 'a') as fiw: #
        fiw.write(r.text+'\n')

with open('numbers_api_0-100.txt', 'a') as fiw: #Closing brackets
    fiw.write('}')

## slice i characters to the right

# add colon in the middle

# add the value by using a key value pari