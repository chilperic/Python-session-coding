import random 
import time 
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style

style.use("ggplot")

broke_count = 0

def Labouchere():
	global broke_count
	starting_funds = 100
	goal = 10
	system = [1,1,1,1,1,1,1,1,1,1]
	#system = [1,2,2,3,2]

	profit = 0
	current_funds = starting_funds
	wagerSizes =[]
	plot_funds = []
	not_broke = True

	wins = 1
	losses = 1

	while profit < goal and not_broke:
		if len(system) > 1:
			size = system[0 ]+system[-1]
			wagerSizes.append(size)
			plot_funds.append(current_funds)
		else:
			size =system[0]
			wagerSizes.append(size)
			plot_funds.append(current_funds)

			if current_funds <= 0:
				not_broke = False
				broke_count += 1
			elif current_funds - size <= 0:
				size = current_funds
				not_broke = False
				broke_count += 1

			dice = random.randrange(1,101)

			if dice < 51:
				losses += 1

