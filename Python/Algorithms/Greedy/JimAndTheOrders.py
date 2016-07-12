n = int(raw_input())

#[0] - number of fan, [1] - ending time
l = []

for i in range(n):
    t, d = (int(x) for x in raw_input().split())
    l.append((t+d, i))
    
l.sort()
for t in l:
    print t[1]+1,
