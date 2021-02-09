#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    numAs = countAs(s)
    l = len(s)
    m = math.floor(n/l)
    mod = n%l
    newS = s[ 0 : mod ]
    return numAs*m + countAs(newS)

def countAs(s):
    return len([i for i in s if i == 'a'])
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
