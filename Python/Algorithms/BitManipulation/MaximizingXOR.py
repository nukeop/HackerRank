import itertools

def  maxXor( l,  r):
    largest = 0
    c = itertools.combinations(range(l, r+1), 2)
    for x in c:
        if x[0]^x[1] > largest:
            largest = x[0]^x[1]
    return largest

    

_l = int(raw_input());


_r = int(raw_input());

res = maxXor(_l, _r);
print(res)
