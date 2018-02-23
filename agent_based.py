#!/usr/bin/env python

import numpy as np
import random as ran
import csv
from scipy.stats import gamma
import matplotlib.pyplot as plt

#Initialisation of parameter values
N0 = 1000000
p1 = 0.35
p3 = 0.30
mu_a = 16
mu_po = 24
mu_p = 8
mu_d = 60
mu_d0 = 44
nu_a = 32
nu_p0 = 48
nu_d0 = 88
nu_p =  8
nu_d = 60
# number of generations
w = 10
# cells initialization
pa = np.random.uniform(0,1)
pad = np.random.uniform(0,1)
allcells = [[0 for i in range(w)]]
allcells[0][0] = N0*pa*(1-pad)

# calculated waiting times vector
time_points = [0]

# total running time
t_final = 120

# event probabilities at current time (probabity that a cell will die or divide)
def eprobs():
	pdie = np.random.uniform(0,1)
	pdiv = np.random.uniform(0,1)
	return [pdie,pdiv]


# events generations (cells which can divide or die)
def egenerations():
	events = []
	for i in allcells[-1]:
		if i!= 0:
			events.append([allcells[-1].index(i), i])
		else:
			pass
	return events


# waiting time for next event
def waiting_times():
	wt = list(np.random.gamma(10, scale=1.0, size = len(egenerations())))
	new = egenerations()
	for x in range(len(wt)):
		new[x].append(wt[x])
	new.sort(key = lambda x: x[2])
	return new[0]




# update age structure

def upas():
	if eprobs()[0] > eprobs()[1]:
		allcells[-1][waiting_times()[0]] -= 1
	else:
		allcells[-1][waiting_times()[0]] -= 1
		allcells[-1][waiting_times()[0] + 1] += 2
	return allcells[-1]





while sum(time_points) < t_final:
	time_points.append(waiting_times()[2])
	allcells.append(upas())
	
print allcells



myfile = open('allcells.csv', 'wb')
wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
wr.writerow(allcells)

