#!/bin/python3

import os
import sys

#
# Complete the equalStacks function below.
#
def equalStacks(h1, h2, h3):
    ht1 = sum(h1)
    ht2 = sum(h2)
    ht3 = sum(h3)

    while(ht1 != ht2 or ht1 != ht3):
        if(len(h1) == 0 or len(h2) == 0 or len(h3) == 0):
            return 0
        if ht1 > ht2 or ht1 > ht3:
            ht1-=h1[0]
            h1.pop(0)
        if ht2 > ht1 or ht2 > ht3:
            ht2-=h2[0]
            h2.pop(0)
        if ht3 > ht2 or ht3 > ht1:
            ht3-=h3[0]
            h3.pop(0)

    return ht1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
