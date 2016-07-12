#!/bin/python

n = int(raw_input().strip())
a = []
for a_i in xrange(n):
   a_temp = map(int,raw_input().strip().split(' '))
   a.append(a_temp)

d1 = 0
d2 = 0
    
for row in range(n):
    for v in range(n):
        if v==row:
            d1 += a[row][v]
            
        if v+row==n-1:
            d2 += a[row][v]

print abs(d1-d2)
