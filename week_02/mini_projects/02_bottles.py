'''
--------------------------------------------------------
                99 BOTTLES OF BEER LYRICS
--------------------------------------------------------

https://www.reddit.com/r/beginnerprojects/comments/19kxre/project_99_bottles_of_beer_on_the_wall_lyrics/

-- GOAL --
Create a program that prints out every line to the song
"99 bottles of beer on the wall." This should be a pretty simple program,
so to make it a bit harder, here are some rules to follow.

-- RULES --
1) If you are going to use a list for all of the numbers,
    do not manually type them all in. Instead, use a built in function.
2) Besides the phrase "take one down," you may not type in any
    numbers/names of numbers directly into your song lyrics.
3) Remember, when you reach 1 bottle left, the word "bottles" becomes singular.
4) Put a blank line between each verse of the song.

'''

# list and function copied from stack overflow

num2words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', \
            19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', \
            50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', \
            90: 'Ninety', 0: 'Zero'}

def n2w(n):
    try:
        return num2words[n]
    except KeyError:
        try:
            return num2words[n-n % 10] + '-' + num2words[n % 10].lower()
        except KeyError:
            print('Number out of range ')


chorus = "You take one down, and pass it around.\n"

phrase_2 = 'bottles of beer on wall,'

phrase_3 = 'bottles of beer.'

phrase_4 = 'bottle of beer,'

phrase_5 = 'bottle of beer.'  # for the last beer


def bottle_song(amount_of_bottles):
    count = 0
    for i in range(amount_of_bottles, 0, -1): #
        number = str(n2w(i))
        print(number, phrase_2, number.lower(), phrase_3)
        print(chorus)
        count += 1
        if i == 1:
            print(number, phrase_4, number, phrase_5)

    if count >= 10:
        print('\nEveryone is totally drunk!!!')


bottle_song(99)
