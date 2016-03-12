s = raw_input()
 
found = True
# Write the code to find the required palindrome and then assign the variable 'found' a value of True or False

import string
odd = False
for i in string.ascii_lowercase:
    if not (s.count(i)%2==0):
        if not odd:
            if len(s)%2==1:
                odd = True
            else:
                found = False
                break
        else:
            found = False
            break

print "YES" if found else "NO"
