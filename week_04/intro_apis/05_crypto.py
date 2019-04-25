'''
http://docs.nomics.com/
Using the nomics API, repeatedly fetch the price of Bitcoin for a duration of 10 minutes.
Store each value in a dictionary that uses the time of query as a key.

After the script stopped running, determine programmatically at what query time the price
was the highest, and when the lowest.

HINTS:
- request an API key first and remember to include it in your queries
- the /prices endpoint of the nomics API can be used for achieving this task
- remember to use packages from the standard library, e.g. for time keeping and dates

BONUS: Explore the logging package for easier tracking

'''

from secrets3 import config
import requests
import time

import urllib.request

from pprint import pprint

key = config['nomic']

# url = f"https://api.nomics.com/v1/prices?{key}"
# print(urllib.request.urlopen(url).read())


# url = "https://api.nomics.com/v1/markets/prices?key=" + key   # "&currency=BTC"
# prices = requests.get(url)
# pprint(prices.json())




import nomics
api_key = key
nomics = nomics.Nomics(api_key)

# x = nomics.get_prices()
# pprint(x) #prints all currency pairs

time_minutes = 3
time_seconds = time_minutes*60
time_count = 0
btc_dict = {}
while time_count != time_seconds:
    x = nomics.get_prices()
    time_stamp = time.time()
    time.sleep(10)
    with open('05_time_btc-price_10_min_10_sec_int.txt', 'a') as fout:
        for currency_price in x:
            if currency_price['currency'] == 'BTC':
                # print(time_stamp, currency_price['price'])
                line = str(time_stamp)+" "+str(currency_price['price'])
                fout.write(line + "\n")
                time_count += 10
                btc_dict[time_stamp] = currency_price['price']

max_value = max(btc_dict.values())
min_value = min(btc_dict.values())
print('BTC MIN/MAX values are ', min_value,'/', max_value)
