#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the quickSort function below.
def quickSort(arr):
    p = 0
    num = arr[p]
    left = []
    equal = []
    right = []
    
    for index, i in enumerate(arr):
        if(i == num):
            equal.append(i)
        elif(i < num):
            left.append(i)
        else:
            right.append(i)
            
    return left + equal + right
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
