'''
--------------------------------------------------------
                PROGRAMMED SONG LYRICS
--------------------------------------------------------

Programmatically create your own song lyrics with multiple verses,
interlaced with a repeating chorus.

Train using string methods and loops on an open-end mini-project!

- use one block of text as verse input (hint: linebreaks can be helpful!)
- use a for loop for creating the full lyrics

'''

chorus = '''\nBye, bye Miss American Pie
Drove my Chevy to the levee but the levee was dry
Them good ole boys were drinking whiskey and rye
And singin' this'll be the day that I die
This'll be the day that I die'''


part_1 = '''\nA long long time ago
I can still remember how
That music used to make me smile
And I knew if I had my chance
That I could make those people dance
And maybe they'd be happy for a while
\nBut February made me shiver
With every paper I'd deliver
Bad news on the doorstep
I couldn't take one more step
\nI can't remember if I cried
When I read about his widowed bride
Something touched me deep inside
The day the music died
So'''


part_2 = '''\nDid you write the book of love
And do you have faith in God above
If the Bible tells you so?
Do you believe in rock and roll?
Can music save your mortal soul?
And can you teach me how to dance real slow?
\nWell, I know that you're in love with him
'Cause I saw you dancin' in the gym
You both kicked off your shoes
Man, I dig those rhythm and blues
\nI was a lonely teenage broncin' buck
With a pink carnation and a pickup truck
But I knew I was out of luck
The day the music died
I started singin\''''

part_3 = '''\nNow, for ten years we've been on our own
And moss grows fat on a rolling stone
But, that's not how it used to be
\nWhen the jester sang for the king and queen
In a coat he borrowed from James Dean
And a voice that came from you and me
\nOh and while the king was looking down
The jester stole his thorny crown
The courtroom was adjourned
No verdict was returned
\nAnd while Lennon read a book on Marx
The quartet practiced in the park
And we sang dirges in the dark
The day the music died
We were singin\''''

part_4 = '''\nHelter skelter in a summer swelter
The birds flew off with a fallout shelter
Eight miles high and falling fast
\nIt landed foul on the grass
The players tried for a forward pass
With the jester on the sidelines in a cast
\nNow the half-time air was sweet perfume
While sergeants played a marching tune
We all got up to dance
Oh, but we never got the chance
\n\'Cause the players tried to take the field
The marching band refused to yield
Do you recall what was revealed
The day the music died?
We started singin\''''

part_5 = '''\nOh, and there we were all in one place
A generation lost in space
With no time left to start again
\nSo come on Jack be nimble, Jack be quick
Jack Flash sat on a candlestick
\'Cause fire is the devil's only friend
\nOh and as I watched him on the stage
My hands were clenched in fists of rage
No angel born in Hell
Could break that Satan's spell
\nAnd as the flames climbed high into the night
To light the sacrificial rite
I saw Satan laughing with delight
The day the music died
He was singin\''''

part_6 = '''\nI met a girl who sang the blues
And I asked her for some happy news
But she just smiled and turned away
\nI went down to the sacred store
Where I'd heard the music years before
But the man there said the music wouldn't play
\nAnd in the streets the children screamed
The lovers cried, and the poets dreamed
But not a word was spoken
The church bells all were broken
\nAnd the three men I admire most
The Father, Son, and the Holy Ghost
They caught the last train for the coast
The day the music died
And they were singing'''

part_7 ='''\nThey were singing
Bye, bye Miss American Pie
Drove my Chevy to the levee but the levee was dry
Them good ole boys were drinking whiskey and rye
Singin' this'll be the day that I die'''

list_song = []

# TODO how to make a name into parts

# for i in range(1,8):
#     string_name = f'part_{i}'
#     string_name = eval(string_name)
#     print(string_name)

list_song_2 = [part_1, part_2, part_3, part_4, part_5, part_6, part_7]


def song():
    for i in list_song_2:
        print(i)
        print(chorus)


song()

