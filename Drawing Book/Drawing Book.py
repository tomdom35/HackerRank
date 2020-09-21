#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    if p == 1 or p == n or (n%2==1 and p == n-1):
        return 0

    front = p-1
    back = n-p
    flip = 0

    if front < back:
        cur = 1
        while p > cur:
            cur += 2
            flip += 1
    else:
        if n%2==0:
            cur = n
        else:
            cur = n-1
        while p < cur:
            cur -= 2
            flip += 1

    return flip

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
