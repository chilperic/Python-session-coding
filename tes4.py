#!/usr/bin/env python
# -*-coding:utf-8 -*
''' Ce programme teste si une annee est bissestile ou non

Une annee est dite bissextile si c'est un multiple de 4, sauf si c'est un multiple de 100. 
Toutefois, elle est consideree comme bissextile si c'est un multiple de 400. Je developpe :

Si une annee n'est pas multiple de 4, on s'arrete la, elle n'est pas bissextile.
Si elle est multiple de 4, on regarde si elle est multiple de 100.
Si c'est le cas, on regarde si elle est multiple de 400.
Si c'est le cas, l'annee est bissextile.
Sinon, elle n'est pas bissextile.
Sinon, elle est bissextile.






	
#Ceci est une autre facon de faire 

# Programme testant si une année, saisie par l'utilisateur, est bissextile ou non

annee = raw_input("Saisissez une année : ") # On attend que l'utilisateur saisisse l'année qu'il désire tester
a= "la valeur Entree doit etre un entier"
b= "La valeur entree n'est pas declaree"
try:
	annee = int(annee)
except ValueError:
	print "voici l'erreur: ", "la valeur Entree doit etre un entier ",e
	

if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
    print("L'année saisie est bissextile.")
else:
    print("L'année saisie n'est pas bissextile.")


'''

def div_euclid():
	a=raw_input("Entrer le numerateur: ")
	b=raw_input("Entrer le denominateur: ")
	try:
		numerateur =int(a)
		denominateur =int(b)
		resultat = numerateur-numerateur / denominateur
	except NameError:
	    print "La variable numerateur ou denominateur n'a pas été définie."
	    print "La variable numerateur ou denominateur possède un type incompatible avec la division."
	except ZeroDivisionError:
	    print "La variable denominateur est égale à 0."
	except ValueError:
	    print "La variable numerateur ou denominateur n'a pas un entier."
	else:
	    print "Le résultat obtenu est", resultat


div_euclid()