#!/usr/bin/env python

nombre = input("Entree le nombre donc vous voulez sa table de multiplication: ")
valmax= input ("Entree la valeur maximale pour la multiplication: ")
nombre = int (nombre)
valmax =int(valmax)
def TAB(x):
	i=0
	while i <=valmax:
		print i, "*", x, "=", i*x
		i +=1
TAB(nombre)