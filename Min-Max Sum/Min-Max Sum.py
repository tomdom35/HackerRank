#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    min_h = arr[:]
    max_h = arr[:]
    heapq.heapify(min_h)
    heapq._heapify_max(max_h)
    heapq.heappop(min_h)
    heapq._heappop_max(max_h)
    print(str(sum(max_h)),str(sum(min_h)),end='')



if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
