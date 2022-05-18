#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def numHelper(prev,num):
    if len(num) == 0 or num[0] == '0':
        return False
    for i in range(len(num)):
        n = int(num[:i+1])
        if(n == prev+1):
            if len(num[i+1:]) == 0:
                return True
            return numHelper(n,num[i+1:])
    return False
    

def separateNumbers(s):
    num = str(s)
    if len(num) == 1 or num[0] == '0':
        print('NO')
        return
    for i in range(len(num)):
        n = int(num[:i+1])
        if(numHelper(n,num[i+1:])):
            print('YES '+str(n))
            return
            break
    print('NO')
            
            
            
        

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
