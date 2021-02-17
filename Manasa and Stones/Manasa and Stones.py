#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stones function below.
def stones(n, a, b):
    mx = a if a > b else b
    mn = a if mx == b else b
    mn_nums = n-1
    mx_nums = 0
    sol = []
    while(mx_nums < n):
        val = mn_nums*mn + mx_nums*mx
        if val not in sol:
            sol.append(val)
        mn_nums -= 1
        mx_nums += 1
    return sol

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        n = int(input())

        a = int(input())

        b = int(input())

        result = stones(n, a, b)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
