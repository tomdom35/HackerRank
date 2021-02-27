#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    low = False
    num = False
    upp = False
    spe = False
    count = 0
    for i in password:
        if(low and num and upp and spe):
            break
        if(not low and i in "abcdefghijklmnopqrstuvwxyz"):
            low = True
        elif(not upp and i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            upp = True
        elif(not num and i in "0123456789"):
            num = True
        elif(not spe and i in "!@#$%^&*()-+"):
            spe = True
    if not low:
        count += 1
    if not upp:
        count += 1
    if not num:
        count += 1
    if not spe:
        count += 1
    if count + n < 6:
        count += 6-(count+n)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
