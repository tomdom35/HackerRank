#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    check = 'hackerrank'
    cur_letter_index = 0
    cur_letter = check[cur_letter_index]
    for i in s:
        if i == cur_letter:
            if(cur_letter_index == len(check)-1):
                return "YES"
            else:
                cur_letter_index += 1
                cur_letter = check[cur_letter_index]
    return "NO"
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
