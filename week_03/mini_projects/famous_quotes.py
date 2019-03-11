'''
Using f-strings, print out the name, last name, and quote of each person in the given dictionary,
formatted like so:

"The inspiring quote" - Lastname, Firstname

'''

famous_quotes = [
    {"full_name": "Isaac Asimov", "quote": "I do not fear computers. I fear lack of them."},
    {"full_name": "Emo Philips", "quote": "A computer once beat me at chess, but it was no match for me at "
                                          "kick boxing."},
    {"full_name": "Edsger W. Dijkstra", "quote": "Computer Science is no more about computers than astronomy "
                                                 "is about telescopes."},
    {"full_name": "Bill Gates", "quote": "The computer was born to solve problems that did not exist before."},
    {"full_name": "Norman Augustine", "quote": "Software is like entropy: It is difficult to grasp, weighs nothing, "
                                               "and obeys the Second Law of Thermodynamics; i.e., it always increases."},
    {"full_name": "Nathan Myhrvold", "quote": "Software is a gas; it expands to fill its container."},
    {"full_name": "Alan Bennett", "quote": "Standards are always out of date.  That’s what makes them standards."}
]

for i in range(len(famous_quotes)): # the length of the famous quotes
    x = famous_quotes[i]['full_name'].split() # breaking the name into a list
    list_length = len(x)
    #print(list_length)
    #print(x)
    if list_length == 2: # if there are 2 characters in the surname
        surname_first = x[1] + ' ' + x[0]
        print(f"'{famous_quotes[i]['quote']}' - {surname_first} \n ")
    elif list_length == 3: # if there are 3 characters in the surname
        surname_first = x[2] + ' ' + x[1] + ' ' + x[0]
        print(f"'{famous_quotes[i]['quote']}' - {surname_first} \n ")

