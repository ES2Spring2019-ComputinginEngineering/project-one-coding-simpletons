#Ben Pradko and Rónán Gissler
from math import *
import numpy as np
'''
L = 1
m = 1
g = 9.81
I = (1/3)*m*(L**2)
T = L*(mg)*sin(position)
'''
def system_update(acceleration, position, velocity, t1, t2):
    dt = t2 - t1
    positionf = position + (velocity * dt)
    velocityf = velocity + (acceleration * dt)
    return positionf, velocityf

def print_system(time,position,velocity):
    print("TIME:     ", time)
    print("POSITION: ", position)
    print("VELOCITY: ", velocity, "\n")

#initial conditions:
position = [pi/4]
velocity = [0]
acceleration = [0]

time = np.linspace(0, 10, 10001)
print(len(time))

i = 1
while i < len(time):
    positionf, velocityf = system_update(acceleration[i],position[i-1],velocity[i-1],time[i-1],time[i])
    position.append(positionf)
    velocity.append(velocityf)
    #print_system(time[i],position[i],velocity[i])
    count = 0
    if((acceleration[len(acceleration)-1] == 0) and count%2 == 0):
        acceleration.append(i%5)
        count += 1
    elif(acceleration[len(acceleration)-1] == 5):
        acceleration.append(5-(i%5))
    elif((acceleration[len(acceleration)-1] == 0) and count%2 == 1):
        acceleration.append(-(i%5))
        count += 1
    elif(acceleration[len(acceleration)-1] == -5):
        acceleration.append(-5+(i%5))
    print(time[i],position[i])
    i += 1

#putting on our Big boy pants

