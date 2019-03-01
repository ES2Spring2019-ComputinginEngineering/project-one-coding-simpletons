#Ben Pradko and Rónán Gissler
import math as m
import numpy as np
import matplotlib.pyplot as plt

L = 0.3
g = 9.81
w = m.sqrt(g/L)

def angular_displacement(time, initial_position, angular_velocity):
    return initial_position * m.cos(angular_velocity * time)

def angular_velocity(time, initial_position, angular_velocity):
    return -w * initial_position * m.sin(angular_velocity * time)
    
def angular_acceleration(time, initial_position, angular_velocity):
    return -(w**2) * initial_position * m.cos(angular_velocity * time)

#initial conditions:
position = [(m.pi)/4]
velocity = [0]
acceleration = []

time = np.linspace(0, 10, 1000)

x = time
y1 = []
y2 = []
y3 = []
for t in x:
    y1.append(angular_displacement(t, position[0], w))
    y2.append(angular_velocity(t, position[0], w))
    y3.append(angular_acceleration(t, position[0], w))
    
plt.plot(x, y1, color = 'magenta')
plt.title('Position as a function of time', fontsize = 14)
plt.xlabel('time', fontsize = 12)
plt.ylabel('position', fontsize = 12)
plt.grid()
plt.show()

plt.plot(x, y2, color = 'cyan')
plt.title('Velocity as a function of time', fontsize = 14)
plt.xlabel('time', fontsize = 12)
plt.ylabel('velocity', fontsize = 12)
plt.grid()
plt.show()

plt.plot(x, y3, color = 'orange')
plt.title('Acceleration as a function of time', fontsize = 14)
plt.xlabel('time', fontsize = 12)
plt.ylabel('acceleration', fontsize = 12)
plt.grid()
plt.show()

plt.plot(x, y1, color = 'magenta', label = 'position')
plt.plot(x, y2, color = 'cyan', label = 'velocity')
plt.plot(x, y3, color = 'orange', label = 'acceleration')
plt.title('All together!')
plt.xlabel('time', fontsize = 12)
plt.legend(loc = 2, fontsize = 12)
plt.grid()
plt.show()

#Data collection
fin = open('data_collection.txt')
dataList = []
for angle in fin:
    dataList.append(float(angle.strip()))
fin.close()
    
plt.plot(x, dataList, color = 'green')
plt.title('Position as a function of time', fontsize = 14)
plt.xlabel('time', fontsize = 12)
plt.ylabel('position', fontsize = 12)
plt.grid()
plt.show()
'''
plt.plot(x, y5, color = 'red')
plt.title('Velocity as a function of time', fontsize = 14)
plt.xlabel('time', fontsize = 12)
plt.ylabel('velocity', fontsize = 12)
plt.grid()
plt.show()

plt.plot(x, y6, color = 'blue')
plt.title('Acceleration as a function of time', fontsize = 14)
plt.xlabel('time', fontsize = 12)
plt.ylabel('acceleration', fontsize = 12)
plt.grid()
plt.show()

plt.plot(x, y4, color = 'green', label = 'position')
plt.plot(x, y5, color = 'red', label = 'velocity')
plt.plot(x, y6, color = 'blue', label = 'acceleration')
plt.title('All together!')
plt.xlabel('time', fontsize = 12)
plt.legend(loc = 2, fontsize = 12)
plt.grid()
plt.show()
'''