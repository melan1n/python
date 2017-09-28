#!/bin/python3

import sys


n = int(input().strip())

# convert it to binary
binary = ''
while n > 0:
    remainder = n%2
    binary = str(remainder) + binary
    n = n//2

#find and print the base- integer denoting the maximum number of consecutive 1's in n's binary representation.
max_count_1 = 0
current_count_1 = 0
i = 0
while i < len(binary):
    if binary[i] == '1':
        current_count_1 = current_count_1 + 1
        if current_count_1 > max_count_1:
            max_count_1 = current_count_1
    else:
        if current_count_1 > max_count_1:
            max_count_1 = current_count_1
            current_count_1 = 0
        else:
            current_count_1 = 0
        
    i = i + 1
    
print(max_count_1)
        
