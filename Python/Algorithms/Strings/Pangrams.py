import string
s = raw_input().strip().lower()
print "pangram" if len([x for x in list(string.ascii_lowercase) if x not in list(s)])==0 else "not pangram"
