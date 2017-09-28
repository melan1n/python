#!/bin/python3

import sys

#arr is a list of lists (6*6) or a 2d array
arr = []                               
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

#fix starting coordinates for each 3*3 square
i = 0     
j = 0

hourglass_sums = []
for i in range(4):
    for j in range(4):
        hourglass = []
        for x in range(3):
            for y in range(3):
                hourglass.append(arr[i+x][j+y])
        del hourglass[3]   #remove first list element to get the hourglass
        del hourglass[4]   #remove first list element to get the hourglass
        hourglass_sums.append(sum(hourglass))

print(max(hourglass_sums))

