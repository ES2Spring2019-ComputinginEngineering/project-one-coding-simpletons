#Ben Pradko and Rónán Gissler

import matplotlib.pyplot as plt
from Pendulum import *
from Simulation import *

#L1, L2, L3, L4, and L5 are the five different lengths we measured for our experimental pendulums.
L1 = .39
L2 = .38
L3 = .37
L4 = .29
L5 = .17
Lengths = [L1, L2, L3, L4, L5]

#Each list of files below includes 5 trials for each pendulum length.
Files1 = ['L11.txt', 'L12.txt', 'L13.txt', 'L14.txt', 'L15.txt']  # Matches with L5
Files2 = ['L21.txt', 'L22.txt', 'L23.txt', 'L24.txt', 'L25.txt']  # Matches with L4
Files3 = ['L31.txt', 'L32.txt', 'L33.txt', 'L34.txt', 'L35.txt']  # Matches with L3
Files4 = ['L41.txt', 'L42.txt', 'L43.txt', 'L44.txt', 'L45.txt']  # Matches with L2
Files5 = ['L51.txt', 'L52.txt', 'L53.txt', 'L54.txt', 'L55.txt']  # Matches with L1

#simList is a list of pendulum periods at different lengths for our simulated data.
#By calling sim each time within the list, the graphs for each simulation are plotted. 
simList = [sim(L1), sim(L2), sim(L3), sim(L4), sim(L5)]

#PeriodList is a list of the average pendulum periods from the 5 different trials at
#each pendulum length
#By calling T each time within the list, the graphs of every trial for each
#pendulum length are plotted. 
PeriodList = [T(Files5), T(Files4), T(Files3), T(Files2), T(Files1)]

#Simulated and real periods plotted versus pendulum lengths (regular data)
plt.plot(Lengths, simList, color = 'magenta', label = 'Simulation')
plt.plot(Lengths, PeriodList, color = 'cyan', label = 'Real World')
plt.title('Simulated and Real Periods as a Function of Pendulum Length\n')
plt.xlabel('Length (m)', fontsize = 12)
plt.ylabel('Period (s)', fontsize = 12)
plt.legend(loc = 2, fontsize = 12)
plt.grid()
plt.show()

#Simulated and real periods plotted versus pendulum lengths (logarithmic data)
plt.plot(Lengths, simList, color = 'magenta', label = 'Simulation')
plt.plot(Lengths, PeriodList, color = 'cyan', label = 'Real World')
plt.title('Simulated and Real Periods as a Function of Pendulum Length\n (logarithmic)\n')
plt.xlabel('Length (m)', fontsize = 12)
plt.ylabel('Period (s)', fontsize = 12)
plt.legend(loc = 2, fontsize = 12)
plt.xscale('log')
plt.yscale('log')
plt.grid()
plt.show()