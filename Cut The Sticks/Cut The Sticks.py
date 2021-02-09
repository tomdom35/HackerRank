#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    return recursiveCount(arr,[])
    
def recursiveCount(arr,count):
    l = len(arr)
    if l == 0:
        return count
    count.append(l)
    m = min(arr)
    arr = [i for i in arr if i != m]
    return recursiveCount(arr,count)
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
