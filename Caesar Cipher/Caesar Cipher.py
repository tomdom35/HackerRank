#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    k = k%26
    new_alpha = alpha[k:] + alpha[:k]
    new_s = ""
    for i in s:
        isUpper = i.isupper()
        if i.lower() in alpha:
            indx = alpha.index(i.lower())
            new_s += new_alpha[indx].upper() if isUpper else new_alpha[indx]
        else:
            new_s += i
    return new_s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
