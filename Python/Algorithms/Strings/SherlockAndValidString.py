def is_valid(s):
    c = -1
    for l in set(s):
        if c==-1:
            c = s.count(l)
        else:
            if c!=s.count(l):
                return False
    return True
    
s = raw_input()

for letter in set(s):
    if is_valid(s.replace(letter, "")):
        print "YES"
        sys.exit()

print "NO"
