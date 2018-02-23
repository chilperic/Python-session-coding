#!/usr/bin/env python

'''
1. Generate random Number
2. Between 0 and 1
3. print the gen numbers
'''
import numpy, random, csv

#Function to generate numbers between ......
def gen_numbers(n):
	rand_numbers = []
        for i in range(n):
                random.seed()
		rand_numbers.append(random.uniform(0,1))
	return rand_numbers


#function call, argument is the number of values you want.
get_list = gen_numbers(10)

#save numbers into a csv file
myfile = open('output_rand_number.csv', 'wb')
wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
wr.writerow(get_list)





"""
time = 0
allcells = [[0for x in range(w)]]
allcells[0][0]=N0
for i in range(50):
	Par=ran.uniform(0,1)
	Padr= ran.uniform(0,1)
	allcells.append(allcells[-1])
	time_points = list(np.random.gamma(10, scale=1.0, size=w))
	event =	time_points.index(min(time_points))
	if allcells[-1][event] == 0:
		allcells.remove(allcells[-1])
		pass
	else:
		if event == w-1:
			allcells[-1][-1] = allcells[-1][-1] - 1
		else:
			allcells[-1][event] = allcells[-1][event] - allcells[-1][event]*Par*(1-Padr)
			allcells[-1][event + 1] = allcells[-1][event + 1] + 2*allcells[-1][event]*Par*(1-Padr)
		time = time + min(time_points)
	print allcells[-1]


print allcells

def activated_divided(N,Par,Padr):
	return N*Par*(1-Padr)

def remaining(N,Par,Padr):
	return N*Par -N*Par*(1-Padr)

#fill the matrix allcells



def time_point_events(allcells):
	time = 0
	for i in t_pts:
		while time <= i:
			allcells.append([0 for i in range(w)])
			current_time = allcells[-1]
			current_time[0] = remaining(allcells[-2][0],Par,Padr)
			for x in range(1,w):
				current_time[x] = (2*activated_divided(allcells[-2][x-1],Par,Padr) + remaining(allcells[-2][x],Par,Padr))
			time = time + np.random.gamma(10, scale=1.0, size=None)
		print current_time



time_point_events(allcells)
#print allcells






time = 0
for i in t_pts:
	allcells.append([])
	
	current_time[0] = N0 - N0*Par
	for x in range(1,w):
		current_time[x] = 
	for j in gen:
		current_time.append(N0*Par*(1-Padr))
		time = time + 1


#	for j in gen:
#		if i == 0 and j== 0:
#			allcells[-1].append(N0)







#			allcells[[i][j]]=N0
#		elif i==0 and j != 0:
#			allcells[[i][j]]=0
#		else:
#			allcells[[i][j]]=N0*Par*(1-Padr)

print allcells
"""