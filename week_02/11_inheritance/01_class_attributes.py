
'''
Flush out the classes below with the following:

    - Add inheritance so that Class1 is inherited by Class2 and Class2 is inherited by Class3.
    - Follow the directions in each class to complete the functionality.



'''

class Class1:
    def __init__(self):
        self.x = 10
    # define an __init__() method that sets an attribute x


class Class2(Class1): # inheritance from class one
    def __init__(self):
        self.y = 20
        super().__init__()
    # define an __init__() method that sets an attribute y and calls the __init__() method of its parent


class Class3(Class2):
    def __init__(self):
        self.z = 30
        super().__init__()

    # define an __init__() method that sets an attribute z and calls the __init__() method of its parent


# create an object of each class and print each of its attributes
object_1 = Class1()
print(object_1.x)


object_2 = Class2()
print(object_2.x, object_2.y)

object_3 = Class3()
print(object_3.x, object_3.y, object_3.z)