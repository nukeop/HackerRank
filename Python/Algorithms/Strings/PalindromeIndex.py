def is_palindrome(s):
    return list(s) == [x for x in reversed(s)]


n = int(raw_input())

for i in range(n):
    s = raw_input()
    
    if is_palindrome(s):
        print -1
        continue
    
    for i in range(len(s)/2):
        if(s[i] == s[len(s)-i-1]):
            continue
        else:
            if is_palindrome(s[i:len(s)-i-1]):
                print len(s)-i-1
            else:
                print i
                
        break
