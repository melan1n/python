#!/bin/python3

import sys


s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]
applescount = 0
orangescount = 0

for i in apple:
    if a + i <= t and a + i >= s:
        applescount += 1
for j in orange:
    if b + j >= s and b + j <= t:
        orangescount += 1
        
print(applescount)
print(orangescount)
