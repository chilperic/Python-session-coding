'''
1. solve differential equation
2. plot
3. run 100 simulations using random numbers
'''
from sympy import *
import numpy as np


def N0A(t):
	return N0A(t)

def N0(t):
	return N0(t)


def N1A(t):
	return N1A(t)
	
N0_dot = -(l_0+d_0)*N0A(t)

def solve_dif(l_0,d_0):
	Ax = Symbol('x')
        Ay = -(l_0 + d_0)*Ax
	return Ay.diff(Ax)


