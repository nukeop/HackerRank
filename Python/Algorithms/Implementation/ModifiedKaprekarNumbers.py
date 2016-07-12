p = int(raw_input())
q = int(raw_input())

numbers = 0
for i in range(p, q+1):
    sq = i*i
    d = len(str(i))
    r = str(sq)[len(str(sq))-d:]
    l = str(sq)[:len(str(sq))-d]
    
    s = 0
    if r!= "":
        s+=int(r)
    if l!= "":
        s+=int(l)
    if s==i:
        print i,
        numbers += 1

if numbers==0:
    print "INVALID RANGE"
