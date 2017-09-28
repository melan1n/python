#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
height = list(map(int, input().strip().split(' ')))
# your code goes here
drinks_needed = 0
if (max(height) - k) <= 0:
    drinks_needed = 0
else:
    drinks_needed = max(height) - k
print(drinks_needed)
