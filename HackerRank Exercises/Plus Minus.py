#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
positives_count = 0
negatives_count = 0
zeros_count = 0

for i in arr:
    if i > 0:
        positives_count = positives_count + 1
    elif i < 0:
        negatives_count = negatives_count + 1
    else:
        zeros_count = zeros_count + 1
        
print(float(positives_count/n))
print(float(negatives_count/n))
print(float(zeros_count/n))
