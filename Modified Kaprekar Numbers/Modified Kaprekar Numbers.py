#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    nums = []
    for i in range(p,q+1):
        sl = len(str(i))
        st = str(i*i)
        l = len(st)
        first = st[:l-sl] if l > sl else '0'
        last = st[-sl:]
        if(int(first) + int(last) == i):
            nums.append(i)
    if len(nums) == 0:
        print("INVALID RANGE")
    else:
        for i in nums: 
            print(i, end =" ")
    
if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
