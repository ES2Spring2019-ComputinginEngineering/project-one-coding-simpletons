#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 20:32:06 2019

@author: Ben Pradko & Rónán Gissler
"""
import math as m
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as spicy
from Pendulum import *
from Simulation import *

L1 = .39
L2 = .38
L3 = .37
L4 = .29
L5 = .17
Lengths = [L1, L2, L3, L4, L5]
Files1 = []
Files2 = []
Files3 = []
Files4 = []
Files5 = []
simList = [sim(L1), sim(L2), sim(L3), sim(L4), sim(L5)]
PeriodList = [T(L1, Files1), T(L2, Files2), T(L3, Files3), T(L4, Files4), T(L5, Files5)]

sim(L1)
sim(L2)
sim(L3)
sim(L4)
sim(L5)

T(L1, Files1)
T(L2, Files2)
T(L3, Files3)
T(L4, Files4)
T(L5, Files5)

plt.plot(Lengths, simList, color = 'magenta', label = 'Simulation')
plt.plot(Lengths, PeriodList, color = 'cyan', label = 'Real World')
plt.title('All together!')
plt.xlabel('Length', fontsize = 12)
plt.ylabel('Period', fontsize = 12)
plt.legend(loc = 2, fontsize = 12)
plt.xscale('log')
plt.yscale('log')
plt.grid()
plt.show()