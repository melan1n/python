#!/bin/python3

import sys


h = list(map(int, input().strip().split(' ')))
word = input().strip()

alpha = 'abcdefghijklmnopqrstuvwxyz'
lookup = {}
for i in range(len(alpha)):
    lookup [alpha[i]] = h[i]

height_list = []
for char in word:
    height_list.append(lookup[char])

result = max(height_list)*len(word)
print(result)
