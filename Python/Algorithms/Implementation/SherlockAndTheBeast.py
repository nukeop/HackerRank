#!/bin/python

def getpivot(n):
    while(n>0):
        if(n%3==0):
            break
        else:
            n-=5
    return n

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    
    pivot = getpivot(n)
    
    
    
    if(pivot<0):
        print -1
    else:
        s = ""
        repeat = pivot/3
        while(repeat>0):
            repeat-=1
            s+="555"
            
        repeat = (n-pivot)/5
        while(repeat>0):
            repeat-=1
            s+="33333"
        print s
