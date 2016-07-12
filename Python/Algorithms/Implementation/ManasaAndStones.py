T = int(raw_input())

for loop in range(T):
    n = int(raw_input())
    a = int(raw_input())
    b = int(raw_input())
 
    limit1 = a*n
    limit2 = b*n
    if limit1==limit2:
        print limit1-a
        continue
    
    if limit1 > limit2:
        limit1, limit2 = limit2, limit1

    ans = range(limit1, limit2, abs(a-b))
    
    for p in ans:
        print p-limit1/n,
    print
