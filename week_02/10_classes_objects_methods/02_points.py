'''
Work through the chapter "Classes and Objects" in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2016.html and
build out the Point class example.

'''


class Point:
    def __init__(self, x = None, y = None):
        self.x = x
        self.y = y

    def distance_between_points(self):
        a = self.x
        b = self.y
        c = (a**2 + b**2)**0.5
        return f'The distance between points {a}, {b} is {c}'


class Rectangle:
    def __init__(self, width=None, height=None , corner=Point()):
        self.width = width
        self.height = height
        self.corner = corner # corner is a Point object that specifies the lower-left corner

    def find_centre(self):
        x = self.corner.x + self.width/2
        y = self.corner.y + self.height/2
        return f'centre point is {x} and {y}'


def find_centre2(width, hieght, corner):
    x1 = width/2 + corner.x
    y1 = hieght/2 + corner.y
    return f'centre point is {x1} and {y1}'



mark = Point(3, 4)
print(mark.distance_between_points())

box = Rectangle()
box.width = 100
box.height = 200
box.corner = Point()
box.corner.x = 0
box.corner.y = 0


print(box.find_centre()) # finding the centre using a method in my class already created


print(find_centre2(100, 200, Point(0,0)) )


