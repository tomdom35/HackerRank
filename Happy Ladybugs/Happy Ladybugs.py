#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the happyLadybugs function below.
def happyLadybugs(b):
    if '_' in b:
        if empty_string(b):
            return 'YES'
        return count_bugs(b)
    return check_order(b)
    
def check_order(b):
    for index, bug in enumerate(b):
        left = index != 0 and b[index-1] == bug
        right = index != len(b)-1 and b[index+1] == bug
        if not(left or right):
            return 'NO'
    return 'YES'
            
        
def count_bugs(b):
    bug_type = []
    bug_count = []
    for i in b:
        if i in bug_type:
            index = bug_type.index(i)
            bug_count[index] += 1
        elif i != '_':
            bug_type.append(i)
            bug_count.append(1)
    for i in bug_count:
        if i == 1:
            return 'NO'
    return 'YES'
            
def empty_string(b):
    for i in b:
        if i != '_':
            return False
    return True

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
