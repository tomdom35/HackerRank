#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the runningTime function below.
def runningTime(arr):
    cur_arr = []
    count = 0
    for index, i in enumerate(arr):
        cur_arr.append(i)
        if(index == 0):
            continue
        n = index+1
        cur_val = cur_arr[n-1]
        for i in reversed(range(n-1)):
            if(cur_arr[i] <= cur_val):
                break
            count += 1
            new_arr = cur_arr.copy()
            new_arr[i+1] = cur_arr[i]
            cur_arr[i] = cur_val
            cur_arr[i+1] = new_arr[i]
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
