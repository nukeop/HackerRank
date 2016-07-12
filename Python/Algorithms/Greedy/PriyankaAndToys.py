n = int(raw_input())

w = [int(x) for x in raw_input().split()]

w.sort()

x=w[0]
y=x+4
a = 1

for i in range(n):
    if w[i]>=x and w[i]<=y:
        continue
    else:
        a+=1
        x=w[i]
        y=x+4
 
print a
