#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    maxSum = 0
    first = True
    for i in range(len(arr)-2):
        for j in range(1,len(arr[i])-1):
            if first:
                maxSum = calculateSum(arr,i,j)
                first = False
            else:
                total = calculateSum(arr,i,j)
                maxSum = max(maxSum,total)
    return maxSum

def calculateSum(arr, i, j):
    return (arr[i][j-1] + arr[i][j] + arr[i][j+1] + 
    arr[i+1][j] + 
    arr[i+2][j-1] + arr[i+2][j] + arr[i+2][j+1])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
