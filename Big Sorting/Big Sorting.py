#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the bigSorting function below.
def bigSorting(unsorted):
    buckets = defaultdict(list)
    for i in unsorted:
        buckets[len(i)].append(i)
    res = []    
    for k in sorted(buckets.keys()):
        res += sorted(buckets[k])
    return res
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
