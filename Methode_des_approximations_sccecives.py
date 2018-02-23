#!/usr/bin/env python
# this program help to determine the zero of a function in a certain interval
import scipy.optimize as sc #this module this module contain the brentq fonction which determine the root of a function

def fonction(x):
	return x**3+x**2-x+3
x0=-5
a=-5
b=10
print sc.brentq(fonction,a,b) 
print sc.bisect(fonction,a,b) 
print sc.newton(fonction,x0) 