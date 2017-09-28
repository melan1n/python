#!/bin/python3

import sys


n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
b = [int(b_temp) for b_temp in input().strip().split(' ')]
result = []
min_result = sorted(a)[-1]
max_result = sorted(b)[0]

i = min_result

while i <= max_result:
    result.append(i)
    x = 0
    while x <= (len(a)-1):
        if i % a[x] != 0:
            result.pop()
            
        else:
            y = 0
            while y <= (len(b)-1):
                if b[y] % i != 0:
                    result.pop()
                    break
                else:
                    y += 1
        x += 1
    
    i +=  min_result
    
print(result)

