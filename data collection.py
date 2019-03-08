# Ben Pradko and Ronan Gissler

import math as m
import random as rand
from microbit import *

#generates a new file name each time (hopefully) using the addition of a random number
fileName = 'data_collection' + str(rand.randint(0,999)) + '.txt'

fout = open(fileName, 'w')

#used to limit the while loop used to record data
count = 0

#binary variable, used to change the image displayed by the microbit,
#indicating that a second of data collection has passed
switch = 0

#used to indicate the time intervals at which data is recorded
runningTime = 0

while(count <= 500):

    time0 = running_time()

    x = accelerometer.get_x()
    y = accelerometer.get_y()

    #adds x-acceleration and y-acceleration to the data collection file
    fout.write(str(x) + '\t' + str(y) + '\t')

    #waits 10 ms
    sleep(10)

    #displays after 1 and 3 sec
    if((count % 100 == 0) and (switch == 0)):
        display.show(Image.TRIANGLE)
        switch = 1

    #displays after 2 and 4 sec
    elif((count % 100 == 0) and (switch == 1)):
        display.show(Image.SQUARE)
        switch = 0
    count += 1

    time1 = running_time()

    #adds the elapsed time to the total running times
    runningTime += time1 - time0

    #adds the time value to the data collection file
    fout.write(str(runningTime) + '\n')

#displays when data collection is complete
display.show(Image.HEART)

fout.close()