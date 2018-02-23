#!/usr/bin/env python
plateau=[]
for i in range(0,5):
    plateau.append(["O"]*5) #this helps to construct the table of 5*5 full of "O"

def afficher_plateau(plateau):
    for i in plateau:
        print " ".join(i) #this hepls to replace the "" and , by the spaces between the O
print afficher_plateau(plateau)
