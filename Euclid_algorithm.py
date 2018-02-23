#!/usr/bin/env python
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
GCD=gcd(a,b)
print "GCD is: "
print GCD
'''
f=lambda x: x*x
print f(5)
'''