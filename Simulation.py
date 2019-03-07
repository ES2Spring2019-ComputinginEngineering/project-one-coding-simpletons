#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 20:27:08 2019

@author: benpradko
"""

# SIMULATION
import math as m
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as spicy
 
  
#initial conditions:
def sim(L):
    g = 9.81
    w = m.sqrt(g/L)
    
    def angular_displacement(time, initial_position):
        return initial_position * m.cos(w * time)
    
    def angular_velocity(time, initial_position):
        return -w * initial_position * m.sin(w * time)
        
    def angular_acceleration(time, initial_position):
        return -(w**2) * initial_position * m.cos(w * time)
    
    position = [(m.pi)/4]
    velocity = [0]
    acceleration = []
    time = np.linspace(0, 10, 1000)
    posList = []
    velList = []
    accList = []
    dt = []
    for t in time:
        posList.append(angular_displacement(t, position[0]))
        velList.append(angular_velocity(t, position[0]))
        accList.append(angular_acceleration(t, position[0]))
    
    plt.plot(time, posList, color = 'magenta')
    plt.title('Position as a function of time', fontsize = 14)
    plt.xlabel('Time (ms)', fontsize = 12)
    plt.ylabel('Position (radians)', fontsize = 12)
    plt.grid()
    plt.show()
    
    plt.plot(time, velList, color = 'cyan')
    plt.title('Velocity as a function of time', fontsize = 14)
    plt.xlabel('Time (ms)', fontsize = 12)
    plt.ylabel('Velocity (rads/s)', fontsize = 12)
    plt.grid()
    plt.show()
    
    plt.plot(time, accList, color = 'orange')
    plt.title('Acceleration as a function of time', fontsize = 14)
    plt.xlabel('Time (ms)', fontsize = 12)
    plt.ylabel('Acceleration (rads/s^2)', fontsize = 12)
    plt.grid()
    plt.show()
    
    plt.plot(time, posList, color = 'magenta', label = 'position')
    plt.plot(time, velList, color = 'cyan', label = 'velocity')
    plt.plot(time, accList, color = 'orange', label = 'acceleration')
    plt.title('All together!')
    plt.xlabel('Time (ms)', fontsize = 12)
    plt.legend(loc = 2, fontsize = 12)
    plt.grid()
    plt.show()
    
    
    peaksList = spicy.find_peaks(posList)
    timeArray = np.array(time)
    Ppoints = timeArray[peaksList[0]]
    
    for i in range(len(Ppoints)-1):
        dt.append(Ppoints[i+1] - Ppoints[i])
    avg_dt = np.average(dt)
    return avg_dt