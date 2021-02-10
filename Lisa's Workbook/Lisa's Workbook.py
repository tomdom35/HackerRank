#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the workbook function below.
def workbook(n, k, arr):
    page = 0
    total = 0
    inc = True
    for i in arr:
        if(inc):
            page += 1
        for r in range(1, i+1):
            inc = True
            if(page == r):
                total += 1
            if(r%k == 0):
                page += 1
                inc = False              
    return total
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
