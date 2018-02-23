#!/usr/bin/env python
def diviseur(x):
	a=[]
	for i in range (1,x+1):
		if x%i==0:
			a.append(i)
			i=i+1

	
	print a

diviseur(98824)

def Multiple(x,n):
	a=[]
	if x<=n:
		for i in range(n+1):
			if i%x==0:
				a.append(i)
	else:
		print "Error check your entries "
	print a

Multiple (1,5)