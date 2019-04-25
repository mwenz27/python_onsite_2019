'''
Using the Chuck Norris API in combination with the datamuse API
( https://api.chucknorris.io/ - https://www.datamuse.com/api/ )

* Query the chucknorris api for a sentence
* Use the last word of that sentence to send a query to the Datamuse API
  and use the rel_rhy (or rel_nry) query parameter to fetch a word that rhymes
* Repeat a coupe of times and store the sentences and rhyme words
* Synthesize the collected results into an avant-garde poem and present it to class ;)

'''


from requests_html import HTMLSession
from pprint import pprint

with open('04_chucknorris_text_file.txt', 'a') as fout:
    url = 'https://api.chucknorris.io/jokes/random'
    session = HTMLSession()  # HTMLSession keeps the active
    chuck_data = session.get(url).json()  # converts jason into a dictionary
    url_rhy = 'https://api.datamuse.com/words?rel_rhy='
    pprint(chuck_data)
    print(chuck_data['value'])
    sentence = chuck_data['value']
    list_sentence = sentence.split()
    fout.write('\n' + sentence )
    last_word = list_sentence[len(list_sentence)-1].rstrip(".!'")
    # print(last_word)
    session2 = HTMLSession()
    rhymes_html = session2.get(f'{url_rhy}{last_word}').json()
    # print(f'words that rhyme with {last_word}')
    fout.write('\n' + f'Words that rhyme with {last_word}' + '\n')
    for count, rhyme_word in enumerate(rhymes_html, 1):
        # print(count, ":", rhyme_word['word'])
        string = str(count) + " : " + rhyme_word['word'].capitalize() + '\n'
        fout.write(string)


