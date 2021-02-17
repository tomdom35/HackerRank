#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cavityMap function below.
def cavityMap(grid):
    new_grid = []
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        if(i == 0 or i == rows-1):
            new_grid.append(grid[i])
            continue
        new_word = ""
        for j in range(cols):
            if j == 0 or j == cols-1:
                new_word += grid[i][j]
                continue
            if(deepest(grid,i,j)):
                new_word += "X"
            else:
                new_word += grid[i][j]
        new_grid.append(new_word)
        
    return new_grid
            
def deepest(grid,i,j):
    val = grid[i][j]
    return val > grid[i+1][j] and val > grid[i-1][j] and val > grid[i][j+1] and val > grid[i][j-1]
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
