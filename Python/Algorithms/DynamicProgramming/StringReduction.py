n = int(raw_input())
for i in range(n):
    s = raw_input()

    ac = s.count("a")
    bc = s.count("b")
    cc = s.count("c")
    
    if ((ac==0 and bc==0) or (ac==0 and cc==0) or (bc==0 and cc==0)):
        print len(s)
    elif (ac%2==0 and bc%2==0 and cc%2==0):
        print 2
    elif (ac%2==1 and bc%2==1 and cc%2==1):
        print 2
    else:
        print 1
