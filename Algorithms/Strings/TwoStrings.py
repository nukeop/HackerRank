import string

n = int(raw_input())
for i in xrange(n):
    A = raw_input()
    B = raw_input()

    for c in string.ascii_lowercase:
        if c in A and c in B:
            print "YES"
            break
    else:
        print "NO"
