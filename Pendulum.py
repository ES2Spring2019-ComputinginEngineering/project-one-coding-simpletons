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
        timeList.append(int(dataPoint[2].strip()))
    fin.close()


    filtangle = spicy.medfilt(angleList)


    plt.plot(timeList[50:], xAcc[50:], color = 'orange')
    plt.plot(timeList[50:], yAcc[50:], color = 'red')
    plt.title('Raw Acceleration as a function of time', fontsize = 14)
    plt.xlabel('time', fontsize = 12)
    plt.ylabel('acceleration', fontsize = 12)
    plt.grid()
    plt.show()
    
    
    plt.plot(timeList, angleList, color = 'green')
    plt.title('Position as a function of time', fontsize = 14)
    plt.xlabel('time', fontsize = 12)
    plt.ylabel('position', fontsize = 12)
    plt.grid()
    plt.show()
    
    
    plt.plot(timeList[50:], filtangle[50:], color = 'blue')
    plt.title('Filtered Position as a function of time', fontsize = 14)
    plt.xlabel('time', fontsize = 12)
    plt.ylabel('position', fontsize = 12)
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
    return avg_dt
