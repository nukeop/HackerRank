#!/bin/python

t = int(raw_input().strip())
for a0 in xrange(t):
    n,c,m = raw_input().strip().split(' ')
    n,c,m = [int(n),int(c),int(m)]

    wrappers = 0
    a = 0
    
    a = n/c
    wrappers = a
    
    while wrappers>=m:
        a+=wrappers/m
        bought = wrappers/m
        
        wrappers -= m*(wrappers/m)
        wrappers += bought

        
    
    print a
