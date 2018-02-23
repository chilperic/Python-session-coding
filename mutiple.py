#!/usr/bin/env python
#This function is using for find the common multiple of two numbers within a certain range


def multiple(x,y,m,t): #x is the lower bound  the range and y higher bound
	from sys import argv
	x, y, m, t= input("Enter the the lower bound of your range: "), input("Enter the the higher bound of your range: "), input("enter the first number: "), input("enter the second number: ")

	x, y, m, t= int(x), int(y), int(m), int(t)
	a=[]
	if x>y:
		print str(x)+ " should be greater or equal to " +str(y)
		exit()

	if y<m and  y<t:
			print "The range is too small. Enter a number bigger than "+ str(m) + "  or " + str(t)
			exit()	
	
	for i in range (x,y):
		
		if (i % m)==0 and (i % t)==0: #m and t are the number that we are looking for their multiple 
			a.append(i)
	print a 		

	return sum(a)
	print multiple(x,y,m,t)
	
		
multiple(0,1000000,5,12)