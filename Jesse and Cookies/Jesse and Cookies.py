#!/bin/python3

import os
import sys
import heapq
#
# Complete the cookies function below.
#
def cookies(k, A):
    heapq.heapify(A)
    c = 0

    while(A[0] < k and len(A) > 1):
        val1 = A[0]
        val2 = A[1]
        if len(A) > 2:
            val3 = A[2]
            if val3 < val2:
                newVal = val1 + (val3*2)
            else:
                newVal = val1 + (val2*2)
        else:
            newVal = val1 + (val2*2)
        heapq.heappop(A)
        heapq.heappop(A)
        heapq.heappush(A,newVal)
        c+=1

    if(A[0] < k):
        return -1

    return c
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
