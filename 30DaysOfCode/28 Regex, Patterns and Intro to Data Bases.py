#!/bin/python3

import sys
import re

N = int(input().strip())
result = []
for a0 in range(N):
    firstName,emailID = input().strip().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]
    if re.findall(r'\@gmail\.com$', emailID) != []:
        result.append(firstName)

for r in sorted(result):
    print(r)
