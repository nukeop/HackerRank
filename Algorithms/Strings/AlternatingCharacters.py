n = int(raw_input())

for i in range(n):
    s = raw_input()
    
    count = 0
    for j in range(1, len(s)-1):
        if s[j]==s[j-1]:
            count +=1
    
    if s[len(s)-1] == s[len(s)-2]:
        count+=1
            
    print count
