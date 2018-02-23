#!/usr/bin/env python
A= raw_input
n=15
b=[]
c=[]
d=[]
e=[]

for x in A[0:]:
	if x< A[0]:
		b.append(x)
	else:
		c.append(x)

print b
print c


for i in b:
	d.append(i**2)
print d

for j in c:
	e.append(j**2)
print e