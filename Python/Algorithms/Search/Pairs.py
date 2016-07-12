import itertools
n, k = (int(x) for x in raw_input().split())

ar = [int(x) for x in raw_input().split()]

d = {}

count = 0
for x in ar:
    d[x] = 1
    
for x in ar:
    try:
        if d[x+k] == 1:
            count+=1
    except KeyError:
        pass
        
print count
