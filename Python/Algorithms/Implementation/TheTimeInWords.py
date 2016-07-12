#!/bin/python

hours = {\
    1:"one",\
    2:"two",\
    3:"three",\
    4:"four",\
    5:"five",\
    6:"six",\
    7:"seven",\
    8:"eight",\
    9:"nine",\
    10:"ten",\
    11:"eleven",\
    12:"twelve,"\
}

minutes = {\
    1:"one",\
    2:"two",\
    3:"three",\
    4:"four",\
    5:"five",\
    6:"six",\
    7:"seven",\
    8:"eight",\
    9:"nine",\
    10:"ten",\
    11:"eleven",\
    12:"twelve",\
    13:"thirteen",\
    14:"fourteen",\
    15:"quarter",\
    16:"sixteen",\
    17:"seventeen",\
    18:"eighteen",\
    19:"nineteen",\
    20:"twenty",\
    30:"half",\
}

h = int(raw_input().strip())
m = int(raw_input().strip())

if m==0:
    print hours[h], "o' clock"
    exit()
    
if m>0 and m<31:
    if m<=20:
        if m!=15:
            print minutes[m], "minute" if m==1 else "minutes", "past", hours[h]
        else:
            print minutes[m], "past", hours[h]
    elif m<30:
        print minutes[20], minutes[m-20], "minutes", "past", hours[h]
    else:
        print minutes[m], "past", hours[h]
else:
    if 60-m<=20:
        if 60-m!=15:
            print minutes[60-m], "minute" if m==1 else "minutes", "to", hours[h+1] if h<12 else hours[1]
        else:
            print minutes[60-m], "to", hours[h+1] if h<12 else hours[1]
    else:
        print minutes[20], minutes[60-m-20], "minutes", "to", hours[h+1] if h<12 else hours[1]
