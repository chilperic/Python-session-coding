
#!/usr/bin/env python

#This program is use to plot the plane function
import numpy as np
import pylab as pl 
import scipy as sc

def patrice(x):
	return -x+4+x*sc.exp(-x)+sc.cos(x+5)
def droite(x):
	return -x+4*x
def marc(x):
	return -x**2+4*sc.sin(x+5)
x = pl.linspace(-20, 20, 500)
y = patrice(x)
z = droite(x)
t= marc(x)
pl.xlim(-30,30)
pl.ylim(-30,30)



pl.xlabel("x")
pl.ylabel("y")


#plt.plot(z)
pl.plot(x, y,"g-",label="y=-x+4+xexp(-x)", linewidth=2)
pl.plot(x,z,"b-",label="y=-x+4", linewidth=1)
pl.plot(x, t,"r-",label="-x^3+4x^cos(x^2+5x)", linewidth=.5)
pl.legend()
pl.title("y=-x+4+xexp(-x),  y=-x+4, -x^3+4x^cos(x^2+5x)")
pl.show()

#print patrice(0)


