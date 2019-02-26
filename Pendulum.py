#Ben Pradko and Rónán Gissler
import math as m
import numpy as np
import matplotlib.pyplot as plt
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
position = [(m.pi)/4]
velocity = [0]
acceleration = []

time = np.linspace(0, 10, 101)
acceleration_repeat = [4,3,2,1,0,-1,-2,-3,-4,-3,-2,-1,0,1,2,3]
acceleration = acceleration_repeat*6 + [4,3,2,1] 
print(acceleration)
i = 1
while i < (len(time)-1):
    positionf = system_update(acceleration[i-1],position[i-1],velocity[i-1],time[i-1],time[i])[0]
    velocityf = system_update(acceleration[i-1],position[i-1],velocity[i-1],time[i-1],time[i])[1]
    position.append(positionf)
    velocity.append(velocityf)
    #print_system(time[i], position[i], velocity[i])
    i += 1
print(count)
plt.plot(time[1:], position, color = 'magenta')
plt.title('Position as a function of time', fontsize = 14)
plt.xlabel('time', fontsize = 12)
plt.ylabel('position', fontsize = 12)
plt.show()

plt.plot(time[1:], velocity, color = 'cyan')
plt.title('Velocity as a function of time', fontsize = 14)
plt.xlabel('time', fontsize = 12)
plt.ylabel('velocity', fontsize = 12)
plt.show()

plt.plot(time[1:], acceleration, color = 'orange')
plt.title('Acceleration as a function of time', fontsize = 14)
plt.xlabel('time', fontsize = 12)
plt.ylabel('acceleration', fontsize = 12)
plt.show()

