#!/bin/python3

import sys


n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]

c.sort()
pairs = 0
i = 0
for color in c:
    while i < n:
        if c.count(c[i]) > 1:
            pairs = pairs + c.count(c[i])//2
            i = i + c.count(c[i])
        else:
            pairs = pairs
            i = i + 1

print(pairs)
