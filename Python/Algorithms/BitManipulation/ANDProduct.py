import math
t = int(raw_input())
for i in xrange(t):
    a, b = (int (x) for x in raw_input().split())
    
    if a==0 or b==0 or math.floor(math.log(a, 2)) != math.floor(math.log(b, 2)):
        print 0
        continue
    
    a, b = list(bin(a))[2:], list(bin(b))[2:]
    
    bits = []
    for j in xrange(len(a)):
        if a[j]==b[j]:
            bits.append(a[j])
        else:
            break
    while (len(bits)!=len(a)):
        bits.append('0')
    
    print int("".join(bits), 2)
