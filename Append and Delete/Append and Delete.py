#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    
    index = 0
    s_len = len(s)
    t_len = len(t)
    
    if(s_len + t_len <= k):
        return "Yes"
    
    if(s == t and k >= s_len):
        return "Yes"
    
    min_len = min(s_len,t_len)
    
    while(index < min_len and s[index] == t[index]):
        index+=1
        
    if(index == s_len):
        if(s_len == t_len and k == 0):
            return "Yes"
        if(s_len < t_len):
            val = t_len - s_len
            if(val == k):
                return "Yes"
            if(val < k and (k - val) % 2 == 0):
                return "Yes"
            return "No"
    if(index == t_len):
        val = s_len - t_len
        if(val == k):
            return "Yes"
        if(val < k and (k - val) % 2 == 0):
            return "Yes"
        return "No"

    s_num = s_len - index
    t_num = t_len - index
    
    val = s_num + t_num
    
    if(val == k or val < k):
        return "Yes"
    
    return "No"
        
        
            
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
