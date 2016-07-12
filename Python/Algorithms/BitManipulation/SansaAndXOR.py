t = int(raw_input())
for i in range(t):
    n = int(raw_input())
    arr = [int(x) for x in raw_input().split()]
    
    if len(arr)%2==0:
        print 0
    else:  
        print reduce(lambda i, j: i^j, arr[0::2])
