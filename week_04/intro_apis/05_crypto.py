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
import nomics
import time
import datetime

key = config['nomic']

api_key = key
nomics = nomics.Nomics(api_key)


time_minutes = 1
time_seconds = time_minutes*60
time_count = 0
btc_dict = {}

with open('05_time_btc-price_10_min_10_sec_int.txt', 'a') as fout:
    header = 'Date and time\t BTC price in USD'
    dash = '-'*len(header)
    fout.write(header + "\n"
               +dash + "\n")

    while time_count != time_seconds:
        coin_list = nomics.get_prices()
        time_stamp = datetime.datetime.now()

        for currency_price in coin_list:
            if currency_price['currency'] == 'BTC':
                print(time_stamp, currency_price['price'])
                line = str(time_stamp)+"\t"+str(currency_price['price'])
                fout.write(line + "\n")
                time_count += 10
                btc_dict[time_stamp] = currency_price['price']
        time.sleep(10)

    max_value = max(btc_dict.values())
    min_value = min(btc_dict.values())

    footer = f'BTC MIN/MAX values are , {min_value} / {max_value})'
    fout.write(footer + "\n")
