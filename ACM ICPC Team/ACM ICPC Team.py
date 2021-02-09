#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the acmTeam function below.
def acmTeam(topic):
    n = len(topic)
    m = len(topic[0])
    mx = 0
    num_mx = 0
    for i in range(n):
        if i+1 < n:
            for j in range(i+1,n):
                total = 0
                for k in range(m):
                    if topic[i][k] == '1' or topic[j][k] == '1':
                        total += 1
                if(total > mx):
                    mx = total
                    num_mx = 1
                elif(total == mx):
                    num_mx += 1
    return [mx,num_mx]
            
                    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
