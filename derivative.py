#!/usr/bin/env python
'''import sympy as sp
import numpy as np 
from scipy.misc import derivative 
import matplotlib.pyplot as plt
x=sp.Symbol('x')
print sp.diff(3*x**2+1)
from scipy.misc import derivative 
def f(x):
	return 3*x**2+1
print derivative(f,x)

def der(x):
	return derivative(f,x)

y=np.linspace(-3,3) 
plt.plot(y,f(y))
plt.plot(y,der(y))
plt.show()
'''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
line, = ax.plot(np.random.rand(10))
ax.set_ylim(0, 1)

def update(data):
    line.set_ydata(data)
    return line,


def data_gen():
    while True:
        yield np.random.rand(10)

ani = animation.FuncAnimation(fig, update, data_gen, interval=100)
plt.show()