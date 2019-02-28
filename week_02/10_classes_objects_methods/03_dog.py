'''
Building on the dog exercise in the previous section:

1. Create a dog class and make the functions from the last class methods of the dog class.


2. Add an __init__() method that sets the following attributes:

    - name
    - color
    - age
    - is_hungry (should be a boolean)
    - percent_full

    Note: is_hungry should default to False, and percent_full should default to 100.

3. Change the sleep() method so that when the method is called, the attribute is_hungry is set to True
    and the attribute percent_full is decremented by 20 percent.

4. Change the eat() method so that when the method is called, the attribute is_hungry is set to False
    and the attribute percent full is incremented to 100.

5. Add a __str__() method to print out all the information about the dog.

6. Create at least two objects of the dog class to demonstrate the functionality.


'''

'''
2. Add an __init__() method that sets the following attributes:

    - name
    - color
    - age
    - is_hungry (should be a boolean)
    - percent_full
'''


class Dog:
    def __init__(self, name, colour, age, hungry=True, energy=100):
        self.name = name
        self.colour = colour
        self.age = age
        self.hungry = hungry
        self.energy = energy

#3. Change the sleep() method so that when the method is called, the attribute is_hungry is set to True
#   and the attribute percent_full is decremented by 20 percent.

    def sleep(self):
        self.hungry = False
        self.energy -= 20

#4. Change the eat() method so that when the method is called, the attribute is_hungry is set to False
#    and the attribute percent full is incremented to 100.'''

    def eat(self):
        self.hungry = False
        while self.energy < 100:
            self.energy += 2
            print(f'{self.energy}', end=' ')
        else:
            print('It\'s full')
            self.hungry = True

    def __str__(self):
        return (f"{self.name} is {self.colour} and is {self.age} years old. The dog has "
              f"{self.energy} % energy.")

rex = Dog('rex', 'black', 12)

print(rex.hungry)
print(rex.name)
print(rex.colour)
print(rex.age)
print(rex.energy)
rex.sleep()
print(rex.energy)
rex.eat()
print(rex)

