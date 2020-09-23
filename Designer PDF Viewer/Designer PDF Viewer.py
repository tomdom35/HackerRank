#!/bin/python3

import math
import os
import random
import re
import sys
import string

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    maxH = 1
    heights = []
    for i in word:
        index = string.ascii_lowercase.index(i)
        heights.append(h[index])
    return len(word)*max(heights)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
