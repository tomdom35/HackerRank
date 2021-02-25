#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    cur_val = arr[n-1]
    for i in reversed(range(n-1)):
        if(arr[i] <= cur_val):
            break
        new_arr = arr.copy()
        new_arr[i+1] = arr[i]
        print_nums(new_arr)
        arr[i] = cur_val
        arr[i+1] = new_arr[i]
    print_nums(arr)
    
def print_nums(nums):
    s = ''
    for i in nums:
        s += str(i) + ' '
    print(s)
        

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
