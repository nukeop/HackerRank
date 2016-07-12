#!/bin/python

t = int(raw_input().strip())
for a0 in xrange(t):
    b,w = raw_input().strip().split(' ')
    b,w = [int(b),int(w)]
    x,y,z = raw_input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    
    lowestbprice = x if x < y+z else y+z
    lowestwprice = y if y < x+z else x+z
    
    print b*lowestbprice + w*lowestwprice
