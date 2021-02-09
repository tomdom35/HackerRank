#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    l = len(c)
    cur_index = 0
    num_jumps = 0
    while(cur_index != l-1):
        cur_index += 2 if (cur_index < l-2 and c[cur_index+2] == 0) else 1 if (cur_index < l-1 and c[cur_index+1] == 0) else 0
        num_jumps += 1
    return num_jumps
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
