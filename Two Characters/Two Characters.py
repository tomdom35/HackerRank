#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import permutations

# Complete the alternate function below.
def alternate(s):
    chars = []
    length = 0
    for i in s:
        if i not in chars:
            chars.append(i)
    for i in permutations(chars, 2):
        new_s = removeChars(i,s)
        cur_len = len(new_s)
        if(cur_len > length and isAlternating(new_s)):
            length = cur_len
    return length          
        
def removeChars(keep, s):
    new_s = ''
    for i in s:
        if i in keep:
            new_s += i
    return new_s

def isAlternating(s):
    if len(s) < 2:
        return False
    for index, i in enumerate(s):
        if(index < len(s)-1):
            if s[index] == s[index+1]:
                return False
    return True

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
