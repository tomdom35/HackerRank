#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    count = [0,0,0,0,0,0]
    max_index = 0
    max_count = 0

    for i in arr:
        count[i]+=1
    
    for index, val in enumerate(count):
        if val > max_count:
            max_count = val
            max_index = index
    
    return max_index

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
