#!/bin/python3

import sys

def solve(grades):
    # Complete this function
    answer = []
    for grade in grades:
        if grade < 38:
            answer.append(grade)
        elif 2 < grade%5:
            answer.append(5*(grade//5) + 5)
        elif 2 >= grade%5:
            answer.append(grade)
    return answer

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
r = 0
for r in range(len(result)):
    print(result[r])
