import math
t = int(raw_input())
for i in range(t):
    n, m = (int(x) for x in raw_input().split())
    
    low=0
    high = n
    
    while low+1 < high:
        mid = (low+high)/2
        r = 0.5*(n*n - (n%mid)*math.ceil(n/float(mid))*math.ceil(n/float(mid)) - (mid-(n%mid))*math.floor(n/float(mid))*math.floor(n/float(mid)))
        
        if r < m:
            low = mid
        else:
            high = mid
            
    print high
