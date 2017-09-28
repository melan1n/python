#!/bin/python

import sys


a,b,c,d,e = input().strip().split(' ')
arr = a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]

sum_1 = arr[0] + arr[1] + arr[2] + arr[3]
sum_2 = arr[0] + arr[1] + arr[2] + arr[4]
sum_3 = arr[0] + arr[1] + arr[3] + arr[4]
sum_4 = arr[0] + arr[2] + arr[3] + arr[4]
sum_5 = arr[1] + arr[2] + arr[3] + arr[4]

max_sum = max(sum_1, sum_2, sum_3, sum_4, sum_5)
min_sum = min(sum_1, sum_2, sum_3, sum_4, sum_5)

print(str(min_sum) + ' ' + str(max_sum))
