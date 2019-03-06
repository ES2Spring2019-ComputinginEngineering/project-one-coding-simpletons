# Data collection
# Ben Pradko and Ronan Gissler
import math as m
import random as rand
from microbit import *

fileName = 'data_collection' + str(rand.randint(0,999)) + '.txt'
fout = open(fileName, 'w')
count = 0
switch = 0
runningTime = 0
while(count <= 500):
    time0 = running_time()
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    fout.write(str(x,y) + '\t')
    sleep(10)
    if((count % 100 == 0) and (switch == 0)):
        display.show(Image.TRIANGLE)
        switch = 1
    elif((count % 100 == 0) and (switch == 1)):
        display.show(Image.SQUARE)
        switch = 0
    count += 1
    time1 = running_time()
    runningTime += time1 - time0
    fout.write(str(runningTime) + '\n')
display.show(Image.HEART)
fout.close()