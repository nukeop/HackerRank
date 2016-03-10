#!/bin/python

d1,m1,y1 = raw_input().strip().split(' ')
d1,m1,y1 = [int(d1),int(m1),int(y1)]
d2,m2,y2 = raw_input().strip().split(' ')
d2,m2,y2 = [int(d2),int(m2),int(y2)]

if d1>d2 and m1==m2 and y2==y1:
    print 15*abs(d2-d1)
elif m1>m2 and y2==y1:
    print 500*abs(m2-m1)
elif y1>y2:
    print 10000
else:
    print 0
