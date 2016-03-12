n = int(raw_input())
for i in range(n):
    n, k = (int(x) for x in raw_input().split())
    a = [int(x) for x in raw_input().split()]
    b = [int(x) for x in raw_input().split()]
    
    a = [k-x for x in a]
    a.sort()
    b.sort()
    toprint = "YES"
    
    for j in range(n):
        if a[j]>b[j]:
            toprint = "NO"
            break
    print toprint
