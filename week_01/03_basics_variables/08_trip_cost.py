'''
Receive the following arguments from the user:
    - miles to drive
    - MPG of the car
    - Price per gallon of fuel

Display the cost of the trip in the console.

'''


def total_cost():
    distance = float(input('miles to drive : '))
    mpg = float(input('MPG of the car (average is 24mpg) : '))
    fuel_price = float(input('Price per gallon of fuel (range around 2.30-3.60) : '))
    cost_of_trip = distance/mpg*fuel_price
    #print(cost_of_trip)
    print(f'The total cost is {cost_of_trip}')

total_cost()


