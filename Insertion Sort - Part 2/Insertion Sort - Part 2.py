#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort2 function below.
def insertionSort2(n, arr):
    cur_arr = []
    for index, i in enumerate(arr):
        cur_arr.append(i)
        if(index == 0):
            continue
        cur_arr = insertionSort1(index+1,cur_arr)
        print_nums(cur_arr + arr[index+1:])
    
    
def insertionSort1(n, arr):
    cur_val = arr[n-1]
    for i in reversed(range(n-1)):
        if(arr[i] <= cur_val):
            break
        new_arr = arr.copy()
        new_arr[i+1] = arr[i]
        arr[i] = cur_val
        arr[i+1] = new_arr[i]
    return arr
    
def print_nums(nums):
    s = ''
    for i in nums:
        s += str(i) + ' '
    print(s)
    
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
