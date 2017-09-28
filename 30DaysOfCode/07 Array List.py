#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

new_arr = list(reversed(arr))
output = ''

for number in new_arr:
    output = output + str(number) + ' '
        
print(output)
