#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
r = 0
for i in range(n):
    r+=arr[i]

print r
