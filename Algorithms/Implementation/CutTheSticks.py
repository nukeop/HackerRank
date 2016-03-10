#!/bin/python

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

s = sorted(arr)

while(len(s)>0):
    print len(s)
    s = sorted(s)
    s = [x-s[0] for x in s if x-s[0]>0]
