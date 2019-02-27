'''
The following functions are all intended to check whether a string
contains any lowercase letters, but at least some of them are wrong.
For each function, write its docstring to describe what the function
actually does (assuming that the parameter is a string).



'''

# TODO write each docstring

def any_lowercase1(s):
    for c in s:
        print(c)
        if c.islower():
            return True
        else:
            return False

#print(any_lowercase1('this is a test'))
#print(any_lowercase1('This Ts a Test'))

def any_lowercase2(s):
'''
looks at the letter of the word
'''
    for c in s:
        print(c)
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

any_lowercase1('words in a string')

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True
