#!/bin/python3

import sys


n = int(input().strip())
k = 1

while n > 0:
    next_line = ' '*(n-1)+ '#'*k
    print(next_line)
    n = n - 1
    k = k + 1
