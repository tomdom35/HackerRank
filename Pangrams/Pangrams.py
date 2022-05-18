#!/bin/python3

import math
import os
import random
import re
import sys
import string

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    alpha = list(string.ascii_lowercase)
    for i in s.lower():
        if i in alpha:
            alpha.remove(i)
    if len(alpha) > 0:
        return 'not pangram'
    else:
        return 'pangram'
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
