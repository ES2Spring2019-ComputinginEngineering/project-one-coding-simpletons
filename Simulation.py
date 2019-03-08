#Ben Pradko and Rónán Gissler

# SIMULATION
import math as m
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as spicy
 
#Returns the period and plots 4 graphs for each trial: 
#angular position as a function of time, angular
#velocity as a function of time, angular acceleration as a function
#of time, and all 3 together as a function of time.
def sim(L):
    
    g = 9.81
    
    #angular frequency
    w = m.sqrt(g/L)
    
    def angular_displacement(time, initial_position):
        return initial_position * m.cos(w * time)
    
    def angular_velocity(time, initial_position):
        return -w * initial_position * m.sin(w * time)
        
    def angular_acceleration(time, initial_position):
        return -(w**2) * initial_position * m.cos(w * time)
    
    time = np.linspace(0, 10, 1000)
    
    #position is populated with angular position values, given the initial starting point
    posList = []
    
    #velocity is populated with angular velocity values, given the initial starting point
    velList = []
    
    #acceleration is populated with angular acceleration values
    accList = []

    #populates posList, velList, and accList
    for t in time:
        posList.append(angular_displacement(t, (m.pi)/4))
        velList.append(angular_velocity(t, (m.pi)/4))
        accList.append(angular_acceleration(t, (m.pi)/4))
    
    #angular position as a function of time for simulated data
    plt.plot(time, posList, color = 'magenta')
    plt.title('Angular Position as a function of time', fontsize = 14)
    plt.xlabel('Time (s)', fontsize = 12)
    plt.ylabel('Angular Position (radians)', fontsize = 12)
    plt.grid()
    plt.show()
    
    #angular velocity as a function of time for simulated data
    plt.plot(time, velList, color = 'cyan')
    plt.title('Angular Velocity as a function of time', fontsize = 14)
    plt.xlabel('Time (s)', fontsize = 12)
    plt.ylabel('Angular Velocity (rads/s)', fontsize = 12)
    plt.grid()
    plt.show()
    
    #angular acceleration as a function of time for simulated data
    plt.plot(time, accList, color = 'orange')
    plt.title('Angular Acceleration as a function of time', fontsize = 14)
    plt.xlabel('Time (s)', fontsize = 12)
    plt.ylabel('Angular Acceleration (rads/s^2)', fontsize = 12)
    plt.grid()
    plt.show()
    
    #all 3 together on the same plot
    plt.plot(time, posList, color = 'magenta', label = 'position')
    plt.plot(time, velList, color = 'cyan', label = 'velocity')
    plt.plot(time, accList, color = 'orange', label = 'acceleration')
    plt.title('All together!')
    plt.xlabel('Time (s)', fontsize = 12)
    plt.legend(loc = 2, fontsize = 12)
    plt.grid()
    plt.show()
    
    #dt is populated with the time between each peak (1 period)
    dt = []
    
    #peaksList is an array of indices at which peaks exist in posList
    peaksList = spicy.find_peaks(posList)
    
    timeArray = np.array(time)
    
    #PeriodPoints creates an array of time values at which there are peaks
    PeriodPoints = timeArray[peaksList[0]]
    
    #populates dt
    for i in range(len(PeriodPoints)-1):
        dt.append(PeriodPoints[i+1] - PeriodPoints[i])
        
    avg_dt = np.average(dt)
    
    return avg_dt