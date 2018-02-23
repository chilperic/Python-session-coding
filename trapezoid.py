#!/usr/bin/env python
#This program use the  trapezoid method to compute the integral of the function f
from numpy import sin
def trap(a,b,f,n):
	h=(b-a)/float(n) 
	z=0

	for i in range(n):
	
		z=z+(f(a+i*h)+f(a+(i+1)*h))/2
		
	return h*z

#example of function 	

def f(x):
	return sin(x**2+x)+x**4+4

print trap(-1,2,f,100)