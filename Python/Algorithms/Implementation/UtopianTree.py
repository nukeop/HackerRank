#!/bin/python

def next(current, phase):
    if (phase%2!=0):
        return current*2
    else:
        return current+1

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    
    ans = 1
    for i in range(n):
        ans = next(ans, i+1)
    print ans
