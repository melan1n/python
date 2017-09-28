#!/bin/python3

import sys


n = int(input().strip())
height = [int(height_temp) for height_temp in input().strip().split(' ')]

max_height = max(height)
result = height.count(max_height)
print(result)
