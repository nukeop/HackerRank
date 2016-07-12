import string
n = int(raw_input())
s = []

for i in range(n):
    s.append(raw_input())
    
d = {}
for l in string.ascii_lowercase:
    d[l] = 0
    
for ss in s:
    for letter in string.ascii_lowercase:
        if letter in ss:
            d[letter]+=1
        
sum = 0
for (key, value) in d.iteritems():
    if value == len(s):
        sum+=1
print sum
