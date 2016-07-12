#!/bin/python

import sys

n = int(raw_input().strip())

for i in range(n):
    if(i<n):
        #Need stdout.write instead of print to correctly format the symbols
        sys.stdout.write(" "*(n-i-1))
        sys.stdout.write("#"*(i+1) + "\n")
