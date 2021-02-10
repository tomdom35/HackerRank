#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    mn = len(a)+1
    for idx, i in enumerate(a):
        if i not in a[idx+1:]:
            continue
        index = a.index(i,idx+1,len(a))
        if(index - idx < mn):
            mn = index - idx
    if(mn == len(a)+1):
        return -1
    return mn

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
