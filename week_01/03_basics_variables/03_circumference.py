'''
Write the necessary code that prints out the area and circumference
of a circle with a radius of 3.14

'''

import math

def circle(radius):
    area = math.pi*(radius**2)
    circumference = 2*math.pi*radius
    print(f'The  area is {area} m^2 and {circumference}')


circle(3.14)