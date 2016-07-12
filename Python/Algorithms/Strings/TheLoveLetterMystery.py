n = int(raw_input())

for i in range(n):
    s = raw_input()
    
    ops = 0
    for i in range(len(s)/2):
        if s[i]!=s[len(s)-i-1]:
            ops += abs(ord(s[i]) - ord(s[len(s)-i-1]))
    print ops
