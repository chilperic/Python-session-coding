#!/usr/bin/env python


#Chapter 3 Exercise 16b
#A Fibonacci sequence is a  sequence of numbers where each successive number is the sum of the previous two.
#The classic Fibonacci sequence begins 1, 1, 2, 3, 5, 8, 13,....
#Write a program that computes the nth Fibonacci number where the n is a value input by the user
 
print("This program that computes the nth Fibonacci number where the n is a value input by the user")
num = eval(input(100))
def fib(n, a = 0, b = 1):
    seq = [a,b]
    while len(seq) < n:
        seq += [seq[len(seq)-1] + seq[len(seq)-2]]
    return seq
 
b = sum(fib(num + 1))
print(b)