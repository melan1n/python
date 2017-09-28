#!/bin/python3

import sys


time = input().strip()
mm_ss = time[3:8]
hh = time[0:2]

if time[8:10] == 'PM' and 0 < int(hh) < 12:
    print(str(int(hh)+12) + ':' + mm_ss)

elif time[8:10] == 'PM' and int(hh) == 12:
    print('12' + ':' + mm_ss)

elif time[8:10] == 'AM' and int(hh) == 12:
    print('00' + ':' + mm_ss) 
else:
    print(time[0:8])
    
