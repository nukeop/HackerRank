s1 = list(raw_input())
s2 = list(raw_input())

s1c = s1[:]
s2c = s2[:]

for x in range(len(s1)):
    try:
        s2c.remove(s1[x])
    except ValueError:
        pass
    
for x in range(len(s2)):
    try:
        s1c.remove(s2[x])
    except ValueError:
        pass
    
print len(s1c)+len(s2c)
