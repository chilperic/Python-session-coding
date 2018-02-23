#!/usr/bin/env python
import numpy as np
import random as ran
a=[]
def liste(x): # this function just put the numbers from 1 to 10000 into a list called x
	for i in range (1,10001):	
		x.append(i)
	return x
#print liste(a)

def lire(y): # this function read a list of 10000 mumbers in the reverse order
	c=[]
	for j in range(len(y)):
		c.append(y[-(j+1)])
	return c
 
t=lire(liste(g))
print t
'''#print lire(liste(a))
def ran_number(): # this function define a list 10000 random numbers (integer)
	d=[]
	for i in range(10000):
		d.append(int(ran.uniform(0,10000)))
	
	return d
 


def tri(x):
	x=sorted(x)
	return x


print tri(ran_number())
'''