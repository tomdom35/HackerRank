#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the strangeCounter function below.
def strangeCounter(t):
    start_t = 1
    while(start_t <= t):
        start_v = math.ceil(start_t/3)*3
        new_start_t = start_t + start_v
        if(new_start_t > t):
            dif = t - start_t
            return start_v - dif
        start_t = new_start_t
    return start_t
            
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()
