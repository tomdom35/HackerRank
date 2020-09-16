#!/bin/python3

import os
import sys
import math

#
# Complete the runningMedian function below.
#
def runningMedian(a):
    maxHeap = []
    minHeap = []
    medians = [a[0],(a[0] + a[1])/2]

    if a[0] > a[1]:
        maxHeap = [a[1]]
        minHeap = [a[0]]
    else:
        maxHeap = [a[0]]
        minHeap = [a[1]]

    for n in a[2:len(a)]:
        if n < maxHeap[0]:
            addToMaxHeap(n, maxHeap)
        elif n > minHeap[0]:
            addToMinHeap(n, minHeap)
        elif len(maxHeap) > len(minHeap):
            addToMinHeap(n, minHeap)
        else:
            addToMaxHeap(n, maxHeap)

        if len(maxHeap) > len(minHeap) + 1:
            root = maxHeap[0]
            deleteFromMaxHeap(maxHeap)
            addToMinHeap(root,minHeap)
        elif len(minHeap) > len(maxHeap) + 1:
            root = minHeap[0]
            deleteFromMinHeap(minHeap)
            addToMaxHeap(root,maxHeap)

        if len(maxHeap) > len(minHeap):
            medians.append(maxHeap[0])
        elif len(minHeap) > len(maxHeap):
            medians.append(minHeap[0])
        else:
            medians.append((maxHeap[0] + minHeap[0]) / 2)

    return medians

def addToMaxHeap(n, heap):
    heap.append(n)
    ni = len(heap) - 1
    pi = getParentIndex(ni, heap)
    p = heap[pi]

    while(n > p):
        heap[ni] = p
        heap[pi] = n
        ni = pi

        if(ni > 0):
            pi = getParentIndex(ni, heap)
            p = heap[pi]
        else:
            p = n

def addToMinHeap(n, heap):
    heap.append(n)
    ni = len(heap) - 1
    pi = getParentIndex(ni, heap)
    p = heap[pi]

    while(n < p):
        heap[ni] = p
        heap[pi] = n
        ni = pi

        if(ni > 0):
            pi = getParentIndex(ni, heap)
            p = heap[pi]
        else:
            p = n

def deleteFromMaxHeap(heap):
    heap[0] = heap[len(heap)-1]
    heap.pop()

    n = heap[0]
    ni = 0
    cis = getChildrenIndicies(ni,heap)
    maxCi = -1
    maxC = -1

    if cis[0] > 0 and cis[1] > 0:
        maxCi = cis[0]
        if heap[cis[1]] > heap[cis[0]]:
            maxCi = cis[1]
        maxC = heap[maxCi]
    elif cis[0] > 0:
        maxCi = cis[0]
        maxC = heap[maxCi]
    elif cis[1] > 0:
        maxCi = cis[1]
        maxC = heap[maxCi]

    while(n < maxC):
        heap[ni] = maxC
        heap[maxCi] = n

        ni = maxCi
        cis = getChildrenIndicies(ni,heap)
        maxCi = -1
        maxC = -1

        if cis[0] > 0 and cis[1] > 0:
            maxCi = cis[0]
            if heap[cis[1]] > heap[cis[0]]:
                maxCi = cis[1]
            maxC = heap[maxCi]
        elif cis[0] > 0:
            maxCi = cis[0]
            maxC = heap[maxCi]
        elif cis[1] > 0:
            maxCi = cis[1]
            maxC = heap[maxCi]

def deleteFromMinHeap(heap):
    heap[0] = heap[len(heap)-1]
    heap.pop()

    n = heap[0]
    ni = 0
    cis = getChildrenIndicies(ni,heap)
    minCi = -1
    minC = 100000

    if cis[0] > 0 and cis[1] > 0:
        minCi = cis[0]
        if heap[cis[1]] < heap[cis[0]]:
            minCi = cis[1]
        minC = heap[minCi]
    elif cis[0] > 0:
        minCi = cis[0]
        minC = heap[minCi]
    elif cis[1] > 0:
        minCi = cis[1]
        minC = heap[minCi]

    while(n > minC):
        heap[ni] = minC
        heap[minCi] = n

        ni = minCi
        cis = getChildrenIndicies(ni,heap)
        minCi = -1
        minC = 100000

        if cis[0] > 0 and cis[1] > 0:
            minCi = cis[0]
            if heap[cis[1]] < heap[cis[0]]:
                minCi = cis[1]
            minC = heap[minCi]
        elif cis[0] > 0:
            minCi = cis[0]
            minC = heap[minCi]
        elif cis[1] > 0:
            minCi = cis[1]
            minC = heap[minCi]

def getChildrenIndicies(i, heap):
    cs = []
    if (i*2) + 1 > len(heap)-1:
        cs.append(-1)
    else:
        cs.append((i*2) + 1)
    if (i*2) + 2 > len(heap)-1:
        cs.append(-1)
    else:
        cs.append((i*2) + 2)
    return cs

def getParentIndex(i, heap):
    return int((i - 1) / 2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input())

    a = []

    for _ in range(a_count):
        a_item = int(input())
        a.append(a_item)

    result = runningMedian(a)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
