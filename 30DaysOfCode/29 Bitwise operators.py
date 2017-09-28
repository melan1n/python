#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
   
    S = []    
    i = 1
    while i <= n:
        S.append(i)
        i += 1
        
    maximum = 0
    x = k-2
    
    if k < 10:
        while x >= 0 and x <= k-2:
            A = S[x]
            y = x + 1
                
            while y <= n-1:
                B = S[y]
                if (A & B) > maximum and (A & B) < k:
                    maximum = A&B
                y += 1    
            x -= 1
    
    else:
        while x >= k-10 and x <= k-2:
            A = S[x]
            y = x + 1
                
            while y <= n-1:
                B = S[y]
                if (A & B) > maximum and (A & B) < k:
                    maximum = A&B
                y += 1    
            x -= 1
            
    print(maximum)
    
