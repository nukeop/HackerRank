#!/bin/python

import string

n = int(raw_input().strip())
s = raw_input().strip()
k = int(raw_input().strip())

newstring = ""

for letter in s:
    if letter in string.ascii_lowercase:
        newstring += chr(((ord(letter)-ord('a')+k)%len(string.ascii_lowercase))+ord('a'))
    elif letter in string.ascii_uppercase:
        newstring += chr(((ord(letter)-ord('A')+k)%len(string.ascii_uppercase))+ord('A'))
    else:
        newstring += letter

print newstring
