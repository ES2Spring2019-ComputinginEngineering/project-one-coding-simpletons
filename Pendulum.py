#Ben Pradko and Rónán Gissler

import math as m
import numpy as np
import matplotlib.pyplot as plt
#we couldn't resist, it was meant to be. ;)
import scipy.signal as spicy

#calculates the angle of the pendulum from the acceleration values
#taken off the microbit.
def tilt(yAcc, xAcc):
    xdegrees = m.atan2(yAcc, xAcc)
    return xdegrees
   
#Returns the period and plots 4 graphs for each trial: 
#raw acceleration as a function of time, filtered
#acceleration as a function of time, position as a function
#of time, and filtered position as a function of time.
def data_collection(filename):
    
    fin = open(filename)
    
    #dataList is populated with x-acceleration, y-acceleration,
    #and time values in that order. 
    dataList = []
    
    #angleList is populated with angle values calculated from the 
    #x-acceleration and y-acceleration values from the microbit.
    angleList = []
    
    #timeList is populated from the time values recorded directly
    #onto the microbit.
    timeList = []
    
    #xAcc is populated from the x-acceleration values recorded
    #directly onto the microbit.
    xAcc = []
    
    #yAcc is populated from the y-acceleration values recorded
    #directly onto the microbit.
    yAcc = []
    
    #populates dataList
    for line in fin:
        dataList.append(line.split('\t'))
        
    #populates xAcc, yAcc, angleList, and timeList
    for dataPoint in dataList:
        xAcc.append(float(dataPoint[0]))
        yAcc.append(float(dataPoint[1]))
        angleList.append(tilt(float(dataPoint[1]), float(dataPoint[0])))
        timeList.append(int(dataPoint[2].strip())/1000)
        
    fin.close()

    #generates three new arrays with filtered (smoothed) angle data,
    #x-acceleration data, and y-acceleration. 
    filtangle = spicy.medfilt(angleList)
    filtxAcc = spicy.medfilt(xAcc)
    filtyAcc = spicy.medfilt(yAcc)

    #Both x- and y-acceleration as a function of time for real data
    plt.plot(timeList[50:], xAcc[50:], color = 'orange', label = 'X-Acceleration')
    plt.plot(timeList[50:], yAcc[50:], color = 'red', label = 'Y-Acceleration')
    plt.title('Raw Acceleration as a Function of Time', fontsize = 14)
    plt.xlabel('Time (s)', fontsize = 12)
    plt.ylabel('Acceleration (g)', fontsize = 12)
    plt.legend(loc = 7, fontsize = 12)
    plt.grid()
    plt.show()
        
    #Both x- and y- filtered acceleration as a function of time for real data
    plt.plot(timeList[50:], filtxAcc[50:], color = 'orange', label = 'X-Acceleration')
    plt.plot(timeList[50:], filtyAcc[50:], color = 'red', label = 'Y-Acceleration')
    plt.title('Filtered Acceleration as a Function of Time', fontsize = 14)
    plt.xlabel('Time (s)', fontsize = 12)
    plt.ylabel('Acceleration (g)', fontsize = 12)
    plt.legend(loc = 7, fontsize = 12)
    plt.grid()
    plt.show()
    
    #Angular position as a function of time for real data
    plt.plot(timeList, angleList, color = 'green')
    plt.title('Angular Position as a Function of Time', fontsize = 14)
    plt.xlabel('Time (s)', fontsize = 12)
    plt.ylabel('Angular Position (radians)', fontsize = 12)
    plt.grid()
    plt.show()
    
    #Filtered angular position as a function of time for real data
    plt.plot(timeList[50:], filtangle[50:], color = 'blue')
    plt.title('Filtered Angular Position as a Function of Time', fontsize = 14)
    plt.xlabel('Time (s)', fontsize = 12)
    plt.ylabel('Angular Position (radians)', fontsize = 12)
    plt.grid()
    plt.show()
    
    #peaksList is an array of indices at which peaks exist in filtangle
    peaksList = spicy.find_peaks(filtangle[70:255])
    
    timeArray = np.array(timeList)
    
    #PeriodPoints creates an array of time values at which there are peaks
    PeriodPoints = timeArray[peaksList[0]+70]
    
    #dt is populated with the time between each peak (1 period)
    dt = []
    
    #populates dt
    for i in range(len(PeriodPoints)-1):
        dt.append(PeriodPoints[i+1] - PeriodPoints[i])
        
    #The average period for each trial is calculated by averaging all
    #the times between peaks.
    avg_dt = np.average(dt)
    
    return avg_dt

#T returns the average period for all 5 trials for a given pendulum length
def T(array_Files):
    
    #avg_dts is populated with the average period calculated from each trial
    avg_dts = []
    
    #populates avg_dts
    for i in range(len(array_Files)):
        PeriodT = data_collection(array_Files[i])
        avg_dts.append(PeriodT)
        
    total_avg_dt = np.average(avg_dts)
    
    return total_avg_dt
