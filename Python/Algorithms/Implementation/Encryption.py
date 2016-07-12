#!/bin/python

import math

s = raw_input().strip()

l = int(math.ceil(math.sqrt(len(s))))
r = int(math.floor(math.sqrt(len(s))))

if r*l<len(s):
    r=l

sl = list(s)
encrypted = []

while len(sl)>0:
    if len(sl) >= l:
        encrypted.append("".join(sl[:l]))
        sl = sl[l:]
    else:
        encrypted.append("".join(sl))
        break
    
ans = ""

for i in range(l):
    for e in encrypted:
        if i < len(e):
            ans += e[i]
    ans += " "

print ans
