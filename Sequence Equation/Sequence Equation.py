#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    idxs = []
    for x in range(1,len(p)+1):
        index_1 = p.index(x)
        index_1+=1
        index_2 = p.index(index_1)
        index_2+=1
        index_3 = p.index(index_2)
        idxs.append(p[index_3])
    return idxs
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
