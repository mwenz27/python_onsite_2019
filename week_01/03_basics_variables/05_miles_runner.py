'''
If a runner runs 12 kilometers in 30 minutes and 30 seconds.
What is his/her average speed in miles per hour. (Tip: 1 mile = 1.6 km)

'''
distance = 12/1.6# km to miles
print(distance)
time = (30*60 + 30)/60/60 # 30 min and 30 seconds to hours

speed = distance/time

print(speed)