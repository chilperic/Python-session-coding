#!/usr/bin/env python

####################################################################
###    This is the PYTHON version of program 6.1 from page 194 of  #
### "Modeling Infectious Disease in humans and animals"            #
### by Keeling & Rohani.					   #
###								   #
### % It is the SIR epidemic model with constant additive noise    #
### added to the transmission rate.				   #
### Given the difficulties in integrating the dynamics, the user   #
### is prompted for a integration time-step.			   #
####################################################################

##########################################################################
### Copyright (C) <2008> Ilias Soumpasis                                 #
### ilias.soumpasis@deductivethinking.com                                #
### ilias.soumpasis@gmail.com	                                         #
###                                                                      #
### This program is free software: you can redistribute it and/or modify #
### it under the terms of the GNU General Public License as published by #
### the Free Software Foundation, version 3.                             #
###                                                                      #
### This program is distributed in the hope that it will be useful,      #
### but WITHOUT ANY WARRANTY; without even the implied warranty of       #
### MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the        #
### GNU General Public License for more details.                         #
###                                                                      #
### You should find a copy of the GNU General Public License at          #
###the Copyrights section or, see http://www.gnu.org/licenses.           #
##########################################################################


import scipy.integrate as spi
import numpy as np
import pylab as pl


beta=1.0;
noise=10;
gamma=1/10.0;
mu=1/(50*365.0);
X0=1e5;
Y0=500;
N0=1e6;
Step=1.0;
ND=MaxTime=5*365.0;
TS=1.0

INPUT0=np.hstack((X0,Y0))

def diff_eqs(INP,t):  
	'''The main set of equations'''
	Y=np.zeros((2))
	V = INP     
	Y[0] = mu * N0 - beta*V[0]*V[1]/N0 - Noise - mu*V[1]
	Y[1] = beta*V[0]*V[1]/N0 + Noise -  mu*V[1] - gamma*V[1]
	return Y   # For odeint

T=np.zeros((np.ceil(ND/Step),1))
RES=np.zeros((np.ceil(ND/Step),2))
INPUT=INPUT0
t=0
loop=0

while t<ND and INPUT[0]>0 and INPUT[1]>0:
	t_start = 0.0; t_end = t_start+Step; t_inc = TS
	t_range = np.arange(t_start, t_end+t_inc, t_inc)
	sqrtStep=np.sqrt(Step)
	Noise=noise* np.random.normal(size=1)/sqrtStep
	PRES = spi.odeint(diff_eqs,INPUT,t_range)
	T[loop]=t=t+Step
	INPUT=PRES[-1]
	RES[loop]=PRES[-1]
	loop += 1

print(RES)

### plotting
pl.subplot(211)
pl.plot(T/365., RES[:,0], '.-g')
pl.xlabel('Time (Years)')
pl.ylabel('Susceptibles')
pl.subplot(212)
pl.plot(T/365., RES[:,1], '.-r')
pl.ylabel('Infected')
pl.xlabel('Time (Years)')

pl.show()