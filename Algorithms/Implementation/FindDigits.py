#!/bin/python

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())

    print len([x for x in list(str(n)) if int(x)!=0 and n%int(x)==0])
