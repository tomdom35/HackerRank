#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    nums = []
    r = range(1,max(b)+1)
    for i in r:
        if passA(i,a) and passB(i,b):
            nums.append(i)
    return len(nums)

def passA(i,a):
    for j in a:
        if i%j != 0:
            return False
    return True

def passB(i,b):
    for j in b:
        if j%i != 0:
            return False
    return True

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
