#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    newBill = [0]
    if k == 0:
        newBill = bill[k+1]
    elif k == len(bill)-1:
        newBill = bill[:-1]
    else:
        newBill = bill[:k]
        b2 = bill[k+1:]
        newBill.extend(b2)
    owes = sum(newBill)/2
    if(b > owes):
        print(int(b-owes))
    else:
        print('Bon Appetit')


if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
