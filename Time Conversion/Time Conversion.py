#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    s1 = s

    if s.endswith("PM") and s[:2] != '12':
        h = int(s[:2])
        h+=12
        s1 = s[2:]
        s1 = str(h)+s1
    elif s[:2] == '12' and s.endswith("AM"):
        s1 = '00' + s[2:]

    return s1[:-2]

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
