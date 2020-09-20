#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    minS = scores[0]
    maxS = scores[0]
    low = 0
    high = 0
    for s in scores[1:]:
        if s < minS:
            minS = s
            low += 1
        if s > maxS:
            maxS = s
            high += 1

    return [high,low]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
