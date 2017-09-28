#!/bin/python3

import sys


a0,a1,a2 = input().strip().split(' ')
A = a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = input().strip().split(' ')
B = b0,b1,b2 = [int(b0),int(b1),int(b2)]

Ar = 0
Br = 0

for i in range(3):
    if A[i] > B[i]:
        Ar = Ar + 1
    elif A[i] < B[i]:
        Br = Br + 1

print(str(Ar)+' '+str(Br))
