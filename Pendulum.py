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

time = np.linspace(0, 10, 10001)
print(len(time))

i = 0
while i < (len(time)-1):
    #print_system(time[i],position[i],velocity[i])
    if (len(time)%20 == 1):
        acceleration.extend([4,3,2,1,0,0-1,-2,-3,-4,-4,-3,-2,-1,0,1,2,3,4])
    positionf, velocityf = system_update(acceleration[i],position[i-1],velocity[i-1],time[i-1],time[i])
    position.append(positionf)
    velocity.append(velocityf)
    i += 1
    
plt.plot(time, position, color = 'magenta')
plt.title('Position as a function of time', fontsize = 14)
plt.xlabel('time', fontsize = 12)
plt.ylabel('position', fontsize = 12)
plt.show()

plt.plot(time, velocity, color = 'cyan')
plt.title('Velocity as a function of time', fontsize = 14)
plt.xlabel('time', fontsize = 12)
plt.ylabel('velocity', fontsize = 12)
plt.show()

plt.plot(time, acceleration, color = 'yellow')
plt.title('Acceleration as a function of time', fontsize = 14)
plt.xlabel('time', fontsize = 12)
plt.ylabel('acceleration', fontsize = 12)
plt.show()
#putting on our Big boy pants

