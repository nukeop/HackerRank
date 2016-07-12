t = int(raw_input())

for i in range(t):
    m = int(raw_input())
    n = int(raw_input())
    c = [int(x) for x in raw_input().split()]
    
    for flavor in c:
        d = list(c)
        d[c.index(flavor)] = -1
        if m > flavor and m-flavor in d:
            print c.index(flavor)+1, d.index(m-flavor)+1
            break
