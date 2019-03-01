# Ben Pradko and Ronan Gissler
# This code is for collecting the acceleration data of the motion

import math
import microbit

count = 0

def tilt(x, y):
    angle = math.atan2(y, x)
    return angle

fout = open('data_collection.txt', 'w')
while (count < 1000):
    x = microbit.accelerometer.get_x()
    y = microbit.accelerometer.get_y()
    angle = tilt(x, y)
    fout.write(str(angle) + '\n')
    microbit.sleep(10)
    count += 1
fout.close()
