#!/usr/bin/env python
#This program use the rectangle method to compute the integral of the function f
from numpy import sin
def rect(a,b,f,n):
	h=(b-a)/float(n)
	z=0

	for i in range(n):
		xi=a+i*h
		z=z+f()
	return h*z

#example of function 	

def f(x):
	return sin(x**2+x)+x**4+4

print rect(-1,2,f,100)