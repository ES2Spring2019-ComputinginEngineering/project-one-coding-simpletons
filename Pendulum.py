#Ben Pradko and Rónán Gissler
import math as m
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as spicy

def tilt(yAcc, xAcc):
    xdegrees = m.atan2(yAcc, xAcc)
    return xdegrees
   

#Data collection
def data_collection(filename):
    fin = open(filename)
    dataList = []
    angleList = []
    timeList = []
    xAcc = []
    yAcc = []
    for line in fin:
        dataList.append(line.split('\t'))
    for dataPoint in dataList:
        xAcc.append(float(dataPoint[0]))
        yAcc.append(float(dataPoint[1]))
        angleList.append(tilt(float(dataPoint[1]), float(dataPoint[0])))
        timeList.append(int(dataPoint[2].strip())/1000)
    fin.close()

    filtangle = spicy.medfilt(angleList)

    plt.plot(timeList[50:], xAcc[50:], color = 'orange')
    plt.plot(timeList[50:], yAcc[50:], color = 'red')
    plt.title('Raw Acceleration as a Function of Time', fontsize = 14)
    plt.xlabel('Time (s)', fontsize = 12)
    plt.ylabel('Acceleration (g)', fontsize = 12)
    plt.grid()
    plt.show()
    
    
    plt.plot(timeList, angleList, color = 'green')
    plt.title('Position as a Function of Time', fontsize = 14)
    plt.xlabel('Time (s)', fontsize = 12)
    plt.ylabel('Position (radians)', fontsize = 12)
    plt.grid()
    plt.show()
    
    
    plt.plot(timeList[50:], filtangle[50:], color = 'blue')
    plt.title('Filtered Position as a Function of Time', fontsize = 14)
    plt.xlabel('Time (s)', fontsize = 12)
    plt.ylabel('Position (radians)', fontsize = 12)
    plt.grid()
    plt.show()
    
    peaksList = spicy.find_peaks(filtangle[70:255])
    timeArray = np.array(timeList)
    Ppoints = timeArray[peaksList[0]+70]
    
    dt = []
    for i in range(len(Ppoints)-1):
        dt.append(Ppoints[i+1] - Ppoints[i])
    avg_dt = np.average(dt)
    return avg_dt


def T(Length, array_Files):
    avg_dt = []
    for i in range(len(array_Files)):
        PeriodT = data_collection(array_Files[i])
        avg_dt.append(PeriodT)
    total_avg_dt_ms = np.average(avg_dt)
    total_avg_dt = (total_avg_dt_ms)
    return total_avg_dt
