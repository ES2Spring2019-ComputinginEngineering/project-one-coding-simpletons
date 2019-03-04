# Data collection
# Ben Pradko and Ronan Gissler
import math as m
from microbit import *

def tilt(xAcc, yAcc):
    xdegrees = m.atan2(xAcc, yAcc)
    return xdegrees
fileName = 'data_collection.txt'
fout = open(fileName, 'w')
count = 0
switch = 0
while(count < 1000):
    count += 1
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    angle = tilt(x, y)
    time = count*10
    fout.write(str(angle) + '\n' + str(time) + '\n')
    sleep(10)
    if((count % 100 == 0) and (switch == 0)):
        display.show(Image.TRIANGLE)
        switch = 1
    elif((count % 100 == 0) and (switch == 1)):
        display.show(Image.SQUARE)
        switch = 0
display.show(Image.HEART)
fout.close()