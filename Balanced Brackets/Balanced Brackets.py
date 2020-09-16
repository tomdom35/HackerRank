#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    if(len(s) %2 != 0): return 'NO'
    if len(s)==2:
        if s[1] != endVal(s[0]) : return 'NO'
    else:
        s0 = s
        while(len(s0) > 0):
            c = s0[0]
            d = endVal(c)        
            endP = endPos(s0, c, d)
            if(endP == -1): return 'NO'
            s1 = s0[1:endP]
            if(isBalanced(s1) == 'NO'): return 'NO'
            if(endP != len(s0)-1):
                s0 = s0[endP+1:len(s0)]
            else:
                s0 = ''

    return 'YES'

def endVal(c):
    if c == '[': return ']'
    elif c == '{': return '}'
    elif c == '(': return ')'
    else: return ''

def endPos(s, c, d):
    newS = s[1:len(s)]
    n = 1
    for i in range(len(newS)):
        if newS[i] == c: n+=1
        elif newS[i] == d: n-=1
        if(n == 0):
            return i+1
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
