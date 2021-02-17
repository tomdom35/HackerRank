#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    s = sorted(c)
    d = max(s[0],(n-1)-s[len(s)-1])
    for i in range(len(s)):
        if(i < len(s)-1):
            sub = s[i+1] - s[i]
            if(sub > 1):
                sub = sub-1
                dist = math.ceil(sub/2)
                if(dist > d):
                    d = dist
    return d

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
