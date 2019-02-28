'''
Work through the chapter "Classes and Objects" in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2016.html and
build out the Point class example.

'''


class Point():
    '''this a doc string'''
    def __init__(self):
        self.x = 3
        self.y = 4


vector = Point()  # using the brackets to call the class

print(vector.x)

print(vector.y)