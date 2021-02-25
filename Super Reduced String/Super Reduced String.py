#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    if len(s) == 1:
        return s
    p1 = 0
    p2 = 1
    
    while(p2 < len(s)):
        if(s[p1] == s[p2]):
            s = s[0 : p1 : ] + s[p2 + 1 : :]
            if p1 != 0:
                p1 -= 1
                p2 -= 1
        else:
            p1 += 1
            p2 += 1
    if(s == ''):
        return "Empty String"
    return s
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
