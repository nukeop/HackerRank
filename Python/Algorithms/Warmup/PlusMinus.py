#!/bin/python

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

print format(len([x for x in arr if x>0])/float(n), ".6f")
print format(len([x for x in arr if x<0])/float(n), ".6f")
print format(len([x for x in arr if x==0])/float(n), ".6f")
