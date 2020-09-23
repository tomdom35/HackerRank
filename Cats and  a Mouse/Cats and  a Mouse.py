#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    if x == y:
        return "Mouse C"
    if z < x and z < y:
        if min([x,y]) == x:
            return "Cat A"
        else:
            return "Cat B"
    elif z > x and z > y:
        if max([x,y]) == x:
            return "Cat A"
        else:
            return "Cat B"
    else:
        if x < y:
            if (z-x) < (y-z):
                return "Cat A"
            elif (z-x) > (y-z):
                return "Cat B"
            else:
                return "Mouse C"
        elif y < x:
            if (z-y) < (x-z):
                return "Cat B"
            elif (z-y) > (x-z):
                return "Cat A"
            else:
                return "Mouse C"




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
