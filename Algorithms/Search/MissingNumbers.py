n = int(raw_input())
a = [int(x) for x in raw_input().split()]
m = int(raw_input())
b = [int(x) for x in raw_input().split()]

d = [0]*10001
for i in range(len(a)):
    d[a[i]]-=1
    
for i in range(len(b)):
    d[b[i]]+=1
    
missing = []
for i in range(len(d)):
    if d[i] > 0:
        missing.append(i)


for i in sorted(missing):
    print i,
