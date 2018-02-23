#!/usr/bin/env python
from pylab import *
from ddeint import ddeint
delta= 3*pi/2
model=lambda y,t:y(t-delta)# model
tt=linespace(0,50,10000)# starting time, ending time, number of ponts 
f= cos #expression of Y(t) before the integration interval
yy=ddeint(model,f,tt)     # solve the equation 

#plotting 
plot(tt,yy,c='r',label= "$y(t)$")
plot(tt, cos(tt), c='b',label="$cos(t)$")
set_ylim(ymax=2) #make room for the legend 
legend()