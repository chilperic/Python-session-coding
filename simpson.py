#!/usr/bin/env python
#This program uses the Simpson method to compute the integral of the function f
import numpy as np
def simp(a,b,f,n):
	h=(b-a)/float(n)
	z=0

	for i in range(n):
		
		z=z+(f(a+i*h)+f(a+(i+1)*h)+4*f((a+i*h+a+(i+1)*h)/2))/6
	return h*z

#example of function 	

def f(x):
	return np.sin(x**2+x)+x**4+4+np.cos(x**2)

print simp(-1,2,f,100)