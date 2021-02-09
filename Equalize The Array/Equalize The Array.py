#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    counts = [0]*101
    max_val = 0
    
    for i in arr:
        counts[i] += 1
        if(counts[i] > max_val):
            max_val = counts[i]
            
    return len(arr) - max_val
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
