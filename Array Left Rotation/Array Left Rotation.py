#!/bin/python3

import math
import os
import random
import re
import sys

def rotate(d, n, l):
    s = d % n
    first = l[:s]
    last = l[s:]
    return last+first

if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    a = rotate(d, n, a)

    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write(' '.join(map(str, a)))
