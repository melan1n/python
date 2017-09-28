#!/bin/python3

import sys


n = int(input().strip())
a = []                                                              #create a list of lists
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

primary_diagonal = 0

k = 0
for a_i in a:
    primary_diagonal = primary_diagonal + a_i[k]
    k = k + 1
    
secondary_diagonal = 0

k = -1
for a_i in a:
    secondary_diagonal = secondary_diagonal + a_i[k]
    k = k - 1

result = abs(primary_diagonal - secondary_diagonal)
print(result)
