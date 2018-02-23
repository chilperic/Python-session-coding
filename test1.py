#!/usr/bin/env python

import numpy as np

import random as ran
import csv
from scipy.stats import gamma
import matplotlib.pyplot as plt


#time points 
t_pts =np.arange(0,121,12)

gen= np.arange(0,100,1)

#define a radom number between [0,1]

par=ran.uniform(0,1)
padr= ran.uniform(0,1)

# Initialisation of a container which will contain contain the number of cells in different division classes at different time point.

h=100

allcells =  [[0 for x in t_pts] for y in range(h)] 

#fill the matrix allcells


print t_pts

print allcells