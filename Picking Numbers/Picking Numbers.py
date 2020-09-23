#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    maxLen = 0
    for index, val in enumerate(a):
        cur0 = val-1
        cur1 = val
        cur2 = val+1
        sub0 = [val]
        sub2 = [val]
        subMax = 1
        for i in range(index+1,len(a)):
            if a[i] == cur0 or a[i] == cur1:
                sub0.append(a[i])
            if a[i] == cur2 or a[i] == cur1:
                sub2.append(a[i])
        subMax = max([len(sub0),len(sub2)])
        if subMax > maxLen:
            maxLen = subMax
    return maxLen


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
