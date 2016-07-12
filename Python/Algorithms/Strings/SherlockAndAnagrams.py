def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

n = int(raw_input())

for case in xrange(n):
    s = raw_input()
    
    subs = [s[i:j+1] for i in xrange(len(s)) for j in xrange(i, len(s))]
    subs = sorted(subs, key=lambda x: len(x))
    
    groupedsubs = []
    for i in xrange(1, len(s)):
        group = [x for x in subs if len(x)==i]
        groupedsubs.append(group)
    
    ans = 0
    
    for group in groupedsubs:
        for s1 in range(len(group)):
            for s2 in range(s1, len(group)):
                if s1!=s2 and is_anagram(group[s1], group[s2]):
                    ans+=1
    
    
    print ans
