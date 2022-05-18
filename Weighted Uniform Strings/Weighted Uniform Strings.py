#!/bin/python3

import math
import os
import random
import re
import sys
import string

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def checkQ(q,w):
    for n in w:
        t = n[0]*n[1]
        if q < t:
            x = t - q
            if(x%n[0] == 0):
                return True
            else:
                continue
        elif q == t:
            return True
    
    return False

def weightedUniformStrings(s, queries):
    alpha = list(string.ascii_lowercase)
    p = 0
    c = 0
    i = 0
    l = ''
    w = []
    r = []

    while(p < len(s)):
        if(s[p] != l):
            if(l != ''):
                w.append([i,c])
            l = s[p]
            c = 1
            i = alpha.index(l) + 1
        else:
            c+=1
        p+=1
        
    w.append([i,c])
        
    for q in queries:
        ch = checkQ(q,w)
        if(ch):
            r.append('Yes')
        else:
            r.append('No')
    return r

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
