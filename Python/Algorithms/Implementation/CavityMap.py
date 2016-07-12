#!/bin/python

import sys

n = int(raw_input().strip())
grid = []
grid_i = 0
for grid_i in xrange(n):
   grid_t = str(raw_input().strip())
   grid.append(grid_t)
    
for row in range(1, len(grid)-1):
    for col in range(1, len(grid[row])-1):
        if(grid[row][col]>grid[row-1][col] and \
           grid[row][col]>grid[row][col+1] and \
           grid[row][col]>grid[row+1][col] and \
           grid[row][col]>grid[row][col-1]):
            newrow = list(grid[row])
            newrow[col] = "X"
            grid[row] = "".join(newrow)
    
for i in grid:
    for x in i:
        #Need stdout.write instead of print to crrectly format text 
        sys.stdout.write(x)
    print ""
