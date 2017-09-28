#!/bin/python3

import sys


n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]

class Sorting:
    def __init__(self, a, n):
        self.a = a
        self.n = n
        self.numSwaps = 0
        
    def bubbleSort(self):
        i = 0
        while i < n:
            numberOfSwaps = 0
            # Track number of elements swapped during a single array traversal
            j = i
            for j in range(n-1):# Swap adjacent elements if they are in decreasing order
                if (a[j] > a[j + 1]):
                    tmp = a[j]
                    a[j] = a[j + 1]
                    a[j + 1] = tmp
                    numberOfSwaps += 1
                    j += 1
            self.numSwaps = self.numSwaps + numberOfSwaps
            i += 1
        # If no elements were swapped during a traversal, array is sorted
        #if (numberOfSwaps == 0):
           # break
"""            
Output:
Array is sorted in numSwap swaps.
First element: firstElement
Last element: lastElement
    }
To complete this challenge, you will need to add a variable that keeps a running tally of all swaps that occur during execution. """

new_sorting = Sorting(a, n)
new_sorting.bubbleSort()

print('Array is sorted in ' + str(new_sorting.numSwaps) + ' swaps.')
print('First Element: ' + str(new_sorting.a[0]))
print('Last Element: ' + str(new_sorting.a[n-1]))
