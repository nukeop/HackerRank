#!/bin/python

import time

t = raw_input().strip()

s = time.strptime(t, "%I:%M:%S%p")

print time.strftime("%H:%M:%S", s)
