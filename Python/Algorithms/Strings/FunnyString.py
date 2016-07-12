n = int(raw_input().strip())

for i in range(n):
    s = [ord(x) for x in list(raw_input())]
    rs = list(reversed(s))
    funny = True
    
    for j in range(1, len(s)):
        if (abs(s[j]-s[j-1]) != abs(rs[j]-rs[j-1])):
            funny = False
            break
    
    print "Funny" if funny else "Not Funny"
