#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    febDays = 28
    if(year == 1918):
        febDays = 15
    elif(year > 1918 and (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0))):
        febDays = 29
    elif(year < 1918 and year % 4 == 0):
        febDays = 29
    
    days = [31,febDays,31,30,31,30,31,31,30,31,30,31]
    totalDays = sum(days[:8])
    monthNineDays = 256 - totalDays

    return str(monthNineDays) + '.09.' + str(year)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
