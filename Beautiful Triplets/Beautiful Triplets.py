#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

# Complete the beautifulTriplets function below.
def beautifulTriplets(d, arr):
    total = 0
    for i in range(len(arr)):
        index1 = (len(arr)-1) - i
        val1 = arr[index1]
        for j in range(index1):
            index2 = (index1-1) - j
            val2 = arr[index2]
            if val1 - val2 == d:
                for k in range(index2):
                    index3 = (index2-1) - k
                    val3 = arr[index3]
                    if val2 - val3 == d:
                        total += 1
                    elif val2 - val3 > d:
                        break
            elif val1 - val2 > d:
                break
    return total
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
